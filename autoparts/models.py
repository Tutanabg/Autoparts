from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.serializers import serialize



class Body(models.Model):
	body_name = models.CharField(max_length= 100)
	body_price = models.IntegerField(null=True) 
	def serialize(self):
		return {
		"id": self.id,
		"name": self.body_name,
		"price": self.body_price,
        }
     
     

class Doors(models.Model):
	doors_name = models.CharField(max_length=100) 
	doors_price = models.IntegerField(null=True) 
	def serialize(self):
		return {
		"id": self.id,
		"doors_name": self.doors_name, 
		"doors_price": self.doors_price,
		}
     


class AVDevices(models.Model):
	av_name = models.CharField(max_length=100)
	av_price = models.IntegerField(null=True) 
	def serialize(self):
		return {
		"id": self.id,
		"av_name": self.av_name,
		"av_price": self.av_price,
		}
     
     
class Cameras(models.Model):
	cameras_name = models.CharField(max_length=100) 
	cameras_price = models.IntegerField(null=True) 
	def serialize(self):
		return {
		"id": self.id,
		"cameras_name": self.cameras_name,
		"cameras_price": self.cameras_price,
		}
	
	
	
class Windows(models.Model):
	windows_name = models.CharField(max_length=100) 
	windows_price = models.IntegerField(null=True) 
	def serialize(self):
		return {
		"id": self.id,
		"windows_name": self.windows_name,
		"windows_price": self.windows_price,
		}
     
  
class Payment(models.Model):
	name = models.CharField(max_length=100) 
	price = models.IntegerField(null=True) 
	card_number = models.IntegerField(null=True) 
	expiration = models.DateTimeField(auto_now_add=True) 
	def serialize(self):
         return {
         "id": self.id,
		"name": self.name,
		"price": self.price,
		"card_number": self.card_number,
		"expiration": self.expiration,
         
        }
     
    
     
class User(AbstractUser):
	pass



