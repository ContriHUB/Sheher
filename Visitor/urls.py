from django.urls import path
from Visitor import views
urlpatterns = [
    path('login/',views.user_login, name="user_login"),
    path('signup/',views.user_signup, name="user_signup"),
    path('profile/', views.profile, name="profile"),
    path('logout/',views.user_logout, name="user_logout"),
    path('SOS/',views.SOS,name="SOS"),
    path('edit-profile/',views.edit_profile,name="edit_profile"),
]
