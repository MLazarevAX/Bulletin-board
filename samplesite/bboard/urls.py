from .views import by_rubric, index, BbCreateView
from django.urls import path

urlpatterns = [
    path('add/', BbCreateView.as_view(), name='add'),
    path('<int:rubric_id>/', by_rubric, name='by_rubric'),
    path("", index, name='index')
]