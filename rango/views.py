from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    context_dict = {'boldmessage' : 'Dolore consectetur deserunt duis culpa.'}

    return render(request, 'rango/index.html' , context=context_dict)

def about(request):
    return HttpResponse("This is about page")