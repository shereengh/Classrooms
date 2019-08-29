from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.db import models
class Classroom(models.Model):
	teacher = models.ForeignKey(User, default=1, on_delete=models.CASCADE)
	name = models.CharField(max_length=120)
	subject = models.CharField(max_length=120)
	year = models.IntegerField()


	def get_absolute_url(self):
		return reverse('classroom-detail', kwargs={'classroom_id':self.id})

class Student(models.Model):
	name = models.CharField(max_length=120)
	date_of_birth = models.DateField()
	FEMALE = 'FE'
	MALE = "ME"
	GENDER = [
	(FEMALE,'female'),
	(MALE, 'male'),
	]
	gender = models.CharField(max_length=2, choices=GENDER, default=FEMALE,)
	exam_grade= models.IntegerField()
	classroom = models.ForeignKey(Classroom, default=1, on_delete=models.CASCADE)
