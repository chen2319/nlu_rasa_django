from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('training', views.train, name='train'),
    # path('getIntent/<str:question>', views.get_intent, name='intent'),
]