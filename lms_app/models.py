from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

# Create your models here.
class Catalogue(models.Model):
	name = models.CharField(max_length=50, blank=False)

	class Meta:
		verbose_name_plural = 'Catalogue'

	def __str__(self):
		return str(self.name)

class Status(models.Model):
	name = models.CharField(max_length=50, blank=False)

	class Meta:
		verbose_name_plural = 'Status'

	def __str__(self):
		return str(self.name)



class Book(models.Model):
	name = models.CharField(max_length=50, blank=False)
	author = models.CharField(max_length=50, blank=True)
	cover_page = models.ImageField(blank=True, upload_to="cover/")
	edition = models.CharField(max_length=50, blank=True)
	isbn = models.CharField(max_length=50, blank=True)
	publisher = models.CharField(max_length=50, blank=True)
	language = models.CharField(max_length=50, blank=True)
	topic = models.CharField(max_length=50, blank=True)
	length = models.CharField(max_length=50, blank=True)
	category = models.ForeignKey(Catalogue, blank=True, on_delete=models.CASCADE)
	book_count = models.IntegerField(default=1)
	book_price = models.IntegerField(default=10)
	status = models.ForeignKey(Status, blank=True, on_delete=models.CASCADE)

	def __str__(self):
		return str(self.name)

class Cart(models.Model):
	owner=models.OneToOneField(User, null=True, on_delete=models.SET_NULL)
	books = models.ManyToManyField(Book, related_name='cart', blank=True)
	total_amount = models.IntegerField(default=0)

	def __str__(self):
		return str(self.owner)


class Profile(models.Model):
	user=models.OneToOneField(User, null=True, on_delete=models.SET_NULL)
	contact = models.CharField(blank=True, max_length=500)
	books_taken = models.ManyToManyField(Book, related_name='book', blank=True)
	book_count = models.IntegerField(default=0)
	books_price = models.IntegerField(default=0)
	checked_out = models.BooleanField(default=False)

	def __str__(self):
		return f'{self.user.username}'

def create_profile(sender, instance, created, **kwargs):
	if created:
		profile = Profile(user=instance)
		profile.save()

post_save.connect(create_profile, sender=User)