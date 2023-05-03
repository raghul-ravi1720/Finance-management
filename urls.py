from django.contrib import admin
from django.urls import path
from .views import *


urlpatterns = [
    path('add_transaction/', add_transaction, name='add_transaction'),
    
    path('transactions/', TransactionListView, name='transaction_list'),
    
    path('my_view/', my_view, name='my_view'),

]
