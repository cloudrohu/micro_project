from django.contrib import admin

from .models import *

# Register your models here.
class HeaderAdmin(admin.ModelAdmin):
    list_display = ['id','logo','logo_2', 'color']
admin.site.register(Header,HeaderAdmin)


class Web_SliderAdmin(admin.ModelAdmin):
    list_display = ['id','web_image','mobile_image', 'title']
admin.site.register(Web_Slider,Web_SliderAdmin)