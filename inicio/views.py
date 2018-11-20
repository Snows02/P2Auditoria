from django.shortcuts import render,redirect

def login_view(request):
    return render(request, 'inicio/login.html')

def proyect_view(request):
    return render(request, 'inicio/index.html')

def graphics(request):
    return render(request, 'inicio/graficas.html')

def rgrafi(request):
	return redirect('grafica')
