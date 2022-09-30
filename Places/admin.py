from django.contrib import admin
from Places.models import PlacesDetails,ComplaintsData,RatingReview

admin.site.register(ComplaintsData)
admin.site.register(RatingReview)
# admin.site.register(PlacesDetails)
# Register your models here.
from Places.models import PostImage

class PostImageAdmin(admin.StackedInline):
    model = PostImage

@admin.register(PlacesDetails)
class PostAdmin(admin.ModelAdmin):
    inlines = [PostImageAdmin]

    class Meta:
       model = PlacesDetails

@admin.register(PostImage)
class PostImageAdmin(admin.ModelAdmin):
    pass
