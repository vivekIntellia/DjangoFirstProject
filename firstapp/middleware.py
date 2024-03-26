from django.http import HttpResponseForbidden
from firstapp.models import UserDetail , SignUp
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


def ProfileRequestApprovalMiddleware(get_response):
    def middleware(request):
        current_path = request.path

        signup_objs = SignUp.objects.all()

        for signup_obj in signup_objs:
            if signup_obj.status == 'Rejected':
                if current_path != '/profileRejected/':
                    return redirect('profileRejected')
                
                if request.method == 'POST' and 'signup_after_rejection' in request.POST:
                    signup_obj.status = 'Pending'
                    signup_obj.save()
                    return redirect('signup')
                else:
                    response = get_response(request)
                    return response

            # elif current_path != '/CompleteProfile/' or current_path != '/profileApproval/':
            #         return redirect('CompleteProfile') 
            
            elif signup_obj.status == 'Approved':
                return redirect('signup')  

        response = get_response(request)
        return response

    return middleware

# def ProfileRequestApprovalMiddleware(get_response):
#     def middleware(request):
#         current_path = request.path

#         signup_objs = SignUp.objects.all()

#         for signup_obj in signup_objs:
#             if signup_obj.status == 'Rejected':
#                 if current_path != '/rejected/':
#                     return redirect('rejected')
                
#                 if request.method == 'POST' and 'signup_after_rejection' in request.POST:
#                     signup_obj.status = 'Pending'
#                     signup_obj.save()
#                     return redirect('signup')
#                 else:
#                     response = get_response(request)
#                     return response
            
#             elif signup_obj.status == 'Approved':
#                 return redirect('signup')
        
#         # Count the filled fields
#         filled_fields_count = sum(
#             1 for field in [
#                 signup_obj.fname,
#                 signup_obj.lname,
#                 signup_obj.user.username,
#                 signup_obj.gender,
#                 signup_obj.user.email,
#                 signup_obj.phone,
#                 signup_obj.address,
#                 signup_obj.zip_code,
#                 signup_obj.city,
#                 signup_obj.state,
#                 signup_obj.country,
#                 signup_obj.description,
#             ] if field
#         )

#         # If less than 10 fields were filled, allow access to 'CompleteProfile' and 'profileApproval'
#         if filled_fields_count < 10:
#             if current_path in ('/CompleteProfile/'):
#                 print('Error in the page')
#                 response = get_response(request)
#                 return response
#             else:
#                 return redirect('CompleteProfile')

#         # Otherwise, block access to all other pages
#         else:
#             return redirect('CompleteProfile')

#     return middleware

# def ProfileRequestApprovalMiddleware(get_response):
#     def middleware(request):
#         current_path = request.path

#         signup_objs = SignUp.objects.all()

#         for signup_obj in signup_objs:
#             if signup_obj.status == 'Rejected':
#                 if current_path != '/rejected/':
#                     return redirect('rejected')
                
#                 if request.method == 'POST' and 'signup_after_rejection' in request.POST:
#                     signup_obj.status = 'Pending'
#                     signup_obj.save()
#                     return redirect('signup')
#                 else:
#                     response = get_response(request)
#                     return response
            
#             elif signup_obj.status == 'Approved':
#                 return redirect('signup')  

#         # If no SignUp object found or all SignUp objects are neither rejected nor approved, redirect to 'CompleteProfile'
#         return render(request , 'CompleteProfile.html')

#     return middleware