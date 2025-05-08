from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.orderFormView, name='order_url'),
    path('show/', views.showView, name='show_url'),
    path('update/<int:f_oid>/', views.updateView, name='update_url'),
    path('delete/<int:f_oid>/', views.deleteView, name='delete_url'),
]
