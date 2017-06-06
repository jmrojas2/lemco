from django.db import models
from django.utils import timezone

class work_file(models.Model):
	number 					= models.CharField('Número de Archivo', max_length = 20)
	actual_process			= models.IntegerField(default='0')
	status 					= models.CharField(default='pendiente', max_length=10)
	area					= models.CharField(default='-', max_length=10)
	accumulated_time 		= models.CharField(default='0', max_length=100)
	actual_time				= models.CharField(default='0', max_length=100)
	ini_date_process		= models.DateTimeField(default=timezone.now)
	finish_date_process		= models.DateTimeField(default=timezone.now)
	ini_date				= models.DateTimeField(default=timezone.now)
	time_process1			= models.CharField(default='-', max_length=100)
	time_process2			= models.CharField(default='-', max_length=100)
	time_process3			= models.CharField(default='-', max_length=100)
	time_process4			= models.CharField(default='-', max_length=100)
	status_one 				= models.CharField(max_length=10, default='pendiente')
	status_two 				= models.CharField(max_length=10, default='pendiente')
	status_three 			= models.CharField(max_length=10, default='pendiente')
	status_four 			= models.CharField(max_length=10, default='pendiente')
	ini_date_process1		= models.DateTimeField(null=True, blank=True)
	ini_date_process2		= models.DateTimeField(null=True, blank=True)
	ini_date_process3		= models.DateTimeField(null=True, blank=True)
	ini_date_process4		= models.DateTimeField(null=True, blank=True)
	finish_date_process1	= models.DateTimeField(null=True, blank=True)
	finish_date_process2	= models.DateTimeField(null=True, blank=True)
	finish_date_process3	= models.DateTimeField(null=True, blank=True)
	finish_date_process4	= models.DateTimeField(null=True, blank=True)
	
	def __str__(self):
		return self.number
		
