from django.http import HttpResponse

def index(request,name):
    return HttpResponse(f"Hello {name.capitalize()}, Tanisha here...")