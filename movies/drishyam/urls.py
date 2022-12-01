from django.urls import path
from drishyam import views

urlpatterns = [
   path("",views.renderindex)
]
