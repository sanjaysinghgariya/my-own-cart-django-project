from django.db import models
from datetime import datetime
# Create your models here.
class makeblog(models.Model):
	post_id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=50)
	title = models.CharField(max_length=50, default='')
	heading0 = models.CharField(max_length=50)
	cheading0 = models.CharField(max_length=5000)
	heading1 = models.CharField(max_length=50)
	cheading1 = models.CharField(max_length=5000)
	sub_heading = models.CharField(max_length=50)
	csub_heading = models.CharField(max_length=5000)
	image = models.ImageField(upload_to="blog2/images", default="")
	pub_date = models.DateField(default=datetime.now)

	def __str__(self):
			return self.title