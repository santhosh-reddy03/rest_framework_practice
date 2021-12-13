from django.db import models
from django.contrib.auth.models import User
# Create your models here.


# class UserStore(models.Model):
# 	"""docstring for UserStore"""
	
# 	username = models.OneToOneField(User, on_delete=models.CASCADE)
# 	ACCOUNT_TYPE_CHOICE = [('C', 'Cashier'), ('T', 'Teller')]
# 	account_type = models.CharField(max_length=1, choices=ACCOUNT_TYPE_CHOICE, default='C')

# 	class Meta:
# 		"""docstring for Meta"""
# 		db_table = 'userstore'


# from django.db import models
# from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, UserManager


# class RegisterUser(AbstractBaseUser):
# 	id = models.AutoField(primary_key=True)
# 	user_name = models.CharField(max_length=255, null=False)
# 	user_email = models.EmailField(unique=True)
# 	password = models.CharField(max_length=30, null=False)
# 	user_dob = models.DateField(null=False)
# 	location = models.CharField(max_length=255, null=False)
# 	user_mobile = models.CharField(max_length=10, null=False)

# 	USERNAME_FIELD = 'user_email'
# 	REQUIRED_FIELDS = []
	
# 	objects = UserManager()
	
# 	def __str__(self):
# 		return self.user_email
	