from django.forms import ModelForm
from .models import Ticket, Update

class TicketForm(ModelForm):
    class Meta:
        model = Ticket
        fields = '__all__'

class UpdateForm(ModelForm):
    class Meta:
        model = Update
        fields = '__all__'