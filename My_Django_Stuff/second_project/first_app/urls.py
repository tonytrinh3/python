from django.urls import path
from first_app import views

urlpatterns = [
    path('',views.index, name ='index'),
    path('webpages/',views.webpage_name, name ='webpage_name')
]