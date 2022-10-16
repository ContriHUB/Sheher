from tkinter import Place
from django.contrib.auth import authenticate,login, logout
from django.shortcuts import render, redirect
from Visitor.models import VisitorDetails,User
from django.http import HttpResponse, HttpResponseRedirect
from home import urls
from Places.models import PlacesDetails, ComplaintsData
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
        user=User.objects.create_user(email=email,first_name=firstname,last_name=lastname,password=password)
        user.save()
        myfields=VisitorDetails()
        myfields.user=User.objects.get(email=email)
        myfields.city=city
        myfields.address=address
        myfields.phone=phone
        myfields.save()

        return HttpResponse('/')

# user login
def user_login(request):
    data={}
    if request.user.is_authenticated:
        d = request.user
        all_places = PlacesDetails.objects.all()
        data = {
            'places': all_places,
            'user': d,
            'status': '1',
        }
        # print(data)
        return render(request, 'index.html', context=data)

    else :
        if request.method=='POST':
            print(request)
            email=request.POST['email']
            password=request.POST['password']
            user=authenticate(request,email=email,password=password)
            if user:
                login(request,user)
                d = user
                all_places = PlacesDetails.objects.all()
                data = {
                    'places': all_places,
                    'user' : d,
                    'status' : '1',
                }
                # print(data)
                return render(request, 'index.html', context=data)
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
        # complaints = ComplaintsData.objects.filter(user_id=user.id).values()
        # # for i in complaints.values():
        # #     print(i.complaint_title)
        print(gender)
        # print(complaints.get()
        data = {
            'user': user,
            'gender':gender,
            'mobile':mobile,
            'sos':sos,
            'address':address,
            'profile_pic':0,
            # 'complaints': u_complaints,
        }
        return render(request, 'home/profile.html', context=data)


def safety_check(request):
        d = request.user
        all_places = PlacesDetails.objects.all()
        data = {
            'places': all_places,
            'user': d,
            'status': '1',
            'this_place': '',
            'result': '-1',
            'A': {1, 2, 3, 4, 5, 6},
        }
        return render(request,'home/safety_check.html',context=data)

def measure_safety(request,place_id):
        place= PlacesDetails.objects.get(pk=place_id)
        #gender= VisitorDetails.objects.get(pk=user_id).gender
        #place=PlacesDetails.objects.get(name=place_name)
        d = request.user
        v= VisitorDetails.objects.get(user=d)
        gender = v.gender
        # print(gender)
        if gender == 'MALE': gender = 0
        elif gender =='FEMALE': gender = 1
        else: gender = 2
        income=place.avg_income
        density=place.population_density
        age=place.avg_age
        policestationcount=place.police_station_count
        petrolingvans=place.petroling_vans
        moralitylevel=place.morality_level

        # result = getPrediction(0, 18960,50,50000,10,50, 10)
        result = getPrediction(gender, density, age, income , policestationcount, petrolingvans, moralitylevel)
        if result < 0: result=0
        print("prediction: ",result[0])
        result[0]*=10
        result[0]=100-result[0]
        data = {
            'place': place,
            'user': d,
            'status': '1',
            'result': round(result[0]),
            'A': {1, 2, 3, 4, 5, 6},
        }
        return render(request,'home/measure_safety.html',context=data)

def getPrediction(gender, density, age, income , policestationcount, petrolingvans, moralitylevel):
    userdata = [[gender, density, age, income , policestationcount, petrolingvans, moralitylevel]]
    import os
    module_dir = os.path.dirname(__file__)  # get current directory
    file_path = os.path.join(module_dir, 'model2.sav')
    file2 = open(file_path, 'rb')   
    m2 = pickle.load(file2)
    file2.close()
    prediction2 = m2.predict(userdata)
    print(prediction2)

    file_path = os.path.join(module_dir, 'model3.sav')
    file3 = open(file_path, 'rb')   
    m3 = pickle.load(file3)
    file3.close()
    prediction3 = m3.predict(userdata)
    print(prediction3)

    file_path = os.path.join(module_dir, 'model4.sav')
    file4 = open(file_path, 'rb')   
    m4 = pickle.load(file4)
    file4.close()
    prediction4 = m4.predict(userdata)
    print(prediction4)

    file_path = os.path.join(module_dir, 'model5.sav')
    file5 = open(file_path, 'rb')   
    m5 = pickle.load(file5)
    file5.close()
    prediction5 = m5.predict(userdata)
    print(prediction5)
    return (prediction5 + prediction2 + prediction3 + prediction4)/4
    


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
                return render(request,'Visitor/edit_profile_form.html',{'form':form})
        form = EditProfileForm(initial=fields)
        return render(request,'Visitor/edit_profile_form.html',{'form':form})
    else:
        return HttpResponseRedirect('/Visitor/login')
def edit(request):
    pass

