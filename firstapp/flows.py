from viewflow import this
from django.core.mail import send_mail
from django.shortcuts import redirect
from django.urls import reverse
from django.conf import settings
from viewflow.workflow import flow
from . import views


class SignupFlow(flow.Flow):
    start = flow.Start(views.SignupPage).Next(this.task)

    task = flow.If(lambda activation: activation.process.filled_fields_count <= 10).Then(this.redirect_to_complete_profile).Else(this.move_forward)

    move_forward = flow.Handle(this.move_forward_logic).Next(this.end)

    redirect_to_complete_profile = flow.Handle(this.redirect_to_complete_profile_logic).Next(this.admin_email)

    admin_email = flow.Handle(this.send_email_to_admin).Next(this.end)

    end = flow.End()

def move_forward_logic(activation):
    print("Inside move_forward_logic")
    return redirect('token_send')

def redirect_to_complete_profile_logic(activation):
    print("Inside redirect_to_complete_profile_logic")
    return redirect('CompleteProfile')

def send_email_to_admin(activation):
    print("Inside send_email_to_admin")
    user = activation.process.user
    email = user.email
    username = user.username
    admin_email = "vivekyadav2750@gmail.com"
    profile_details_page_url = activation.request.build_absolute_uri(reverse("profileApproval"))
    send_mail(
        "New Approval Request",
        f"A new approval request has been submitted by {username} having email {email}, Please review it at: {profile_details_page_url}.",
        settings.EMAIL_HOST_USER,
        [admin_email],
    )

# class SignupFlow(flow.Flow):
#     start = flow.Start(views.SignupPage).Next(this.create_user_or_render_complete_profile)

#     create_user_or_render_complete_profile = (
#         flow.If(lambda activation: activation.process.filled_fields_count <= 10)
#         .Then(this.send_email_to_admin_and_render_complete_profile)
#         .Else(this.create_user_and_redirect)
#     )

#     send_email_to_admin_and_render_complete_profile = (
#         flow.Handle(this.complete_profile)
#         .Next(this.send_email)
#         .Annotation(title="New message")
#     )

#     complete_profile = (
#         flow.View(views.CompleteProfile)
#         .Next(this.end)
#     )

#     send_email = (
#         flow.Handle(this.send_email_to_admin)
#         .Next(this.end)
#     )

#     create_user_and_redirect = (
#         flow.Handle(this.token_send)
#         .Next(this.end)
#     )

#     token_send = (
#         flow.Handle(views.token_send)
#         .Next(this.end)
#     )

#     end = flow.End()

#     def complete_profile(self, activation):
#         print(activation.process.filled_fields_count)
#         return redirect('CompleteProfile')

#     def send_email_to_admin(self, activation):
#         email = activation.process.signup_email
#         username = activation.process.username
#         admin_email = "vivekyadav2750@gmail.com"
#         profile_details_page_url = activation.request.build_absolute_uri(reverse("profileApproval"))
#         send_mail(
#             "New Approval Request",
#             f"A new approval request has been submitted by {username} having email {email}, Please review it at: {profile_details_page_url}.",
#             settings.EMAIL_HOST_USER,
#             [admin_email],
#         )

    # def token_send(self, activation):
    #     return redirect('token_send')
    

