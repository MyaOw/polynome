from django.shortcuts import render
from math import sqrt
from polynome.models import Model

def index(request):
	context = { 'title': 'ax² + bx +c',}
	if request.method == 'GET':
		a = 0.0
		b = 0.0
		c = 0.0
		x = 0.0
	elif request.method == 'POST':
		a = request.POST['a']
		b = request.POST['b']
		c = request.POST['c']
		x = request.POST['x']
		t = a*x**2+(b*x)+c

	return render(request, 'polynome/index.html', context)