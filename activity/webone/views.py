from imaplib import _Authenticator
from django.shortcuts import  redirect,render,HttpResponse
from webone.forms import PUPIL_DetailsForm, Personal_DetailsForm, Prant_DetailsForm 
from .models import *
from .models import Personal_Details
from .models import Prant_Details
from .models import PUPIL_Details
from django.contrib.auth import authenticate, login
# Create your views here.
from django.views.decorators.csrf import csrf_exempt


def home(request):
        
        student_id = request.POST['student_id']
        Aname= request.POST['Aname']
        name = request.POST['name']
        Adate = request.POST['Adate']
        division = request.POST['division']
        gender = request.POST['gender']
        db_birth = request.POST['db_birth']
        age = request.POST['age']
        nationality = request.POST['nationality']
        religion = request.POST['religion']
        cast = request.POST['cast']
        state = request.POST['state']
        category = request.POST['category']
        sylubus = request.POST['sylubus']
        tongues = request.POST['tongues']
        id_marks = request.POST['id_marks']

        #Parent
        Ad_Number=request.POST['Ad_Number']
        Parent_Name=request.POST['Parent_Name']
        relation=request.POST['relation']
        Parent_Occ=request.POST['Parent_Occ']
        Parent_Add=request.POST['Parent_Add']
        tele_number=request.POST['tele_number']
        G_name=request.POST['G_name']
        G_address=request.POST['G_address']
        G_tele_number=request.POST['G_tele_number']
        Prant_Mobile_num=request.POST['Prant_Mobile_num']
        email=request.POST['email']
        G_Mobile_num=request.POST['G_Mobile_num']
        Pincode=request.POST['Pincode']
        Income=request.POST['Income']
        Parent_ID=request.POST['Parent_ID']
        #PUPIL
        Rg_Number=request.POST['Rg_Number']
        Adate=request.POST['Adate']
        Yumedium=request.POST['Yumedium']
        Lschool=request.POST['Lschool']
        Lstandard=request.POST['Lstandard']
        Lmedium=request.POST['Lmedium']
        LDate_Admission=request.POST['LDate_Admission']
        LDate_Leave=request.POST['LDate_Leave']
        Transfer_date=request.POST['Transfer_date']
        Remarks=request.POST['Remarks']
        mark=request.POST['mark']
        total_mark=request.POST['total_mark']
        ages=request.POST['age']

        student = Personal_Details.objects.create(student_id=student_id,Aname=Aname,name=name,Adate=Adate,division=division,gender=gender,db_birth=db_birth,age=age,nationality=nationality,religion=religion,cast=cast,state=state,category=category,sylubus=sylubus,tongues=tongues,id_marks=id_marks)
        student.save()
        Parent = Prant_Details.objects.create(Ad_Number=Ad_Number,Parent_Name=Parent_Name,relation=relation,Parent_Occ=Parent_Occ,Parent_Add=Parent_Add,tele_number=tele_number,G_name=G_name,G_address=G_address,G_tele_number=G_tele_number,Prant_Mobile_num=Prant_Mobile_num,email=email,G_Mobile_num=G_Mobile_num,Pincode=Pincode,Income=Income,Parent_ID=Parent_ID)
        Parent.save()
        pupil = PUPIL_Details.objects.create(Rg_Number=Rg_Number,Adate=Adate,Yumedium=Yumedium,Lschool=Lschool,Lstandard=Lstandard,Lmedium=Lmedium,LDate_Admission=LDate_Admission,LDate_Leave=LDate_Leave,Transfer_date=Transfer_date,Remarks=Remarks,mark=mark,total_mark=total_mark,ages=ages)
        pupil.save()
        return render(request,"profile.html")

def listallstu(request):
    students = Personal_Details.objects.all()
    parents = Prant_Details.objects.all()
    pupils = PUPIL_Details.objects.all()
    return render(request,"listall.html",{'students':students,'parents':parents,'pupils':pupils})


def edit(request,id):
    students = Personal_Details.objects.get(id=id)
    parents = Prant_Details.objects.get(id=id)
    pupils = PUPIL_Details.objects.get(id=id)
    return render(request,"edit.html",{'students':students,'parents':parents,'pupils':pupils})
  

def demo(request):
    return render(request,"index.html")

def update(request,students,parents,pupils,id):
    students = Personal_Details.objects.get(id=id)
    parents = Prant_Details.objects.get(id=id)
    pupils = PUPIL_Details.objects.get(id=id)
    return render(request,"edit.html",{'students':students,'parents':parents,'pupils':pupils})
  
 
def profile(request,students,id):
    students = Personal_Details.objects.get(id=id)
    return render(request,"profile.html",{'students':students})

# def submit_redirect_view(request,students,id):
#     students = Personal_Details.objects.get(id=id)
#     return render(request, 'submit.html', {'students': students})