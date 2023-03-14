from django.urls import path
from . import views

urlpatterns = [
    path('hello', views.hello, name= 'hello'),
    path('hi', views.hi, name= 'hi'),

    path('ourview', views.OurView.as_view(), name="our_view"),
]

