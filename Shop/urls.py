from django.urls import path
from . import views

app_name = 'Shop'

urlpatterns = [
     path('', views.index, name='home'),
     path('create_product', views.create_product, name='create'),
     path('create_costumer', views.create_costumer, name='create'),
     path('change/<int:pk>', views.edit_product, name='change'),
     path('change_product/<int:pk>', views.edit_product, name='change'),
     path('change_costumer/<int:pk>', views.edit_costumer, name='change')
]
