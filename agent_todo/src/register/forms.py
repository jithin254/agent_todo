from django import forms

from .models import Agent

class AgentForm(forms.ModelForm):
    class Meta:
        password = forms.CharField(widget=forms.PasswordInput)
        model = Agent
        fields = '__all__'
        widgets = {
            'password': forms.PasswordInput(),
        }

	