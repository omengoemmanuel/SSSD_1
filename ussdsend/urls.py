from django.urls import path
from . import views

urlpatterns = [
    path('ussd_handler', views.ussd_handler, name="ussd_handler"),
    path('sendussd', views.sendussd, name="sendussd")

]