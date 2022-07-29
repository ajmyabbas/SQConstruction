from django import views
from django.urls import include, path
from.import views

urlpatterns = [
    path('',views.load_home,name='load_home'),
    path('internship',views.internship,name='internship'),
    path('learnmore',views.learnmore,name='learnmore'),
]