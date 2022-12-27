from rest_framework import routers
from django.urls import re_path, include
from . import views

# use SimpleRouter() not the DefaultRouter() for closing the api end points
router = routers.SimpleRouter()

# register the models here
router.register(r'sample',views.SampleViewset)

urlpatterns = [
    re_path('^', include(router.urls)),
]
