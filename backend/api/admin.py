from django.contrib import admin
from .models import SampleModel

# Register your models here.
@admin.register(SampleModel)
class SampleModelAdmin(admin.ModelAdmin):
    fields = ('title','image',)
    list_display = ('id','title','image')

# tinyInject.js is added incase textfield is added
    # class Media:
    #     js = ('tinyInject.js',)