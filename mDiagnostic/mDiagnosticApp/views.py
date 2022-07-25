from django.shortcuts import render

# Create your views here.
def mDiagnosticApp(request):
    return render(request, template_name='index.html')