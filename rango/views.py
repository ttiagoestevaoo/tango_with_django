from django.shortcuts import render
from django.http import HttpResponse
from .models.Category import Category
from .models.Page import Page

# Create your views here.
def index(request):
    category_list = Category.objects.order_by('-likes')[:5]
    context_dict = {'boldmessage' : 'Dolore consectetur deserunt duis culpa.','category_list' : category_list}

    return render(request, 'rango/index.html' , context=context_dict)

def about(request):
    return HttpResponse("This is about page")

def show_category(request, category_name_slug):
    context_dict = {}

    try:
        category = Category.objects.get(slug = category_name_slug)

        pages = Page.objects.filter(category = category)

        context_dict['pages'] = pages

        context_dict['category'] = category
    except Category.DoesNotExist:
        context_dict['pages'] = None   
        context_dict['category'] = None

    return render(request, 'rango/category.html', context=context_dict)