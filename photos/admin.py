from django.contrib import admin
from .models import Photo


#customizzare l'interfaccia admin
class PhotoAdmin(admin.ModelAdmin):
    list_display = ('__unicode__','upload_date' ,'votes', 'match_number')



# Register your models here.
admin.site.register(Photo, PhotoAdmin)
