from django.shortcuts import render
from Places.models import PlacesDetails,RatingReview

def homepage(request):
    if request.user.is_authenticated:
        d = request.user
        all_places = PlacesDetails.objects.all()
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
        data = {
            'places' : all_places,
            'user': d,
            'status': '1',
            'reviews': all_reviews,
            'ratings': all_ratings,
        }
        return render(request, 'index.html', context=data)
    all_places = PlacesDetails.objects.all()
    data = {
        'places': all_places,
        'status': '0',
    }
    return render(request, 'index.html', context=data)
# Create your views here.

def register(request):
    return render(request, 'home/register.html')

def search(request):
    if request.POST:
        search_text = request.POST['search_field']
        records = PlacesDetails.objects.filter(name__contains=search_text)
        data = {
            'user' : request.user,
            'places' : records,
        }
        return render(request,'Visitor/search_result.html',context=data)