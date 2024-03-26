import csv
import io
import xlsxwriter
from django.shortcuts import render , HttpResponse , redirect ,get_object_or_404
from django.urls import reverse
from django.http import HttpResponseRedirect
from services.models import Services 
from .models import Profile_picture , UserDetail , UserProfile 
from django.contrib.auth.models import User
from django.contrib.auth import authenticate , login , logout
from django.contrib.auth.decorators import login_required
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.core.mail import send_mail
from .models import UserResponse
import random
import uuid
from django.conf import settings
from django.contrib import messages
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from . helper import send_otp_to_phone
from .form import UserProfileForm
from django.contrib import messages
from .forms import EducationForm
from .models import Education
from django.views import View
from django.core.exceptions import ValidationError
from .forms import ReviewEducationForm



@login_required(login_url='login')

def HomePage(request):
    user = request.user
    try:
        profile_picture = Profile_picture.objects.get(user=user)
        context = {'profile_picture': profile_picture}
    except Profile_picture.DoesNotExist:
        context = {'no_profile_picture': True}
    return render(request, 'home.html', context)


def SignupPage(request):
    error = False
    error1 = False
    if request.method == 'POST':
        uname = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')
        request.session['signup_email'] = email
        request.session['username'] = uname

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
                verification_token = str(uuid.uuid4())
                profile_obj = UserProfile.objects.create(user=my_user, verification_token=verification_token)
                send_mail_after_registration(email, verification_token)
                profile_obj.save()
                print('Redirecting to token_send')
                return redirect('token_send')
            except Exception as e:
                print('error message', e)
                error = True
                return redirect('token_send')
            
            except Exception as e:
                print('error message', e)
                error = True
            return redirect('userdetails')
        elif pass1 != pass2:
            error1 = True
        else:
            error = True

    return render(request, 'signup.html', {'error': error, 'error1': error1})

def success(request):
    return render(request,'success.html')
def error_page(request):
    return render(request,'error.html')

def token_send(request):
    return render(request,'token_send.html')

def send_mail_after_registration(email, token):
    subject = "Your account has been verified"
    message = f"Hi, please click the following link to verify your account: http://127.0.0.1:8000/verify/{token}"
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail(subject, message, email_from, recipient_list)
    
def verify(request, verification_token):
    try:
        profile_obj = UserProfile.objects.filter(verification_token=verification_token).first()
        if profile_obj:
            profile_obj.email_verified = True
            profile_obj.save()
            messages.success(request, 'Your account has been verified')
            # Redirect to 'userdetails' instead of 'error'
            return redirect(reverse('userdetails'))
        else:
            messages.error(request, 'Invalid verification token')
            return render(request, 'error.html')
    except Exception as e:
        print(e)
        messages.error(request, 'An error occurred during verification')
        return render(request, 'error.html')

def success(request):
    return render(request,'success.html')
def error_page(request):
    return render(request,'error.html')

def token_send(request):
    return render(request,'token_send.html')

def send_mail_after_registration(email, token):
    subject = "Your account has been verified"
    message = f"Hi, please click the following link to verify your account: http://127.0.0.1:8000/verify/{token}"
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail(subject, message, email_from, recipient_list)

def verify(request, verification_token):
    try:
        profile_obj = UserProfile.objects.filter(verification_token=verification_token).first()
        if profile_obj:
            profile_obj.email_verified = True
            profile_obj.save()
            messages.success(request, 'Your account has been verified')
            return redirect(reverse('login'))
        else:
            messages.error(request, 'Invalid verification token')
            return render(request, 'error.html')
    except Exception as e:
        print(e)
        messages.error(request, 'An error occurred during verification')
        return render(request, 'error.html')

def UserDetails(request):
    user_detail = None
    if request.method == 'POST':
        sport = request.POST.get('sport')
        school_experience = request.POST.get('school')
        state_experience = request.POST.get('state')
        national_experience = request.POST.get('national')
        international_experience = request.POST.get('international')
        username = request.session.get('username')

        user = User.objects.get(username=username)

        user_detail = UserDetail.objects.create(
            user = user,
            sport = sport,
            school_experience = school_experience,
            state_experience = state_experience,
            national_experience = national_experience,
            international_experience = international_experience
        )

        sport_label = user_detail.get_sport_label()
        user_detail.sport = sport_label
        user_detail.save() 

        request.session['user_detail_id'] = user_detail.id

        return redirect('approvalrequest')
    return render(request , 'userdetails.html'  , {'user_detail': user_detail})

def adminApproval(request):
    if request.method == 'POST':
        user_detail_id = request.POST.get('user_detail_id')
        note = request.POST.get('note') 
        if user_detail_id and note:
            user_detail = UserDetail.objects.get(id=user_detail_id)
            user_detail.note = note 
            user_detail.save()
            return redirect('adminApproval') 
        else:
            return HttpResponse('User detail ID and note are required')


def ApprovalRequest(request):
    email = request.session.get('signup_email')
    username = request.session.get('username')
    if request.method == 'GET':
        send_mail(
        'Confirmation mail',
        'This is the confirmation mail that you have received.Thank You for filing the form , we appreciate your interest in joning us for now just wait for the administration to approve your request. We will get to you soon ',
        settings.EMAIL_HOST_USER,
        [email],
        )

        admin_email = 'vivekyadav2750@gmail.com'
        user_details_page_url = request.build_absolute_uri(reverse('adminApproval'))
        send_mail(
            'New Approval Request',
            f'A new approval request has been submitted by {username} having email {email}, Please review it at: {user_details_page_url}.',
            settings.EMAIL_HOST_USER,
            [admin_email],
    )

    return render(request , 'approvalrequest.html')

def send_acceptance_email(request, user_detail_id):
    user_detail = UserDetail.objects.get(pk=user_detail_id)
    user_detail.status = 'Approved'
    user_detail.save()

    email = user_detail.user.email
    login_page_url = request.build_absolute_uri(reverse('login'))
    send_mail(
        'Update on Your request',
        f'Your request has been accepted use this link to login to the website to access the services {login_page_url}',
        settings.EMAIL_HOST_USER,
        [email],
        fail_silently=False,
    )
    return JsonResponse({'message': 'Acceptance email sent'})

def send_rejection_email(request, user_detail_id):
    user_detail = UserDetail.objects.get(pk=user_detail_id)
    user_detail.status = 'Rejected'
    user_detail.save()

    email = user_detail.user.email
    send_mail(
        'Update on Your request',
        f'We appreciate your interest in joining our organisation, but unfortunately your details does not match our requirement. You can reapply after 3 months.',
        settings.EMAIL_HOST_USER,
        [email],
        fail_silently=False,
    )
    return JsonResponse({'message': 'Rejection email sent'})

def rejected(request):
    user_detail_id = request.session.get('user_detail_id')
    if user_detail_id:
        user_detail = UserDetail.objects.get(id=user_detail_id)
        note = user_detail.note  
    else:
        user_detail = None
        note = None
    return render(request, 'rejected.html', {'note': note})

@login_required(login_url='login')
def LoginPage(request):
    error2 = False
    verification_message = None

    if request.method == 'POST':
        username = request.POST.get('username')
        pass1 = request.POST.get('pass')
        user = authenticate(request, username=username, password=pass1)

        if user is not None:
            try:
                profile_obj = UserProfile.objects.get(user=user)
                if profile_obj.email_verified:
                    login(request, user)
                    return redirect("home")
                else:
                    verification_message = 'Please verify your email before logging in.'
            except UserProfile.DoesNotExist:
                messages.error(request, 'User profile not found.')
                return render(request, 'login.html', {'error2': error2, 'verification_message': verification_message})

        else:
            error2 = True
            return render(request, 'login.html', {'error2': error2, 'verification_message': verification_message})

    return render(request, 'login.html', {'verification_message': verification_message})

def LogoutPage(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def services(request):
    servicedata = Services.objects.all()
    default_icon_class = 'fas fa-question-circle'
    icon_classes = [
        'fas fa-futbol', 
        'fas fa-table-tennis',   
        'fas fa-volleyball-ball',   
        'fas fa-chess-queen',        
        'fas fa-basketball-ball',    
        'fas fa-skating',
        # ''
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
    


def generate_excel(service_id):
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



def upload_profile_image(request):
    user = request.user
    try:
        # Attempt to retrieve the user's existing profile picture
        profile_picture = Profile_picture.objects.get(user=user)
    except Profile_picture.DoesNotExist:
        profile_picture = None

    if request.method == 'POST':
        # If the form is submitted via POST, process the form data
        form = UserProfileForm(request.POST, request.FILES, instance=profile_picture)
        if form.is_valid():
            # Save the form data to the database
            profile_picture = form.save(commit=False)
            profile_picture.user = user
            profile_picture.save()
            # Redirect to the home page or any other desired page after successful upload
            return redirect('home')
    else:
        # If the request method is GET, initialize the form with existing profile picture data if available
        form = UserProfileForm(instance=profile_picture)

    # Render the upload_profile_image.html template with the form
    return render(request, 'upload_profile_image.html', {'form': form})


def display_services(request):
    servicedata = Services.objects.all()
    return render(request, 'services_table.html', {'servicedata': servicedata})




def chatbot(request):
    return render(request,'chatbot.html')

def save_response(request):
    if request.method == 'POST' and 'userResponse' in request.POST:
        user_response_text = request.POST['userResponse']  # Correct key name
        print("User Response:", user_response_text)  # Debugging: Print user response to console
        # Save the user response in the database
        user_response = UserResponse.objects.create(response_text=user_response_text)  # Correct field name
        print("User Response saved:", user_response)  # Debugging: Print saved response object to console
        return JsonResponse({'success': True})
    else:
        return JsonResponse({'error': 'Invalid request method or parameters'})
    
def admin_notification(request):
    return render(request,'admin_notification.html')
    

def education_form_view(request):
    from .flows import EducationFlow 
    if request.method == 'POST':
        form = EducationForm(request.POST)
        if form.is_valid():
            education_instance = form.save(commit=False)
            education_instance.user = request.user
            education_instance.save()

            total_fields = len(form.fields)
            filled_fields = sum(1 for field in form.cleaned_data.values() if field is not None)
            filled_percentage = (filled_fields / total_fields) * 100

            if filled_percentage < 70:
                send_email_to_admin(request, filled_percentage,education_instance)
                messages.warning(request, 'Please fill at least 70% of the details to proceed.')
                return redirect('admin_notification')

            try:
                flow_instance = EducationFlow.start(
                    request=request,
                    user=request.user,
                    process_instance=education_instance
                )
                messages.success(request, 'Education flow started successfully.')
                return redirect('home')
            except Exception as e:
                messages.error(request, f"An error occurred: {str(e)}")
                return redirect('login')

        else:
            messages.error(request, 'Failed to save education details. Please check the form.')
    else:
        form = EducationForm()
    return render(request, 'education_form.html', {'form': form})


def send_email_to_admin(request, filled_percentage, education_instance):
    subject = 'Education Form Alert'
    message = f'Please review the submitted education form. Filled percentage: {filled_percentage}%\n\n'
    message += f'Click the link below to review:\n{request.build_absolute_uri(reverse("make_decision", kwargs={"education_id": education_instance.id}))}'
    from_email = settings.EMAIL_HOST_USER
    to_email = 'ayushijain.jain12345@gmail.com'  # Replace with admin's email address
    send_mail(subject, message, from_email, [to_email])



class MakeDecisionView(View):
    template_name = 'make_decision.html'

    def get(self, request, *args, **kwargs):
        education_id = kwargs.get('education_id')
        education_instance = Education.objects.get(pk=education_id)
        return render(request, self.template_name, {'education_instance': education_instance})

    def post(self, request, *args, **kwargs):
        education_id = kwargs.get('education_id')
        education_instance = Education.objects.get(pk=education_id)

        decision = request.POST.get('decision')
        if decision == 'approve':
            education_instance.approved = True
            send_email_to_user(education_instance.user.email,request, approved=True)
            messages.success(request, 'Education form approved successfully.')
        elif decision == 'reject':
            education_instance.approved = False
            send_email_to_user(education_instance.user.email, request,approved=False)
            messages.success(request, 'Education form rejected successfully.')
        else:
            pass

        education_instance.save()

        return redirect('home')


def send_email_to_user(user_email, request, approved=True):
    subject = 'Education Form Status Update'
    if approved:
        message = 'Your education form has been approved.'
        redirect_link = reverse('home')
    else:
        message = 'Your education form has been rejected. Please sign up again.'
        redirect_link = reverse('signup')

    absolute_redirect_link = request.build_absolute_uri(redirect_link)

    message += f'\n\nClick here to {absolute_redirect_link}'

    from_email = settings.EMAIL_HOST_USER
    # to_email = 'aayushi.jain@intelliatech.com'
    to_email = user_email
    

    send_mail(subject, message, from_email, [to_email])


