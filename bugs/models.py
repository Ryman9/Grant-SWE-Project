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
    )

    # for categories, wasn't sure what all to include for now
    # can be easily modified by adding tuples here
    CATEGORY = (
        ('Front End', 'Front End'),
        ('Back End', 'Back End'),
    )

    URGENCY = (
        ('Red', 'Red'),
        ('Yellow', 'Yellow'),
        ('Green', 'Green'),
    )

    ticketId = models.AutoField(primary_key=True)
    title = models.CharField(max_length=80, null=True)
    description = models.CharField(max_length=255, null=True)
    status = models.CharField(max_length=100, null=True, choices=STATUS)
    category = models.CharField(max_length=20, null=True, choices=CATEGORY)
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