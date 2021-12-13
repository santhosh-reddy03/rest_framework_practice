from bank_app.forms import CustomerCreationForm
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views import View
from django.utils.decorators import method_decorator
# Create your views here.

@login_required(login_url='/login/')
def home(request):
	if request.user.is_authenticated:
		form = CustomerCreationForm()
		return render(request,'bank_app/home.html', {'form':form})
	else:
		redirect('/login/')

def login_view(request):
	if request.method == "POST":
		print("reached login")
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			return redirect('home')
		else:
			messages.error(request, 'authentication failure please check your username and password', fail_silently=True)
			return render(request, 'bank_app/login.html')
	else:
		return render(request, 'bank_app/login.html')

@login_required
def logout_view(request):
	logout(request)
	return redirect('login')


class AppHome(View):
	form_class = CustomerCreationForm
	initial = {'key': 'value'}
	template_name = 'home.html'

	@method_decorator(login_required)
	def get(self, request, *args, **kwargs):
		form = self.form_class(initial=self.initial)
		return render(request, self.template_name, {'form': form})
