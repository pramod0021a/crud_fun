from django.shortcuts import render, HttpResponseRedirect
from .forms import StudentForm
from .models import Student

# Add and show data.
def index_fun(request):
   if request.method == 'POST':
      fm = StudentForm(request.POST)
      if fm.is_valid():
         # fm.save()
         nm = fm.cleaned_data['name']
         ag = fm.cleaned_data['age']
         lcn = fm.cleaned_data['location']
         add = Student(name=nm, age=ag, location=lcn)
         add.save()
         fm = StudentForm()
   else:
      fm = StudentForm()

   stud = Student.objects.all()
   return render(request, 'mains/index.html', {'form':fm, 'stu':stud})

# Update Data
def update_student(request, id):
   if request.method == 'POST':
      pi = Student.objects.get(pk=id)
      fm = StudentForm(request.POST, instance=pi)
      if fm.is_valid():
         fm.save()
         fm = StudentForm()
   else:
      pi = Student.objects.get(pk=id)
      fm = StudentForm(instance=pi)

       
   return render(request, 'mains/update.html', {'form':fm})

# Delete Data
def delete_student(request, id):    
   pi = Student.objects.get(pk=id)    

   if request.method=="POST":
      pi.delete()
      return HttpResponseRedirect('/')