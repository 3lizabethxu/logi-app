from django.urls import path
from . import views

urlpatterns = [
    path('', views.products),
    path('products/', views.products, name='products'),
    path('warehouses/', views.warehouses, name='warehouses'),

    path('create_inventory/', views.createInventory, name='create_inventory'),
    path('update_inventory/<str:pk>/<', views.updateInventory, name='update_inventory'),
    path('delete_inventory/<str:pk>/<', views.deleteInventory, name='delete_inventory'),

    path('create_warehouse/<', views.createWarehouse, name='create_warehouse'),
    path('update_warehouse/<str:pk>/<', views.updateWarehouse, name='update_warehouse'),

]