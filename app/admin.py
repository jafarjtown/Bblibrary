from django.contrib import admin

from .models import Course, Department,Material
# Register your models here.


admin.site.register(Material)
admin.site.register(Course)
admin.site.register(Department)