"""civiconnect URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from myapp import views



urlpatterns = [
    path('login_get/',views.login_get),
    path('login_post/',views.login_post),
    path('logout_get/',views.logout_get),
    path('adminhomepage_get/',views.adminhomepage_get),
    path('adddepartment_get/',views.adddepartment_get),
    path('adddepartment_post/',views.adddepartment_post),
    path('viewdepartment/',views.viewdepartment),
    path('editdepartment_get/<id>',views.editdepartment_get),
    path('editdepartment_post/',views.editdepartment_post),
    path('deletedepartment/<id>',views.deletedepartment),
    path('changepassword_get/',views.changepassword_get),
    path('changepassword_post/',views.changepassword_post),
    path('viewcomplaint/',views.viewcomplaint),
    path('viewreview/',views.viewreview),


    # __________________department





    path('departmentchangepassword_get/',views.departmentchangepassword_get),
    path('departmentchangepassword_post/',views.departmentchangepassword_post),
    path('departmenthome_get/',views.departmenthome_get),
    path('viewcomplaint_get/',views.viewcomplaint_get),
    path('viewprofile_get/',views.viewprofile_get),
    path('sendreply_get/',views.sendreply_get),
    path('sendreply_post/',views.sendreply_post),
    path('forgot_password/',views.forgot_password),
    path('forgotpassword_post/',views.forgotpassword_post),


    # __________USER_________________
    path('signup/',views.signup),
    path('applogin/',views.applogin),
    path('viewprofile/',views.viewprofile),
    path('editprofile/',views.editprofile),
    path('changepassword/',views.changepassword),
    path('sendreview/',views.sendreview),
    path('sendcomplaint/',views.sendcomplaint),
    path('userviewaction/',views.userviewaction),


]
