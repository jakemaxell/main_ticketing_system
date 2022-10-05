from datetime import datetime
from django.shortcuts import redirect
from django.views.generic import CreateView, ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from .models import Ticket
from .forms import TicketForm

class TicketCreateView(CreateView):
    model = Ticket
    success_url = '/'
    form_class = TicketForm
    template_name = 'ticket_form.html'

class TicketListView(LoginRequiredMixin, ListView):
    model = Ticket
    context_object_name = 'tickets'
    template_name = 'tickets_list.html'
    login_url = 'login'

class TicketDetailView(DetailView):
    model = Ticket
    context_object_name = 'ticket'
    template_name = 'ticket_detail.html'

class TicketLoginInterfaceView(LoginView):
    template_name = 'login.html'

class TicketLogoutInterfaceView(LogoutView):
    template_name = 'home.html'

def MarkAsCompleted(request, pk):
    user = request.user
    ticket = Ticket.objects.get(pk = pk)
    ticket.completed = True
    ticket.completedDate = datetime.now()
    ticket.completedBy = user.username
    ticket.save()
    return redirect('ticket.view')