from django.shortcuts import render
from .models import Fitur

# Create your views here.
def index(request):
	fiturku = Fitur()
	fiturku.id=1
	fiturku.icon='ri-stack-line'
	fiturku.name='Service'
	fiturku.detail='Merupakan model yang digunakan untuk mendapatkan kekuatan'

	fiturku2 = Fitur()
	fiturku2.id=2
	fiturku2.icon='ri-palette-line'
	fiturku2.name='Paket'
	fiturku2.detail='Pesanan yang akan kami antarkan sebentar lagi, akan meluncur'

	fiturku3 = Fitur()
	fiturku3.id=3
	fiturku3.icon='ri-command-line'
	fiturku3.name='Kontak'
	fiturku3.detail='Anda bisa menghubungi kami dimanapun kalian berada'

	fiturku4 = Fitur()
	fiturku4.id=4
	fiturku4.icon='ri-fingerprint-line'
	fiturku4.name='Tentang'
	fiturku4.detail='Kami Melayani semua jenis jasa pengiriman kurir'

	fiturs = [fiturku,fiturku2,fiturku3,fiturku4]

	return render(request,'index.html',{'fiturs':fiturs})

def counter(request):
	text = request.POST['text']
	counter_kata = len(text.split())
	return render(request,'counter.html',{'jum_kata':counter_kata})