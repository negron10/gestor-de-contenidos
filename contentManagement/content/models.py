from django.db import models
from user.models import User

class Category(models.Model):
	name  = models.CharField(max_length=30)
	STAT = (('1', 'Activo'),('0','Inactivo'))
	status = models.CharField(max_length=1,choices=STAT,default='1')
	def __str__(self):
		return self.name

class Content(models.Model):
	title  = models.CharField(max_length=30)
	subtitle = models.CharField(max_length=30)
	content = models.CharField(max_length=1000)
	createDate = models.DateField()
	STAT = (('1', 'Activo'),('0','Inactivo'))
	status = models.CharField(max_length=1,choices=STAT,default='1')
	category = models.ForeignKey(Category, on_delete=models.CASCADE)
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	def __str__(self):
		return self.title

class Comment(models.Model):
	text = models.CharField(max_length=1000)
	createDate = models.DateField()
	STAT = (('1', 'Activo'),('0','Inactivo'))
	status = models.CharField(max_length=1,choices=STAT,default='1')
	content = models.ForeignKey(Content, on_delete=models.CASCADE)
	def __str__(self):
		return self.text

class File(models.Model):
	name = models.CharField(max_length=50)
	extension = models.CharField(max_length=30)
	uploadDate = models.DateField()
	STAT = (('1', 'Activo'),('0','Inactivo'))
	status = models.CharField(max_length=1,choices=STAT,default='1')
	content = models.ForeignKey(Content, on_delete=models.CASCADE)
	def __str__(self):
		return self.name

	
