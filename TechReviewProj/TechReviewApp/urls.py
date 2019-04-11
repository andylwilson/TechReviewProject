from django.urls import path
from . import views

# project url directs to this, which directs to the proper view
urlpatterns=[
    path('', views.index, name='index'),

]