from django.urls import path
from . import views

app_name = 'Shop'

urlpatterns = [
     path('', views.index, name='home'),
     path('create_product', views.create_product, name='create_pr'),
     path('create_client', views.create_client, name='create_cl'),
     path('change_product/<int:pk>', views.edit_product, name='change_pr'),
     path('change_client/<int:pk>', views.edit_client, name='change_cl')
]
