from django.shortcuts import render
from math import sqrt
from polynome.models import Model

def index(request):
	context = { 'title': 'ax² + bx +c',}

	if request.method == 'POST':
		a = request.POST.get("a", False)
		a = float(a)
		b = request.POST.get("b", False)
		b = float(b)
		c = request.POST.get("c", False)
		c = float(c)
		x = request.POST.get("x", False)
		x = float(x)
		t = a*x**2+(b*x)+c
		print(t)


	return render(request, 'polynome/index.html', context, t)

