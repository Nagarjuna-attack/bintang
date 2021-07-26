from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Fitur
from django.contrib.auth.models import User, auth
from django.contrib import messages

# Create your views here.
def index(request):
	fiturs = Fitur.objects.all()
	return render(request,'index.html',{'fiturs':fiturs})

#method for register new user
def register(request):
	if request.method == 'POST':
		username = request.POST['username']
		email = request.POST['email']
		password = request.POST['password']
		password2 = request.POST['password2']
		if password == password2:
			if User.objects.filter(email=email).exists():
				messages.info(request,'Email Already Exists')
				return redirect('register')
			elif User.objects.filter(username=username).exists():
				messages.info(request,'Username Already Exists')
				return redirect('register')
			else:
				user = User.objects.create_user(username=username,email=email,password=password)
				user.save()
				return redirect('login')
		else:
			messages.info(request,'The Password Must Be Similar')
			return redirect('register')
	else:
		return render(request,'user/register.html')


def login(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']

		user = auth.authenticate(username=username,password=password)
		if user is not None:
			auth.login(request,user)
			return redirect('/')
		else:
			messages.info(request,'Data tidak valid')
			return redirect('login')
	else:
		return render(request,'user/login.html')

def counter(request):
	text = request.POST['text']
	counter_kata = len(text.split())
	return render(request,'counter.html',{'jum_kata':counter_kata})