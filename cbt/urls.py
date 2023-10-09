from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="cbt"),
    path("tests/", views.tests, name="cbt_tests"),
    path("<int:id>/test", views.cbt_test, name="cbt_test"),
    path("<int:id>/test/essay", views.cbt_test_essay, name="cbt_test_essay"),
    path("<int:id>/test/answers", views.cbt_test_result, name="cbt_test_result"),
    path('courses', views.cbt_create_course, name="cbt_create_course"),
    path('courses/essays/', views.cbt_create_course_essay, name="cbt_create_course_essay"),
    path('courses/add/questions/<int:course>/', views.cbt_add_qs, name="cbt_add_qs"),
    path('courses/add/upload/', views.add_by_upload, name="cbt_course_by_upload"),
    path('courses/essay/upload/', views.add_by_upload_essay, name="cbt_course_by_upload_essay"),
    path('essay', views.essay_cbt, name="essay_cbt"),
    path('true-false', views.true_false_test, name="true_false_test"),
    path('true-false/test/<int:tid>', views.true_false_result, name="true_false_result"),
]
