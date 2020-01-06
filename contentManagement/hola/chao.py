from django.http import HttpResponse

def chao(request):
	return HttpResponse("chao")

def principal(request):
	return HttpResponse("<h1 style='color:red;'>esto es un simulacro</h1>")
