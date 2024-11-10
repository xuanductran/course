from django.shortcuts import render
from courses.models import Category,Course
from . import serializers
# Create your views here.
from rest_framework import viewsets,generics
from . import paginators
class CategoryViewSet(viewsets.ViewSet,generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = serializers.CategorySerializer

class CourseViewSet(viewsets.ViewSet,generics.ListAPIView):
    queryset = Course.objects.filter(active=True).all()
    serializer_class = serializers.CourseSerializer
    pagination_class = paginators.ItemPaginator