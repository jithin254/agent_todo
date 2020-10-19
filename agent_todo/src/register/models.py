from django.db import models

# Create your models here.
class Agent(models.Model):
	agent_id	= models.CharField(max_length=120)
	password	= models.CharField(max_length=120)

