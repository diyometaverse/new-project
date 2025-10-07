
from django.urls import path
from ordering import views

app_name = 'ordering'
urlpatterns = [
    
    path('list/', views.ordering_list, name='list'),
    
]
