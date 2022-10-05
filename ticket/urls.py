from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('new-ticket', views.TicketCreateView.as_view(), name = 'ticket.create'),
    path('tickets/', views.TicketListView.as_view(), name = 'ticket.view'),
    path('tickets/<int:pk>', views.TicketDetailView.as_view(), name = 'ticket.detail'),
    path('tickets/complete/<int:pk>', views.MarkAsCompleted, name = 'ticket.completed'),
    path('tickets/login', views.TicketLoginInterfaceView.as_view(), name = 'login'),
    path('logout', views.TicketLogoutInterfaceView.as_view(), name = 'logout')
]
