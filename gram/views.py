from django.http import HttpResponseRedirect
from django.shortcuts import render,redirect
from .forms import UserRegistrationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UpdateUserForm,UpdateUserProfileForm
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

@login_required(login_url='login')
def profile(request,username):
  images = request.user.profile.posts.all()
  if request.method == 'POST':
    user_form = UpdateUserForm(request.POST,instance=request.user)
    prof_form = UpdateUserProfileForm(request.POST, request.FILES, instance=request.user.profile)
    if user_form.is_valid() and prof_form.is_valid():
      user_form.save()
      prof_form.save()
      return HttpResponseRedirect(request.path_info)
    else:
      user_form = UpdateUserForm(instance=request.user)
      prof_form = UpdateUserProfileForm(instance=request.user.profile)
      params = {
        'user_form': user_form,
        'pprof_form': prof_form,
        'images': images,
      }
      return render(request,'gram/profile.html', params)
	