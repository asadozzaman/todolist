from todolistapp import views
from django.urls import path

app_name = 'todolistapp'
urlpatterns = [
    path('',views.index,name='index'),
]