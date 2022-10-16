from django.shortcuts import render
from Places.models import ComplaintsData, PlacesDetails, RatingReview
from Visitor.models import User, VisitorDetails
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render, redirect

from Visitor import urls
def Complaints(request):
    places=PlacesDetails.objects.all()
    user = request.user
    data={
        "user":user,
        "places":places,
    }
    return render(request,"Places/complaints.html",context=data);

def Save_Complaints(request):
    if request.user.is_authenticated:
        myfields=ComplaintsData()
        myfields.user_id=User.objects.get(email=request.user.email)
        myfields.complaint_title=request.POST['title']
        myfields.complaints_desc=request.POST['desc']
        myfields.name_of_place=PlacesDetails.objects.get(id=request.POST['place']).name;
        myfields.city = PlacesDetails.objects.get(id=request.POST['place']).city;
        myfields.date=request.POST['date']
        myfields.save()
        return HttpResponse("Complain Registerd. To go back <a href='/'>Click here</a>")
    else:
        all_places = PlacesDetails.objects.all()
        data = {
            'status' : '0',
            'places' : all_places,
        }
        render(request, "index.html", data)
# Create your views here.
def Rate_Review(request,pk):
    if request.user.is_authenticated:
        print(request.POST)
        place = PlacesDetails.objects.get(pk=pk)
        data ={
            'place':place,
            'rating': {1,2,3,4,5},
        }
        return render(request, "Places/RatingReview.html", context=data)
    return redirect('/')

def Review(request,pk):
    if request.user.is_authenticated:
        if request.POST:
            safety = request.POST['safety']
            security = request.POST['security']
            sanitization = request.POST['sanitization']
            overallfun = request.POST['overallfun']
            desc = request.POST['ta1']
            user = request.user
            place = PlacesDetails.objects.get(pk=pk)
            rating_review = RatingReview.objects.create(safety=safety,sanitization=sanitization,security=security,overall_fun=overallfun,place=place,user=user,review=desc)
            rating_review.save()
            return redirect('/')