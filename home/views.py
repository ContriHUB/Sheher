from django.shortcuts import render
from django.http import JsonResponse
from Places.models import PlacesDetails,RatingReview
from Visitor.models import VisitorDetails
import pickle
from django.template.loader import render_to_string
import collections
from collections import Counter

def homepage(request):
    all_places = PlacesDetails.objects.all()
    if request.user.is_authenticated:
        d = request.user
        profile_pic = VisitorDetails.objects.get(user_id=d).profile_picture
        all_reviews = []
        all_ratings = []
        for places in all_places:
            reviews = RatingReview.objects.filter(place=places)
            all_reviews.append(reviews)
        for reviews_qs in all_reviews:
            rating = 0
            count = 0
            for review in reviews_qs:
                rating+=int(review.safety)
                rating+=int(review.sanitization)
                rating+=int(review.security)
                rating+=int(review.overall_fun)
                count+=4
            if count == 0:
                all_ratings.append(0)
            else:
                all_ratings.append(round(rating/count, 1))
        # print(all_ratings)
        temp = {}
        for i in range(0,len(all_places)):
            temp[all_places[i]] = all_ratings[i]
        temp = dict(Counter(temp).most_common(5))
        top_places = {}
        for q,r in temp.items():
            for i in range(0,len(all_places)):
                if all_places[i]==q:
                    top_places[i+1] = q
        # print(top_places)
        data = {
            'places' : all_places,
            'user': d,
            'status': '1',
            'reviews': all_reviews,
            'ratings': all_ratings,
            'safety_index': '???',
            'top_places': top_places,
            'profile_pic':profile_pic,
        }
        return render(request, 'index.html', context=data)
    data = {
        'places': all_places,
        'status': '0',
    }
    return render(request, 'index.html', context=data)
# Create your views here.

def measure_safety(request,place_id):
    if request.is_ajax():
        place= PlacesDetails.objects.get(pk=place_id)
        #gender= VisitorDetails.objects.get(pk=user_id).gender
        #place=PlacesDetails.objects.get(name=place_name)
        d = request.user
        v= VisitorDetails.objects.get(user=d)
        gender = v.gender
        # print(gender)
        if gender == 'MALE': gender = 0
        elif gender =='FEMALE': gender = 1
        else: gender = 2
        income=place.avg_income
        density=place.population_density
        age=place.avg_age
        policestationcount=place.police_station_count
        petrolingvans=place.petroling_vans
        moralitylevel=place.morality_level

        result = getPrediction(gender, density, age, income , policestationcount, petrolingvans, moralitylevel)
        if result < 0: result=0
        print("prediction: ",result[0])
        result[0]*=10
        result[0]=100-result[0]
        return JsonResponse({'safety_index': round(result[0])})
    else:        
        return JsonResponse({'safety_index': "?!?"})

def getPrediction(gender, density, age, income , policestationcount, petrolingvans, moralitylevel):
    userdata = [[gender, density, age, income , policestationcount, petrolingvans, moralitylevel]]
    import os
    module_dir = os.path.dirname(__file__)  # get current directory
    file_path = os.path.join(module_dir, 'model2.sav')
    file2 = open(file_path, 'rb')   
    m2 = pickle.load(file2)
    file2.close()
    prediction2 = m2.predict(userdata)
    print(prediction2)

    file_path = os.path.join(module_dir, 'model3.sav')
    file3 = open(file_path, 'rb')   
    m3 = pickle.load(file3)
    file3.close()
    prediction3 = m3.predict(userdata)
    print(prediction3)

    file_path = os.path.join(module_dir, 'model4.sav')
    file4 = open(file_path, 'rb')   
    m4 = pickle.load(file4)
    file4.close()
    prediction4 = m4.predict(userdata)
    print(prediction4)

    file_path = os.path.join(module_dir, 'model5.sav')
    file5 = open(file_path, 'rb')   
    m5 = pickle.load(file5)
    file5.close()
    prediction5 = m5.predict(userdata)
    print(prediction5)
    return (prediction5 + prediction2 + prediction3 + prediction4)/4

def register(request):
    return render(request, 'home/register.html')

def places_view(request):
    ctx = {}
    url_parameter = request.GET.get("q")
    template = request.GET.get("template")

    if url_parameter:
        places = PlacesDetails.objects.filter(name__startswith=url_parameter)
    else:
        places = PlacesDetails.objects.all()

    ctx["places"] = places
    does_req_accept_json = request.accepts("application/json")
    is_ajax_request = request.headers.get("x-requested-with") == "XMLHttpRequest" and does_req_accept_json

    if is_ajax_request:

        html = render_to_string(
            template_name=template, context={"search_places": places}
        )
        data_dict = {"html_from_view": html}
        return JsonResponse(data=data_dict, safe=False)

    return render(request, "index.html", context=ctx)