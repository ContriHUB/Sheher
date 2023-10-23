from django.urls import path
from Places import views
urlpatterns = [
    path('complaints',views.Complaints,name = 'report'),
    path('save-complaints',views.Save_Complaints, name='report_complaint'),
    path('rate_and_review/<int:pk>/',views.Rate_Review,name='rate_review'),
    path('save_review/<int:pk>/',views.Review,name='save_review'),
    path('',views.all_places, name="all_places"),
]
