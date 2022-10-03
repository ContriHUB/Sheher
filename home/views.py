from django.shortcuts import render
from Places.models import PlacesDetails,RatingReview

def homepage(request):
    if request.user.is_authenticated:
        d = request.user
        all_places = PlacesDetails.objects.all()
        rating_all=[]
        for places in all_places:
            rating = RatingReview.objects.filter(place=places)
            rating_all.append(rating)
        data = {
            'places' : all_places,
            'user': d,
            'rating':rating_all,
            'status': '1',
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