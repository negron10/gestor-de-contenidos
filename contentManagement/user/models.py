from django.db import models

class Role(models.Model):
	name  = models.CharField(max_length=30)
	STAT = (('1', 'Activo'),('0','Inactivo'))
	status = models.CharField(max_length=1,choices=STAT,default='1')
	def __str__(self):
		return self.name

class User(models.Model):
	name = models.CharField(max_length=30)
	last_name = models.CharField(max_length=30)
	birthday = models.DateField()
	SEX = (('F', 'Femenino'),('M','Masculino'),('O','Otro'))
	gender = models.CharField(max_length=1,choices=SEX,default='M')
	telephone = models.CharField(max_length=15)
	email = models.EmailField()
	password = models.CharField(max_length=40)
	city = models.CharField(max_length=30)
	country = models.CharField(max_length=30)
	picture = models.ImageField(upload_to='pictures')
	STAT = (('1', 'Activo'),('0','Inactivo'))
	status = models.CharField(max_length=1,choices=STAT,default='1')
	role = models.ForeignKey(Role, on_delete=models.CASCADE)
	#local = models.ForeignKey('comercio.Local', related_name='secciones', on_delete=models.CASCADE)

	def __str__(self):
		return '%s %s' % (self.name, self.last_name)
	
