from rest_framework import serializers
from .models import SampleModel

class SampleModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = SampleModel
        fields  =('id','title','image')





# sample when content has foreignField nav and related_name content and two tables are interconnected

# class ContentSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Content
#         fields = ('id','title','author','subtitle','datetime','image','body','nav')


# class NavSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Nav
#         fields = ('id','category')

# class NavFullSerializer(serializers.ModelSerializer):
#     contents = ContentSerializer(many=True)
#     class Meta:
#         model = Nav
#         fields = ('id','category','contents')