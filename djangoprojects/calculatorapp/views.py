from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
# Create your views here.

def index(request):
    #return HttpResponse("calculater app server started")
    return render(request, 'index.html')

def submitquery(request):
    q = request.GET['query']
    #return HttpResponse(q)
    try:
        ans = eval(q)
        mydictionary={
            "q":q,
            "ans":ans,
            "error":False,
            "result":True
        }
        return render(request, 'index.html', context=mydictionary)
    except:
        mydictionary={
            "error": True,
            "result":False
        }
        return render(request, 'index.html', context=mydictionary)

    #jsonedic={
    #    "q":q
    #}
    #return JsonResponse(jsonedic)