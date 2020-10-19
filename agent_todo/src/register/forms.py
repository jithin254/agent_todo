from django import forms

from .models import Agent

class AgentForm(forms.ModelForm):
    class Meta:
        model = Agent
        widgets = {
        'password': forms.PasswordInput(),
    }

	