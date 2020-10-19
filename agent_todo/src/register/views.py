from django.shortcuts import render
from .models import Agent
from .forms import AgentForm
# Create your views here.

def agent_register_view(request):
	my_form = AgentForm()
	context = {
		'form' : my_form	
	}
	return render(request,"register_view.html",context)