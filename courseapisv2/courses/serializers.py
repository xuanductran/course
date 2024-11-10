from courses.models import Category,Course
from rest_framework import serializers
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields=['id','name']

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model=Course
        fields=['id','subject','description','image','category','active','created_date','updated_date']