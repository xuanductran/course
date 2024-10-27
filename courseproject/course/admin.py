from django.contrib import admin
from course.models import Category,Lesson,Course
from django.utils.html import mark_safe
class LessonAdmin(admin.ModelAdmin):
    list_display = ["id","subject","content"]


    def avater(self,lesson):
        return mark_safe(f"<img src='' />")


admin.site.register(Category)
admin.site.register(Lesson,LessonAdmin)
admin.site.register(Course)
# Register your models here.
