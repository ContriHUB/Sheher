from django.contrib.auth import authenticate,login, logout
from django.shortcuts import render, redirect
from Visitor.models import VisitorDetails,User
from django.http import HttpResponse, HttpResponseRedirect
from home import urls
from Places.models import PlacesDetails, ComplaintsData, RatingReview
import pickle
from django.conf import settings
from twilio.rest import Client
from django import forms
from Visitor.forms import EditProfileForm
from django.core.mail import send_mail
from django.http import HttpResponse
from Sheher import settings
from django.core.mail import send_mail
from django.contrib import messages


def user_signup(request):
    if request.method=='POST':
        firstname=request.POST["firstname"]
        lastname=request.POST["lastname"]
        email=request.POST["email"]
        password=request.POST['password']
        city=request.POST['city']
        address=request.POST['address']
        phone=request.POST['phone']
        sos_contact=request.POST['sos']
        profile_pic=request.FILES['profile_pic']
        user=User.objects.create_user(email=email,first_name=firstname,last_name=lastname,password=password)
        user.save()
        myfields=VisitorDetails()
        myfields.user=User.objects.get(email=email)
        myfields.city=city
        myfields.address=address
        myfields.phone=phone
        myfields.profile_picture = profile_pic
        myfields.save()
        return HttpResponse('User account created')

# user login
def user_login(request):
    data={}
    if request.user.is_authenticated:
        return redirect('../../')
    else :
        if request.method=='POST':
            # print(request)
            email=request.POST['email']
            password=request.POST['password']
            user=authenticate(request,email=email,password=password)
            if user:
                login(request,user)
                messages.success(request, 'Logged in successfully')
                return redirect('../../')
            else:
                data={
                    'error':'Invalid Credentials',
                    'status':'0',
                      }
                return render(request, 'home/register.html', data)
        else:
            all_places = PlacesDetails.objects.all()
            data = {
                'places' : all_places,
                'status':'0',
            }
            return render(request, 'home/register.html', data)


#user dashboard
def dashboard(request):
    pass
# Create your views here.

def user_logout(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request, 'Logged out successfully')
        return redirect('/')
    else:
        return redirect('/')


def profile(request):
    if request.user.is_authenticated:
        print(request.POST)
        user = request.user
        gender = VisitorDetails.objects.get(user_id=user).gender
        sos = VisitorDetails.objects.get(user_id=user).sos_contact
        mobile = VisitorDetails.objects.get(user_id=user).phone
        address = VisitorDetails.objects.get(user_id=user).address
        profile_pic = VisitorDetails.objects.get(user_id=user).profile_picture
        # complaints = ComplaintsData.objects.filter(user_id=user.id).values()
        # # for i in complaints.values():
        # #     print(i.complaint_title)
        # print(complaints.get()
        data = {
            'user': user,
            'gender':gender,
            'mobile':mobile,
            'sos':sos,
            'address':address,
            'profile_pic':profile_pic,
            # 'complaints': u_complaints,
            'status':'1',
        }
        return render(request, 'home/profile.html', context=data)

# SOS
def SOS(request):
    if request.user.is_authenticated:
        subject = "Greetings"
        msg = "Congratulations for your success"
        to = request.user.email
        res = send_mail(subject, msg, settings.EMAIL_HOST_USER, [to])
        if res == 1:
            msg = "Mail Sent Successfuly"
        else:
            msg = "Mail could not sent"
        print(msg)
        account_sid = 'AC34ee140258455678b0ce14baf8dffefb'
        auth_token = '4e1cb93f875a151baea34cc6a950c512'
        client = Client(account_sid, auth_token)

        message = client.messages.create(
                                        body=f'Hello buddy',
                                        from_='+19894673701',
                                        to='+919830936340',
                                    )
            # print(message.sid)
        return HttpResponse('Message sent')
    else:
        return HttpResponseRedirect('/Visitor/login')
#     edit profile
def edit_profile(request):
    if request.user.is_authenticated:
        print(request.user)
        myfields=VisitorDetails.objects.get(user=User.objects.get(email=request.user.email))
        fields={
            'first_name':myfields.user.first_name,
            'last_name':myfields.user.last_name,
            'gender':myfields.gender,
            'phone':myfields.phone,
            'sos_contact':myfields.sos_contact,
            'address':myfields.address,
        }
        if request.method == 'POST':
            form = EditProfileForm(request.POST)
            if form.is_valid():
                messages.success(request, 'Profile details updated.')
                return render(request,'Visitor/edit_profile_form.html',{'form':form,'status':'1'})
        form = EditProfileForm(initial=fields)
        user=request.user
        profile_pic = VisitorDetails.objects.get(user_id=user).profile_picture
        return render(request,'Visitor/edit_profile_form.html',{'form':form,'status':'1','profile_pic':profile_pic,})
    else:
        return HttpResponseRedirect('/Visitor/login')
def edit(request):
    pass

