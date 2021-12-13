from rest_framework import serializers
from django.contrib.auth.models import User
from bank_app.models import Account, Customer, CustomerStatus, UserStore


class CustomerSerializer(serializers.ModelSerializer):

	class Meta:
		model = Customer
		fields = '__all__'


class AccountSeralizer(serializers.ModelSerializer):

	class Meta:
		model = Account
		fields = '__all__'


class CustomerStatusSerialzer(serializers.ModelSerializer):

	class Meta:
		model = CustomerStatus
		fields = '__all__'


class UserSerializer(serializers.ModelSerializer):

	class Meta:
		model = User
		fields = ['username']


class UserstoreSerializer(serializers.ModelSerializer):
	"""docstring for UserSerializer"""
	username = UserSerializer(read_only=True, default=serializers.CurrentUserDefault())

	class Meta:
		model = UserStore
		fields = ('username', 'account_type')


# from .models import RegisterUser


# class RegisterSerializer(serializers.ModelSerializer):
# 	class Meta:
# 		model = RegisterUser
# 		fields = '__all__'

# 	def create(self, validated_data):
# 		user = super().create(validated_data)
# 		# user.set_password(validated_data['password'])
# 		user.save()
# 		return user


# class SigninSerializer(serializers.ModelSerializer):
# 	class Meta:
# 		model = RegisterUser
# 		fields = ['user_email', 'password']
