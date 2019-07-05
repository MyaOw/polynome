from django.shortcuts import render

def index(request):	
	if request.method == 'GET':
		a = 0
		b = 0
		c = 0
		x = 0
		t = 0
	elif request.method == 'POST':
		a = float(request.POST.get("a", False))
		b = float(request.POST.get("b", False))
		c = float(request.POST.get("c", False))
		x = float(request.POST.get("x", False))
		t = a * x ** 2 + (b * x) + c

	context = { 'title': 'ax² + bx +c', 'a': str(a), 'b': str(b), 'c': str(c), 'x': str(x), 't': str(t)}
	return render(request, 'polynome/index.html', context)

