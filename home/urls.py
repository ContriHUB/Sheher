from django.urls import path
from home import views
urlpatterns = [
    path('',views.homepage, name = "home"),
    path('register/', views.register,name = "register"),
    path('search/',views.search,name='search'),
    path('<int:place_id>/measure_safety/',views.measure_safety, name="measure_safety"),
]
