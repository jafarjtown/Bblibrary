from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="cbt"),
    path("<int:id>/test", views.cbt_test, name="cbt_test"),
    path("<int:id>/test/answers", views.cbt_test_result, name="cbt_test_result"),
]
