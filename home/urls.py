from django.urls import path
from home import views
urlpatterns = [
    path('',views.homepage, name = "home"),
    path('register/', views.register,name = "register"),
    path('search/',views.places_view,name='search'),
    path('<int:place_id>/meaure_preference/',views.meaure_preference, name="meaure_preference"),
]
