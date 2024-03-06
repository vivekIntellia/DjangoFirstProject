import csv
import io
from PIL import Image
import xlsxwriter
from django.shortcuts import render , HttpResponse , redirect 
from django.urls import reverse
from django.http import HttpResponseRedirect
from services.models import Services 
from django.contrib.auth.models import User
from django.contrib.auth import authenticate , login , logout
from django.contrib.auth.decorators import login_required
from django.template.loader import get_template
from xhtml2pdf import pisa


@login_required(login_url='login')

def HomePage(request):
    return render(request, 'home.html')

def SignupPage(request):
    error = False
    error1 = False

    if request.method == 'POST':
        uname = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')

        print(uname, email, pass1, pass2)

        if len(pass1) >= 8 and len(pass1) <= 16 and len(pass2) >= 8 and len(pass2) <= 16:
            has_valid_length = True
        else:
            has_valid_length = False

        has_lower_char = any(char.islower() for char in pass1) and any(char.islower() for char in pass2)
        has_upper_char = any(char.isupper() for char in pass1) and any(char.isupper() for char in pass2)
        has_digit = any(char.isdigit() for char in pass1) and any(char.isdigit() for char in pass2)
        has_special_char = any(char in '@#$^&*' for char in pass1) and any(char in '@#$^&*' for char in pass2)

        if not (has_valid_length and has_lower_char and has_upper_char and has_digit and has_special_char):
            error = True  

        if pass1 == pass2 and not error:
            try:
                my_user = User.objects.create_user(username=uname, email=email, password=pass1)
                my_user.save()
                return redirect('uploadimage')
            except Exception as e:
                print('error message', e)
        else:
            error = True

    return render(request, 'signup.html', {'error': error, 'error1': error1})


    
def LoginPage(request):
    error2 = False
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            return redirect("home")
        else:
            error2 = True
            return render(request, 'login.html', {'error2': error2})

    return render (request,'login.html')

def LogoutPage(request):
    if request.method == 'POST':
        logout(request)
        return redirect('login')
    return render(request, 'logout.html')

def services(request):
    servicedata = Services.objects.all()
    default_icon_class = 'fas fa-question-circle'
    icon_classes = [
        'fas fa-laptop-code', 
        'fab fa-battle-net',   
        'fab fa-artstation',   
        'fab fa-500px',        
        'fas fa-chart-pie',    
        'fab fa-asymmetrik',
        "fas fa-car",
        ''
    ]

    if len(icon_classes) < len(servicedata):
        icon_classes += [default_icon_class] * (len(servicedata) - len(icon_classes))
    elif len(icon_classes) > len(servicedata):
        icon_classes = icon_classes[:len(servicedata)]

    services_with_icons = list(zip(servicedata, icon_classes))

    data = {
           'services_with_icons' : services_with_icons 
    }
    return render( request , 'services.html' , data)

def generate_pdf(request, service_id):
    service = Services.objects.get(id=service_id)
    template_path = 'services_pdf.html'
    context = {'service': service}
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="service_{service_id}.pdf"'
    template = get_template(template_path)
    html = template.render(context)
    pisa_status = pisa.CreatePDF(html, dest=response)
    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response

# USE THIS CODE TO DOWNLOAD ALL SERVICES PDF IN A SINGLE PDF FILE 
# UPDATE THE URL WITH THIS <a href="{% url 'generate_pdf'%}" class="learn-more">Download PDF</a>
# ALSO UPDATE THE PATH WITH THIS path('generate-pdf', views.generate_pdf, name='generate_pdf'),
# def generate_pdf(request):
#     services = Services.objects.all()
#     template_path = 'services_pdf.html'
#     context = {'services': services}
#     template = get_template(template_path)
#     html = template.render(context)
#     response = HttpResponse(content_type='application/pdf')
#     response['Content-Disposition'] = 'attachment; filename="services_pdf.pdf"'
#     pisa_status = pisa.CreatePDF(html, dest=response)
#     if pisa_status.err:
#         return HttpResponse('PDF generation error', status=500)

#     return response

### TO DOWNLOAD ALL SERVICES DATA IN SINGLE FILE [USE THIS IN THE SERVCIE. HRML FILE <a href="{% url 'download_csv' %}" class="learn-more">Download CSV</a>#####
# def download_csv(request):
#     response = HttpResponse(content_type='text/csv')
#     response['Content-Disposition'] = 'attachment; filename="services.csv"'
#     writer = csv.writer(response)
#     writer.writerow(['Service Title', 'Description', 'Link'])
#     services = Services.objects.all()
#     for service in services:
#         writer.writerow([service.service_icon, service.service_des, service.service_title])

#     return response

def download_csv(request, service_id):
    try:
        service = Services.objects.get(id=service_id)
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = f'attachment; filename="service_{service_id}.csv"'
        
        writer = csv.writer(response)
        writer.writerow(['Service Title', 'Description', 'Icon'])
        writer.writerow([service.service_title, service.service_des, service.service_icon])

        return response
    except Services.DoesNotExist:
        return HttpResponse("Service not found", status=404)
    

# USE THIS CODE TO GENERATE ALL THE SERVICES IN EXCEL FILE <a href="{% url 'generate_excel' %}" class="learn-more">Download EXCEL</a> USE THIS URL AND USE THIS PATH path('generate-excel/', views.generate_excel, name='generate_excel'),
# def generate_excel(request , service_id):
#     services = Services.objects.gte(id=service_id)
#     output = io.BytesIO()
#     workbook = xlsxwriter.Workbook(output)
#     worksheet = workbook.add_worksheet()
#     headers = ['Service Title', 'Description', 'Icon']
#     for col, header in enumerate(headers):
#         worksheet.write(0, col, header)
#     for row, service in enumerate(services, start=1):
#         worksheet.write(row, 0, service.service_title)
#         worksheet.write(row, 1, service.service_des)
#         worksheet.write(row, 2, service.service_icon)
#     workbook.close()
#     response = HttpResponse(output.getvalue(), content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
#     response['Content-Disposition'] = 'attachment; filename="services_report.xlsx"'

#     return response


def generate_excel(request, service_id):
    try:
        service = Services.objects.get(id=service_id)
    except Services.DoesNotExist:
        return HttpResponse('Service not found', status=404)
    output = io.BytesIO()
    workbook = xlsxwriter.Workbook(output)
    worksheet = workbook.add_worksheet()
    headers = ['Service Title', 'Description', 'Icon']
    for col, header in enumerate(headers):
        worksheet.write(0, col, header)
    worksheet.write(1, 0, service.service_title)
    worksheet.write(1, 1, service.service_des)
    worksheet.write(1, 2, service.service_icon)
    workbook.close()
    response = HttpResponse(output.getvalue(), content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = f'attachment; filename="service_{service_id}_report.xlsx"'

    return response

def thankyou(request):
    return render( request , 'thankyou.html')

def form(request):
    try:
        name = request.GET['name']
        signupemail = request.GET['signupemail']
        signuppassword = request.GET['signuppassword']
        confirmpassword = request.GET['signuppassword']
        request.save()
        print(name,signupemail,signuppassword,confirmpassword)
    except:
        pass
    return render( request , 'form.html')

def calculator(request):
    data = {}
    try:
        if request.method == "POST":
            if request.POST.get('num1') == "":
                return render( request , 'calculator.html' , {'error' : True})
            n1 = eval(request.POST.get('num1'))
            # n2 = int(request.POST.get('num2'))
            # result = request.POST.get('opr')
            # for op in request.POST.get('opr'):
            #     if op == '+':
            #         cal = n1+n2
            #     if op == '-':
            #         cal = n1-n2
            #     if op == '*':
            #         cal = n1*n2
            #     if op == '/':
            #         cal = n1/n2
            if n1 % 2 == 0 and n1 != 1:
                cal = 'Even'
            else:
                cal = 'Odd'
            data = {
                'result' : cal
            }
            # print(cal)
    except:
        cal = 'Invalid opr......'
    # print(cal)
    return render( request , 'calculator.html' , data)

# def UserForm(request):
#     fn = UserForms()
#     finalans = 0
#     data = {}
#     try:
#         if request.method=='post':
#             n1 = int(request.POST['num1'])
#             n2 = int(request.POST['num2'])
#             finalans = n1+n2
#             data = {
#                 'control' : fn,
#                 'output': finalans
#             }
#             url = "/about/?output={}".format(finalans)

#             return redirect(url)
#     except:
#         pass

#     return render(request,'UserForms.html',data)
# Create your views here.



