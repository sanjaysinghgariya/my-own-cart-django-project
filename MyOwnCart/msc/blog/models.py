from django.db import models
from datetime import datetime


class blogpost(models.Model):
	post_id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=50)
	heading0 = models.CharField(max_length=50)
	cheading0 = models.CharField(max_length=500)
	heading1 = models.CharField(max_length=50)
	cheading1 = models.CharField(max_length=500)
	sub_heading = models.CharField(max_length=50)
	csub_heading = models.CharField(max_length=500)
	pub_date = models.DateField(datetime.today(), blank=True)
