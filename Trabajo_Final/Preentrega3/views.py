from django.http import HttpResponse
from django.shortcuts import render

def saludo(request):
	return render(request=request, template_name='app1/base.html')

