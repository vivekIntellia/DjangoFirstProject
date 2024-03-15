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
                    return redirect('rejected')
                
                if request.method == 'POST' and 'signup_after_rejection' in request.POST:
                    user_detail.status = 'Pending'
                    user_detail.save()
                    return redirect('signup')
                else:
                    response = get_response(request)
                    return response

            elif user_detail.status == 'Approved':
                return redirect('login')  

        response = get_response(request)
        return response

    return middleware
