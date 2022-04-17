from .views import by_rubric, index
from django.urls import path

urlpatterns = [
    path('<int:rubric_id>/', by_rubric),
    path("", index)
]