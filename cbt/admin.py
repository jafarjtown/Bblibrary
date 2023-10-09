from django.contrib import admin
from .models import Course, Option, Question , TrueFalseQuestion, TrueFalseCourse
# Register your models here.
admin.site.register(Course)
admin.site.register(Question)

admin.site.register(Option)
admin.site.register(TrueFalseQuestion)
admin.site.register(TrueFalseCourse)