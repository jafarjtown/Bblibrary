from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="cbt"),
    path("<int:id>/test", views.cbt_test, name="cbt_test"),
    path("<int:id>/test/answers", views.cbt_test_result, name="cbt_test_result"),
    path('courses', views.cbt_create_course, name="cbt_create_course"),
    path('courses/add/questions/<int:course>/', views.cbt_add_qs, name="cbt_add_qs"),
    path('courses/add/upload/', views.add_by_upload, name="cbt_course_by_upload")
]
