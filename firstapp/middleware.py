from django.http import HttpResponseForbidden
from firstapp.models import UserDetail
from django.shortcuts import redirect , render

def RequestApprovalMiddleware(get_response):
    def middleware(request):
        current_path = request.path

        user_details = UserDetail.objects.all()

        for user_detail in user_details:
            if user_detail.status == 'Rejected':
                if current_path != '/rejected/':
                    print("Redirecting to rejected page") 
                    return redirect('rejected')
                
                if request.method == 'POST' and 'signup_after_rejection' in request.POST:
                    user_detail.status = 'Pending'
                    user_detail.save()
                    print("Redirecting to signup page")
                    return redirect('signup')
                else:
                    response = get_response(request)
                    return response

            elif user_detail.status == 'Approved':
                print("Redirecting to login page")
                return redirect('login')  

        response = get_response(request)
        return response

    return middleware
