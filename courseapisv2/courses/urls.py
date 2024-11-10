
from django.urls import path, re_path, include
from courses.admin import admin_site
from rest_framework.routers import DefaultRouter
from . import views

r = DefaultRouter()
r.register('categories',views.CategoryViewSet,basename='cate')
r.register('courses',views.CourseViewSet,basename='course')

urlpatterns = [
    path('', include(r.urls)),
]
