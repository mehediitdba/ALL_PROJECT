from django.shortcuts import render

# Create your views here.
def index(request):
    #return HttpResponse("calculater app server started")
    return render(request, 'index.html')