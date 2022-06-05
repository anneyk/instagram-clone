from django.shortcuts import render,redirect
from .forms import UserRegistrationForm
from django.contrib import messages
# Create your views here.
def index(request):
  return render(request, 'index.html')

def register(request):
	if request.method == "POST":
		form = UserRegistrationForm(request.POST)
		if form.is_valid():
			form.save()
			# user = form.save()
			# login(request, user)
			messages.success(request, f"Registration successful." )
			return redirect("login")
	else:
		form = UserRegistrationForm()

	context = {'form':form}
	return render (request, 'register.html', context)
	