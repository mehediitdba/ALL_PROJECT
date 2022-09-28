from curses.ascii import US
from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import get_template

# Create your views here.

def page_not_found(request):
    return HttpResponse("<h1>Page Not Found. go to /home_page </h1>")

def home_page1(request):
    my_title = "hello Pytyon"
    #doc="<h1>{title}</h2>".format{title=my_title}
    #django_rendered_doc="<h1>{title}</h2>".format{title=my_title}
    return render(request, 'hello_world1.html', {"title":my_title})

def home_page(request):
    my_title = "hello Pytyon"
    context={"title":my_title}
    template_name = "title.txt"
    template_obj=get_template(template_name)
    rendered_string = template_obj.render(context)
    #doc="<h1>{title}</h2>".format{title=my_title}
    #django_rendered_doc="<h1>{title}</h2>".format{title=my_title}
    return render(request, 'hello_world1.html', {"title":rendered_string})


def home_page2(request):
    my_title = "hello Pytyon.."
    context = {"title":my_title}
    if request.user.is_authenticated:
        context={"title":my_title, "my_list":[1,2,3,4,5]}
    return render(request, 'home.html', context)


#def home_page(request):
#    return HttpResponse("<h1>Hello World</h1>")

def about_page(request):
    return render(request, 'about.html', {"title":"about us"})

def contact_page(request):
    return render(request, 'hello_world.html', {"title":"contact us"})

def page(request):
    return HttpResponse("<h1>page</h1>")

def example_page(request):
    context          =   {"title":"Example"}
    template_name    =    "hello_world.html"
    template_obj =get_template(template_name)
    rendered_item = template_obj.render(context)
    return HttpResponse(rendered_item)
