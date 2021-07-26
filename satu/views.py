from django.shortcuts import render

# Create your views here.
def index(request):
	context = {
		'nama':'Amigo',
		'umur':25,
	}

	return render(request,'index.html',context)