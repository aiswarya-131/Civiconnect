import smtplib
from datetime import datetime
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
from django.core.files.storage import FileSystemStorage
from django.http import JsonResponse, request
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, Group


# Create your views here.
from myapp.models import *


def login_get(request):
    return render(request,'loginindex.html')

def login_post(request):
    username=request.POST['username']
    password=request.POST['password']
    user=authenticate(request,username=username,password=password)
    if user is not None:
        login(request,user)
        if user.groups.filter(name='admin').exists():
            return redirect('/myapp/adminhomepage_get/')

        elif user.groups.filter(name='department').exists():
            return redirect('/myapp/departmenthome_get/')

        else:
            return redirect('/myapp/login_get/')
    else:
        return redirect('/myapp/login_get/')

# g=User.objects.get(username='admin')
# g.set_password("12345")
# g.save()

def logout_get(request):
    logout(request)
    return redirect('/myapp/login_get/')


def adminhomepage_get(request):
    return render(request,'Admin/homeadmin.html')

login_required(login_url='/myapp/login_get/')
def adddepartment_get(request):
    return render(request, 'Admin/adddepartment.html')


def adddepartment_post(request):
    name=request.POST['department']
    type=request.POST['type']
    description=request.POST['description']
    contact=request.POST['number']
    email=request.POST['email']
    place=request.POST['place']
    post=request.POST['post']
    city=request.POST['city']
    district=request.POST['district']
    state=request.POST['state']
    pincode=request.POST['pincode']

    user=User.objects.create_user(username=email,password=contact)
    user.groups.add(Group.objects.get(name='department'))
    user.save()

    obj=Department()
    obj.name=name
    obj.type=type
    obj.description=description
    obj.contactno=contact
    obj.email=email
    obj.place=place
    obj.post=post
    obj.city=city
    obj.district=district
    obj.state=state
    obj.pincode=pincode
    obj.AUTHUSER=user
    obj.save()
    return redirect('/myapp/viewdepartment/')

login_required(login_url='/myapp/login_get/')
def viewdepartment(request):
    data=Department.objects.all()
    return render(request, 'Admin/viewdepartment.html',{'data':data})

login_required(login_url='/myapp/login_get/')
def editdepartment_get(request,id):
    data=Department.objects.get(id=id)
    return render(request, 'Admin/editdepartment.html',{'data':data})

login_required(login_url='/myapp/login_get/')
def editdepartment_post(request):
    name = request.POST['department']
    type = request.POST['type']
    description = request.POST['description']
    contact = request.POST['contactno']
    email = request.POST['email']
    place = request.POST['place']
    post = request.POST['post']
    city = request.POST['city']
    district = request.POST['district']
    state = request.POST['state']
    pincode = request.POST['pincode']
    id = request.POST['id']



    obj = Department.objects.get(id=id)
    obj.name = name
    obj.type = type
    obj.description = description
    obj.contactno = contact
    obj.email = email
    obj.place = place
    obj.post = post
    obj.city = city
    obj.district = district
    obj.state = state
    obj.pincode = pincode
    obj.save()
    return redirect('/myapp/viewdepartment/')

login_required(login_url='/myapp/login_get/')
def deletedepartment(request,id):
    Department.objects.filter(id=id).delete()
    return redirect('/myapp/viewdepartment/')

login_required(login_url='/myapp/login_get/')
def viewcomplaint(request):
    b = Complaint.objects.all()
    return render(request, 'Admin/complaintsview.html',{'data':b })

login_required(login_url='/myapp/login_get/')
def viewreview(request):
    a = Review.objects.all()
    return render(request, 'Admin/viewreview.html',{'data':a})

login_required(login_url='/myapp/login_get/')
def changepassword_get(request):
    return render(request, 'Admin/changepassword.html')

login_required(login_url='/myapp/login_get/')
def changepassword_post(request):
    currentpass = request.POST['currentpass']
    newpass = request.POST['newpass']
    confirmpass = request.POST['confirmpass']
    data = request.user
    if data.check_password(currentpass):
        if newpass==confirmpass:
            data.set_password(newpass)
            data.save()
            return redirect('/myapp/login_get/')
        else:
            return redirect('/myapp/ changepassword/')

    else:
        return redirect('/myapp/ changepassword/')


# #deparment
#
login_required(login_url='/myapp/login_get/')
def departmentchangepassword_get(request):
    return render(request, 'department/changepassword.html')

login_required(login_url='/myapp/login_get/')
def departmentchangepassword_post(request):
    currentpass = request.POST['currentpass']
    newpass = request.POST['newpass']
    confirmpass = request.POST['confirmpass']
    data = request.user
    if data.check_password(currentpass):
        if newpass==confirmpass:
            data.set_password(newpass)
            data.save()
            return redirect('/myapp/login_get/')
        else:
            return redirect('/myapp/departmentchangepassword_get/')
    else:
        return redirect('/myapp/departmentchangepassword_get/')


login_required(login_url='/myapp/login_get/')
def departmenthome_get(request):
    return render(request,'department/departmentindex.html')

login_required(login_url='/myapp/login_get/')
def viewcomplaint_get(request):
    return render(request,'department/viewcomplaint.html')

login_required(login_url='/myapp/login_get/')
def viewprofile_get(request):
    a=Department.objects.get(AUTHUSER=request.user)
    return render(request,'department/viewprofile.html',{'data':a})

login_required(login_url='/myapp/login_get/')
def sendreply_get(request):
    return render(request,'department/sendreply.html')

login_required(login_url='/myapp/login_get/')
def sendreply_post(request):
    return redirect('/myapp/viewcomplaint_get/')

login_required(login_url='/myapp/login_get/')
def forgot_password(request):
    return render(request,'forgetpassword.html')


login_required(login_url='/myapp/login_get/')
def forgotpassword_post(request):
    email=request.POST['email']

    if User.objects.filter(username=email).exists():

        import random
        new_pass = random.randint(00000, 99999)
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login("leagaladvisorteam@gmail.com", " eugnxtyylwtqwlav")  # App Password
        to = email
        subject = "Test Email"
        body = "Your new password is " + str(new_pass)
        msg = f"Subject: {subject}\n\n{body}"
        server.sendmail("s@gmail.com", to, msg)  # Disconnect from the server
        server.quit()

        user = User.objects.get(username=email)
        user.set_password(new_pass)
        user.save()

        return redirect('/myapp/login_get/')
    else:
        messages.warning(request, 'email not  exists')
        return redirect('/myapp/forgot_password/')



# ___________________USER____________________________




def signup(request):
    name=request.POST['name']
    dob=request.POST['dob']
    password=request.POST['password']
    gender=request.POST['gender']
    phone=request.POST['phone']
    email=request.POST['email']
    photo=request.FILES['photo']
    place=request.POST['place']
    post=request.POST['post']
    city=request.POST['city']
    district=request.POST['district']
    state=request.POST['state']
    pincode=request.POST['pincode']


    fs=FileSystemStorage()
    s=datetime.now().strftime('%Y%m%d%H%M%S')+'.jpg'
    fs.save(s,photo)
    path=fs.url(s)

    user=User.objects.create(username=email,password=make_password(password))
    user.groups.add(Group.objects.get(name='Users'))

    a = Users()
    a.name = name
    a.dob = dob
    a.password = password
    a.gender = gender
    a.phone = phone
    a.email = email
    a.photo = path
    a.place = place
    a.post = post
    a.city = city
    a.district = district
    a.state = state
    a.pincode = pincode
    a.AUTHUSER =user
    a.save()
    return JsonResponse({'status':'ok'})


def applogin(request):
    username = request.POST['Username']
    password = request.POST['Password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        if user.groups.filter(name='Users').exists():
            return JsonResponse({'status':'ok', 'lid':user.id })

        else:
            return JsonResponse({'status':'no'})

    else:
        return JsonResponse({'status':'no'})



def viewprofile(request):
    lid=request.POST['lid']
    a=Users.objects.get(AUTHUSER=lid)
    return JsonResponse({'status': 'ok',
                         'name':a.name,
                         'dob':a.dob,
                         'gender':a.gender,
                         'phone':a.phone,
                         'email':a.email,
                         'photo':a.photo,
                         'place':a.place,
                         'post':a.post,
                         'city':a.city,
                         'district':a.district,
                         'state':a.state,
                         'pincode':a.pincode})

def editprofile(request):
    name = request.POST['name']
    dob = request.POST['dob']
    gender = request.POST['gender']
    phone = request.POST['phone']
    email = request.POST['email']
    place = request.POST['place']
    post = request.POST['post']
    city = request.POST['city']
    district = request.POST['district']
    state = request.POST['state']
    pincode = request.POST['pincode']
    id = request.POST['lid']

    a = Users.objects.get(AUTHUSER=id)
    a.name = name
    a.dob = dob
    a.gender = gender
    a.phone = phone
    a.email = email

    if 'photo' in request.FILES:
        photo = request.POST['photo']
        fs = FileSystemStorage()
        s = datetime.now().strftime('%Y%m%d%H%M%S') + '.jpg'
        fs.save(s, photo)
        path = fs.url(s)
        a.photo = path
        a.save()

    a.place = place
    a.post = post
    a.city = city
    a.district = district
    a.state = state
    a.pincode = pincode
    a.save()
    return JsonResponse({'status': 'ok'})

def changepassword(request):
    currentpass = request.POST['currentpass']
    newpass = request.POST['newpass']
    confirmpass = request.POST['confirmpass']
    lid = request.POST['lid']
    data = User.objects.get(id=lid)
    if data.check_password(currentpass):
        if newpass == confirmpass:
            data.set_password(newpass)
            data.save()
            return JsonResponse({'status': 'ok'})
        else:
            return JsonResponse({'status': 'no'})
    else:
        return JsonResponse({'status': 'no'})


def sendreview(request):
    review=request.POST['review']
    rating=request.POST['rating']
    lid=request.POST['lid']
    a=Review()
    a.date=datetime.now().today()
    a.review=review
    a.rating=rating
    a.USERS=Users.objects.get(AUTHUSER=lid)
    a.save()
    return JsonResponse({'status': 'ok'})


def sendcomplaint(request):
    complaint = request.POST['complaint']
    photo = request.FILES['photo']
    latitude = request.POST['latitude']
    longitude = request.POST['longitude']
    lid = request.POST['lid']

    fs = FileSystemStorage()
    s = datetime.now().strftime('%Y%m%d%H%M%S') + '.jpg'
    fs.save(s,photo)
    path = fs.url(s)

    a=Complaint()
    a.date=datetime.now().today()
    a.longitude=longitude
    a.latitude=latitude
    a.complaint=complaint
    a.status='pending'
    a.reply='pending'
    a.priority='1'
    a.photo=path
    a.USERS=Users.objects.get(AUTHUSER=lid)
    a.DEPARTMENT_id=2
    a.save()
    return JsonResponse ({'status': 'ok'})


def userviewaction(request):
    lid = request.POST['lid']
    l = []
    data = Complaint.objects.filter(USERS__AUTHUSER_id=lid)
    for i in data:
        l.append({
            'id':i.id,
            'date':i.date,
            'complaint':i.complaint,
            'status':i.status,
            'reply':i.reply,
            'priority':i.priority,
            'longitude':i.longitude,
            'latitude':i.latitude,
            'photo':i.photo,
            'departmentname':i.DEPARTMENT.name
        })

    return JsonResponse({'status': 'ok','data':l})