from django.shortcuts import render
from.models import student
# Create your views here.

def home(request):
    return render(request,"home.html")

def register(request):
    if request.method=='POST':
        # print(request.POST)
        name=request.POST.get('nm')
        email=request.POST.get('em')
        contact=request.POST.get('con')
        password=request.POST.get('pass')
        # print(name,email,contact,password)

        # Model_name.objects.create(
        #     col_name=value,
        #     col_name=value,
        #     col_name=value,
        
        student.objects.create(
            stu_name=name,
            stu_email=email,
            stu_contact=contact,
            stu_password=password,
            )
        msg="Registration successfull"
        return render(request,"home.html",{'msg':msg})



    else:
        return render(request,"register.html")
