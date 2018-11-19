from django.shortcuts import render,redirect


def inicio(request):
    return render(request, 'inicio/login.html')

def inde(request):
    return render(request, 'inicio/index.html')

def grafica(request):
    return render(request, 'inicio/graficas.html')

def rgrafi(request):
	return redirect('grafica')