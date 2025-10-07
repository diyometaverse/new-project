
from django.urls import path
from transaction import views

app_name = 'transaction'
urlpatterns = [
    path('dashboard/', views.transaction_page, name='dashboard'),
    path('add_transaction/', views.add_transaction, name='add_transaction'),
    
]
