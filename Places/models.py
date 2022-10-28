from django.db import models
from django.forms import IntegerField
from geoposition import Geoposition

from Visitor.models import User
from geoposition.fields import GeopositionField

class PlacesDetails(models.Model):#post
    name=models.CharField(max_length=255,blank=False)
    city=models.CharField(max_length=20,blank=False)
    address=models.CharField(max_length=255,blank=False)
    picture=models.ImageField(null=True,blank=True,upload_to="images/Places/profile")
    visiting_time=models.CharField(max_length=20,null=True,blank=True)
    day_open=models.CharField(max_length=255,null=True,blank=True)
    fees=models.IntegerField(null=True,blank=True)
    month_to_visit=models.CharField(max_length=20,null=True,blank=True)
    position = GeopositionField()
    #for ML
    population_density=models.IntegerField(null=True, blank=True)
    avg_age=models.IntegerField(null=True,blank=True)
    avg_income=models.IntegerField(null=True,blank=True)
    police_station_count=models.IntegerField(null=True,blank=True)
    petroling_vans=models.IntegerField(null=True,blank=True)
    morality_level=models.IntegerField(null=True,blank=True)
#
    def __str__(self):
        return self.name; 

class PostImage(models.Model):
    post = models.ForeignKey(PlacesDetails, default=None, on_delete=models.CASCADE)
    images = models.ImageField(upload_to = 'images/Places')
 
    def __str__(self):
        return self.post.name+" "+self.post.city

class ComplaintsData(models.Model):
    CHOICES = (
        ('PENDING', 1),
        ('SUCCESS', 2),
    )
    user_id=models.ForeignKey(User,on_delete=models.CASCADE)
    complaint_title = models.CharField(max_length=200,blank=True)
    complaints_desc = models.TextField()
    name_of_place=models.CharField(max_length=255,blank=True)
    city=models.CharField(max_length=20,blank=False)
    date = models.DateField(blank=True)
    status = models.CharField(max_length=100, choices=CHOICES, default=1)

    def __str__(self):
        return self.complaint_title + " " + self.name_of_place

# Create your models here.
class RatingReview(models.Model):
    CHOICES =(
        (1,'VERY POOR'),
        (2,'POOR'),
        (3,'MEDIOCRE'),
        (4,'GOOD'),
        (5,'EXCELLENT'),
    )
    safety = models.CharField(max_length=100,choices=CHOICES,blank=True)
    sanitization = models.CharField(max_length=100,choices=CHOICES,blank=True)
    security = models.CharField(max_length=100,choices=CHOICES,blank=True)
    overall_fun = models.CharField(max_length=100,choices=CHOICES,blank=True)
    place = models.ForeignKey(PlacesDetails,on_delete=models.CASCADE)
    review = models.TextField(default='Awesome')
    user = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.place.name+" "+self.overall_fun
