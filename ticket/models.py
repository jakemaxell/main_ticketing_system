from django.db import models

class Ticket(models.Model):
    name = models.CharField(max_length = 50)
    title = models.CharField(max_length = 200)
    type = models.CharField(max_length = 200)
    description = models.TextField()
    created = models.DateTimeField(auto_now_add = True)
    completed = models.BooleanField(default = False)
    completedDate = models.DateField(null = True, blank = True)
    completedBy = models.CharField(max_length = 100)