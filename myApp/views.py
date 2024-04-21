from django.http import HttpResponse
# from django.template import Template, Context
from django.shortcuts import render

# def home(request):
#     with open('path/to/your/home.html', 'r') as template_file:
#         template = Template(template_file.read())
#     context = {}  # Add your context data here if needed
#     return HttpResponse(template.render(context, request))

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def explore(request):
    return render(request, 'explore.html')
