from django.urls import path
from . import views

urlpatterns = [
    path('',views.index1),
    path('redirect',views.index6),
    path('process-money',views.index7),
]