from django.forms import ModelForm
from django.contrib.auth.models import User,Group
from .models import *
from django import forms

class SignUpForm(ModelForm):

	class Meta:
		model = User
		fields = ['first_name', 'last_name', 'email', 'username', 'password',]

class CreateGoalForm(forms.ModelForm):
	class Meta:
		model = ScrumyGoals
		fields = ('goal_name', 'user', 'goal_status')

class MoveGoalForm(forms.ModelForm):
    
	class Meta:
		model = ScrumyGoals
		fields = ( 'goal_name', 'user', 'goal_status' )
