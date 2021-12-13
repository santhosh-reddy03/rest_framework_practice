from django.contrib.auth.backends import BaseBackend


# return user object if the creds are valid else return none
class UserBackend(BaseBackend):

	def authenticate(self, request, username=None, password=None):
		pass

	def get_user(self):
		pass

