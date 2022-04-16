from django.forms import ModelForm
from .models import Ticket, Update
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
#Antonio: form to register a new user into the system.
class TicketForm(ModelForm):
    class Meta:
        model = Ticket
        fields = '__all__'

class UpdateForm(ModelForm):
    class Meta:
        model = Update
        fields = '__all__'

class RegisterUser(UserCreationForm):
	email = forms.EmailField(widget = forms.EmailInput(attrs = {'class':'form-control'}))
	first_name = forms.CharField(max_length = 40,widget = forms.TextInput(attrs = {'class':'form-control'}))
	last_name = forms.CharField(max_length = 40,widget = forms.TextInput(attrs = {'class':'form-control'}))
	address = forms.CharField(max_length = 150,widget = forms.TextInput(attrs = {'class':'form-control'}))
	position = forms.CharField(max_length = 50,widget = forms.TextInput(attrs = {'class':'form-control'}))
	department = forms.CharField(max_length = 50,widget = forms.TextInput(attrs = {'class':'form-control'}))
	company = forms.CharField(max_length = 50,widget = forms.TextInput(attrs = {'class':'form-control'}))
	class Meta:
		model = User
		fields = ('username', 'first_name', 'last_name','email','password1','password2','address','company','position','department')

	def __init__(self,*args,**kwargs):
		super(RegisterUser,self).__init__(*args,**kwargs)

		self.fields['username'].widget.attrs['class'] = 'form-control'
		self.fields['password1'].widget.attrs['class'] = 'form-control'
		self.fields['password2'].widget.attrs['class'] = 'form-control'
