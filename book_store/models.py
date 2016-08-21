from django.db import models
from django.utils import timezone
import json
#from django.contrib.postgres.fields import ArrayField

def add_object_to_jsonlist(obj, jsonlist):
	jsonDec = json.JSONDecoder()
	list = jsonDec.decode(jsonlist)
	list.append(obj)
	jsonlist = json.dumps(list)
	return jsonlist

class Receipt(models.Model):
	
	book_name = models.CharField(max_length=70)
	person_name = models.CharField(max_length=50)
	price = models.FloatField()
	date = models.DateTimeField(default=timezone.now)

	def __init__(self, book_name, person_name, price):
		self.book_name = book_name
		self.person_name = person_name
		self.price = price

	def __str__(self):
		return ("book_name = "+ self.book_name + ", person_name = "+ self.person_name)

class BookName(models.Model):
	name = models.CharField(max_length=30, default="???")


#Test models inheritance
class Base(models.Model):
	num = models.IntegerField(default=0)
	password = models.CharField(max_length=10, default="0")

	def base_func(self):
		print("num = " +str(self.num))

class Derived(Base):
	name = models.CharField(max_length=40)
	unique_name = models.IntegerField(primary_key=True)

	def derived_func(self):
		print("name = " + self.name)
		self.base_func()
		
#End of test models inheritance
		
class Book(models.Model):

	BOOK_CATEGORY = (
		('History', 'History'),
		('Drama', 'Drama'),
		('Fantazi', 'Fantazi'),
		('None', 'None')
	)

	name = models.CharField(max_length=70)
	author = models.CharField(max_length=50)
	price = models.FloatField()
	created_date = models.DateTimeField(default=timezone.now)
	data = models.TextField(default="[b1, b2]", null=False)
	#num_of_pages = models.IntegerField(default=100)
	category = models.CharField(max_length=10, choices=BOOK_CATEGORY, default='None')

	def add_book(self, name):
		jsonDec = json.JSONDecoder()
		try:
			list = jsonDec.decode(self.data)
		#If it is the first time that we add book
		except ValueError:
			list = []
			self.data = json.dumps(list)
			list = jsonDec.decode(self.data)
		list.append(name)
		self.data = json.dumps(list)
		self.save()


	def buy(self, person_name):
		receipt = Receipt(self.name, person_name, self.price)
		#receipt.save()

	def add_name(self, name):
		self.data = add_object_to_jsonlist(name, self.data)
		self.save()

	def get_data(self):
		jsonDec = json.JSONDecoder()
		list = jsonDec.decode(self.data)
		return list

	def __str__(self):
		return ("book name = "+ self.name)
