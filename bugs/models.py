from django.db import models

# Create your models here.
class Employee(models.Model):
    userId = models.AutoField(primary_key=True)
    firstName = models.CharField(max_length=50, null=True)
    lastName = models.CharField(max_length=75, null=True)
    username = models.CharField(max_length=50, null=True)
    department = models.CharField(max_length=20, null=True)
    position = models.CharField(max_length=20, null=True)

    def __str__(self):
        return self.username

class Ticket(models.Model):
    STATUS = (
        ('Created', 'Created'),
        ('In Progress', 'In Progress'),
        ('Completed', 'Completed'),
        ('Void', 'Void'),
    )

    URGENCY = (
        ('Green', 'Green'),
        ('Yellow', 'Yellow'),
        ('Red', 'Red'),
    )

    ticketId = models.AutoField(primary_key=True)
    title = models.CharField(max_length=80, null=True)
    description = models.CharField(max_length=255, null=True)
    status = models.CharField(max_length=100, null=True, choices=STATUS)
    category = models.CharField(max_length=20, null=True)
    urgency = models.CharField(max_length=50, null=True, choices=URGENCY)
    timestamp = models.DateTimeField(auto_now_add=True, null=True)
    createdBy = models.ForeignKey(Employee, null=True, on_delete=models.SET_NULL, related_name='createdBy')
    assignedTo = models.ForeignKey(Employee, null=True, on_delete=models.SET_NULL, related_name='assignedTo')

    def __str__(self):
        return self.title

class Update(models.Model):
    updateId = models.AutoField(primary_key=True)
    description = models.CharField(max_length=255)
    madeBy = models.ForeignKey(Employee, null=True, on_delete=models.SET_NULL)
    onTicket = models.ForeignKey(Ticket, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.description