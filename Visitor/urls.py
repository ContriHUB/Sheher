from django.urls import path
from Visitor import views
urlpatterns = [
    path('login/',views.user_login, name="user_login"),
    path('signup',views.user_signup, name="user_signup"),
    path('profile/', views.profile, name="profile"),
    path('logout/',views.user_logout, name="user_logout"),
    path('safety_check/',views.safety_check, name="safety_check"),
    path('<int:place_id>/measure_safety/',views.measure_safety, name="measure_safety"),
    path('SOS/',views.SOS,name="SOS"),
    path('edit-profile',views.edit_profile,name="edit_profile"),
]
