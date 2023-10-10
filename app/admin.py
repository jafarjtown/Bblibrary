from django.contrib import admin

from .models import Course, Department,Material, PastQuestion
# Register your models here.


admin.site.register(Material)
admin.site.register(Course)
admin.site.register(PastQuestion)
admin.site.register(Department)
