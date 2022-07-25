from django.shortcuts import render
from .models import T_Appiontment
# Create your views here.
def mDoctorApp(request):
    if request.method =='POST':
        app_name = request.POST.get('name')
        app_email = request.POST.get('email')
        app_phone = request.POST.get('phone')
        app_date = request.POST.get('date')
        app_dept = request.POST.get('department')
        app_doc = request.POST.get('doctor')
        app_comments= request.POST.get('message')

        if app_name is not None and app_date is not None:
            t_appionment = T_Appiontment(
                app_name=app_name,
                app_email=app_email,
                app_phone=app_phone,
                app_date=app_date,
                app_dept=app_dept,
                app_doc=app_doc,
                app_comments=app_comments
            )    
            t_appionment.save()
            messages.success(request, 'Data Save Successfully')           
    return render(request, template_name='index.html')
