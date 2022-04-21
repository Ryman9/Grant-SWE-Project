from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import Ticket, Update

#Antonio: form to register a new user into the system.
class TicketForm(ModelForm):
	class Meta:
		model = Ticket
		fields = '__all__'

	def __init__(self,*args,**kwargs):
		super(TicketForm,self).__init__(*args,**kwargs)

		self.fields['title'].widget.attrs['class'] = 'form-control'
		self.fields['description'].widget = forms.Textarea()
		self.fields['description'].widget.attrs['class'] = 'form-control'
		self.fields['description'].required = False
		self.fields['status'].widget.attrs['class'] = 'custom-select'
		self.fields['category'].widget.attrs['class'] = 'form-control'
		self.fields['urgency'].widget.attrs['class'] = 'custom-select'
		self.fields['createdBy'].widget.attrs['class'] = 'custom-select'
		self.fields['createdBy'].label = 'Created By'
		self.fields['assignedTo'].widget.attrs['class'] = 'custom-select'
		self.fields['assignedTo'].label = 'Assigned To'

class UpdateForm(ModelForm):
    class Meta:
        model = Update
        fields = '__all__'

class LoginUserForm(forms.Form):
	username = forms.CharField(max_length=40, widget=forms.TextInput(attrs = {'class':'form-control'}))
	password = forms.CharField(max_length=50, widget=forms.PasswordInput(attrs = {'class':'form-control'}))

class RegisterUserForm(UserCreationForm):
	email = forms.EmailField(widget = forms.EmailInput(attrs = {'class':'form-control'}))
	first_name = forms.CharField(required=False, max_length=40, widget = forms.TextInput(attrs = {'class':'form-control'}))
	last_name = forms.CharField(required=False, max_length=40, widget = forms.TextInput(attrs = {'class':'form-control'}))
	address = forms.CharField(required=False, max_length=150, widget = forms.TextInput(attrs = {'class':'form-control'}))
	position = forms.CharField(required=False, max_length=50, widget = forms.TextInput(attrs = {'class':'form-control'}))
	department = forms.CharField(required=False, max_length=50, widget = forms.TextInput(attrs = {'class':'form-control'}))
	company = forms.CharField(required=False, max_length=50, widget = forms.TextInput(attrs = {'class':'form-control'}))
	class Meta:
		model = User
		fields = ('username','first_name','last_name','email','password1','password2','address','company','position','department')

	def __init__(self,*args,**kwargs):
		super(RegisterUserForm,self).__init__(*args,**kwargs)

		self.fields['username'].widget.attrs['class'] = 'form-control'
		self.fields['password1'].widget.attrs['class'] = 'form-control'
		self.fields['password2'].widget.attrs['class'] = 'form-control'
