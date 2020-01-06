from django.db import models
from person.models import Person

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
	createDate = models.DateTimeField(auto_now_add=True)
	updateDate = models.DateTimeField(auto_now=True)
	createDates = models.DateField(auto_now_add=True)
	STAT = (('1', 'Activo'),('0','Inactivo'))
	status = models.CharField(max_length=1,choices=STAT,default='1')
	category = models.ForeignKey(Category, on_delete=models.CASCADE)
	person = models.ForeignKey(Person, on_delete=models.CASCADE)
	def __str__(self):
		return self.title

class Comment(models.Model):
	text = models.CharField(max_length=1000)
	createDate = models.DateTimeField(auto_now_add=True)
	updateDate = models.DateTimeField(auto_now=True)
	createDates = models.DateField(auto_now_add=True)
	STAT = (('1', 'Activo'),('0','Inactivo'))
	status = models.CharField(max_length=1,choices=STAT,default='1')
	content = models.ForeignKey(Content, on_delete=models.CASCADE)
	person = models.ForeignKey(Person, on_delete=models.CASCADE)
	def __str__(self):
		return self.text

class File(models.Model):
	name = models.CharField(max_length=50)
	extension = models.CharField(max_length=30)
	uploadDate = models.DateTimeField(auto_now_add=True)
	uploadDates = models.DateField(auto_now_add=True)
	STAT = (('1', 'Activo'),('0','Inactivo'))
	status = models.CharField(max_length=1,choices=STAT,default='1')
	uploads = models.FileField(upload_to='uploads')
	content = models.ForeignKey(Content, on_delete=models.CASCADE)
	def __str__(self):
		return self.name

