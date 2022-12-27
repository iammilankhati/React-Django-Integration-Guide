from django.shortcuts import render
from rest_framework import viewsets
from .models import SampleModel
from .serializers import SampleModelSerializer
from rest_framework.response import Response


class SampleViewset(viewsets.ModelViewSet):
    queryset = SampleModel.objects.all()
    serializer_class = SampleModelSerializer

#sample viewset for nav navfull serializers for excessing contents details only when nav is excessed singly
# This case comes when two tables are interconnected by foreing fields.   

# class NavViewset(viewsets.ModelViewSet):
#     queryset = Nav.objects.all()
#     serializer_class = NavSerializer

#     """
#     Retrieve a model instance.
#     """
#     def retrieve(self, request, *args, **kwargs):
#         instance = self.get_object()
#         serializer = NavFullSerializer(instance, many=False, context={'request':request})
#         return Response(serializer.data)

# class ContentViewset(viewsets.ModelViewSet):
#     queryset = Content.objects.all()
#     serializer_class = ContentSerializer

