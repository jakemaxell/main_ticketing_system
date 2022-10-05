from django.contrib import admin
from . import models

class TicketAdmin(admin.ModelAdmin):
    list_display = ('title', 'type', 'name', 'created', 'completedDate', 'completedBy', 'completed')

admin.site.register(models.Ticket, TicketAdmin)