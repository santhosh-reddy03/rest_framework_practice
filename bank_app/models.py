from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UserStore(models.Model):
	"""docstring for UserStore"""
	
	username = models.OneToOneField(User, on_delete=models.CASCADE)
	ACCOUNT_TYPE_CHOICE = [('C', 'Cashier'), ('E', 'Executive')]
	account_type = models.CharField(max_length=1, choices=ACCOUNT_TYPE_CHOICE, default='C')

	class Meta:
		"""docstring for Meta"""
		db_table = 'userstore2'


class Customer(models.Model):
	customer_id = models.IntegerField(primary_key=True)
	customer_ssn_id = models.IntegerField()
	customer_name = models.CharField(max_length=100)
	age = models.IntegerField()
	address_line1 = models.TextField()
	address_line2 = models.TextField()
	city = models.CharField(max_length=100)
	state = models.CharField(max_length=100)
	

class CustomerStatus(models.Model):
	customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
	customer_ssn_id = models.IntegerField()
	status = models.CharField(max_length=20)
	message = models.TextField()
	last_updated = models.DateTimeField(auto_now=True)


class Account(models.Model):
	customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
	account_id = models.IntegerField()
	ACCOUNT_TYPE_CHOICE = [('C', 'Current'), ('S', 'Savings')]
	account_type = models.CharField(max_length=1, choices=ACCOUNT_TYPE_CHOICE, default='S')
	amount = models.IntegerField()
	amount_credit_debit = models.CharField(max_length=10)
	status = models.CharField(max_length=20)
	message = models.TextField()
	last_updated = models.DateTimeField(auto_now=True)
