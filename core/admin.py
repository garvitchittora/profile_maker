from django.contrib import admin
from .models import profile
# Register your models here.
@admin.register(profile)
class profile(admin.ModelAdmin):
    list_display = ('name','img','cover_img','discription','education','experience','skills','linkedin_url')