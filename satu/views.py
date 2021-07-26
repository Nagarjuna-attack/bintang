from django.shortcuts import render

# Create your views here.
def index(request):
	context = {
		'nama':'Amigo',
		'umur':25,
	}

	return render(request,'index.html',context)

def counter(request):
	text = request.POST['text']
	counter_kata = len(text.split())
	return render(request,'counter.html',{'jum_kata':counter_kata})