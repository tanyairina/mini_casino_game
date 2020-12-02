
from django.urls import path
from . import views

urlpatterns = [
    path('', views.process_money),
    path('process_money', views.process_gold),
    path('reset', views.reset)
]
