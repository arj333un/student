from django.shortcuts import render,redirect
from student.models import StudentDetails

# Create your views here.

def student(request):
    return render(request,'register.html')

def register(request):
    if request.method=='POST':
        sname=request.POST['name']
        saddress=request.POST['address']
        sage=request.POST['age']
        semail=request.POST['email']
        jdate=request.POST['date']
        squalification=request.POST['qualification']
        sgender=request.POST['gender']
        snumber=request.POST['number']
        student=StudentDetails(student_name=sname,address=saddress,age=sage,email=semail,join_date=jdate,qualification=squalification,gender=sgender,number=snumber)
        student.save()
        return redirect('show_student_details')
    
def show_student_details(request):
    student=StudentDetails.objects.all()
    return render(request,"view.html",{'stu': student})

def editstd(request,pk):
    std=StudentDetails.objects.get(id=pk)
    q=StudentDetails.objects.values("qualification").distinct()
    return render (request,"edit.html",{'student':std,'q':q})

def edit_student_details(request,pk):
    if request.method=="POST":
        std=StudentDetails.objects.get(id=pk)
        std.student_name=request.POST.get("stdname")
        std.address=request.POST.get("stdaddress")
        std.age=request.POST.get("stdage")
        std.email=request.POST.get("stdemail")
        std.join_date=request.POST.get("stddate")
        std.qualification=request.POST.get("stdqualification")
        std.gender=request.POST.get("stdgender")
        std.number=request.POST.get("stdnumber")
        std.save()
        return redirect("show_student_details")
    return render(request,"edit.html")

def deletestd(request,pk):
    emp=StudentDetails.objects.get(id=pk)
    emp.delete()
    show_student_details(request)
    return redirect('show_student_details')

def show_student(request,pk):
    students=StudentDetails.objects.get(id=pk)
    return render(request,"card.html",{'std': students})

def back(request):
    show_student_details(request)
    return redirect('show_student_details')   
 
 
