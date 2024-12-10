from django.urls import path
from .views import CreateView,ListQueryView,RetrieveQueryView

urlpatterns = [
  path('',CreateView.as_view(),name='create'),
  path('all/',ListQueryView.as_view(),name='listquery'),
  path('all/<int:pk>/',RetrieveQueryView.as_view(),name='listquery'),
]
