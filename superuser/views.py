from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
# Create your views here.
from django.utils.encoding import smart_str

from aivaidapp.models import doctor_profile_db, clinic_details_db, user_db, patient_appointment_db
from superuser.forms import categoriesForm, categorieseditForm, blogForm, blogseditForm
from superuser.models import categories, blog
from django.contrib.auth.models import User
import datetime

now = datetime.datetime.now()


@login_required(login_url="login")
def dashboard(request):
    if request.user.is_superuser == 1:
        current_Date = now.strftime("%Y-%m-%d")
        doctor_list = doctor_profile_db.objects.all().count()
        patient_list = user_db.objects.all().count()
        patient_appointment_list = patient_appointment_db.objects.all().count()
        today_patient_appointment_list = patient_appointment_db.objects.filter(date_of_appointment=current_Date).count()

        users_List_Patient = User.objects.filter(is_staff=0)
        users_List_Doctor = User.objects.filter(is_staff=1)

        temp = []
        for user in users_List_Patient:
            if current_Date in smart_str(user.date_joined):
                temp.append(user)
        users_List_Patient_New = len(temp)
        temp = []
        for user in users_List_Doctor:
            if current_Date in smart_str(user.date_joined):
                temp.append(user)
        users_List_Doctor_New = len(temp)

        return render(request, 'super-admin/dashboard.html', locals())
    else:
        return HttpResponseRedirect('../../login', locals())


@login_required(login_url="login")
def Doctorlist(request):
    if request.user.is_superuser == 1:
        doctor_list = doctor_profile_db.objects.all()
        # for doctor in doctor_list:
        #     print(doctor.udob)
        return render(request, 'super-admin/Doctorlist.html', locals())
    else:
        return HttpResponseRedirect('../../login', locals())


@login_required(login_url="login")
def doctorprofile(request, uidb64):
    if request.user.is_superuser == 1:
        doctor_profile = doctor_profile_db.objects.filter(doctor_profile_id=uidb64)
        total = 0
        for i in doctor_profile:
            if len(smart_str(i.doctor_profile_id)) != 0:
                total += 10
            if len(smart_str(i.udob)) != 0:
                total += 10
            if len(smart_str(i.umobile)) != 0:
                total += 10
            if len(smart_str(i.ugender)) != 0:
                total += 10
            if len(smart_str(i.state)) != 0:
                total += 10
            if len(smart_str(i.uregNumber)) != 0:
                total += 10
            if len(smart_str(i.Description)) != 0:
                total += 10
            if len(smart_str(i.selectdegree)) != 0:
                total += 10
            if len(smart_str(i.uexperience01)) != 0:
                total += 10
            if len(smart_str(i.pic)) != 0:
                total += 10

        colour = ''
        if 0 <= total <= 50:
            colour = 'red'
        elif 60 <= total <= 80:
            colour = 'orange'
        else:
            colour = 'green'


        return render(request, 'super-admin/Doctorprofile.html', locals())
    else:
        return HttpResponseRedirect('../../login', locals())


@login_required(login_url="login")
def doctorprofile_approve(request, uidb64):
    if request.user.is_superuser == 1:
        doctor_profile = doctor_profile_db.objects.filter(doctor_profile_id=uidb64).update(admin_verify=1)


        return HttpResponseRedirect('../../superuser/doctorprofile/' + uidb64, locals())
    else:
        return HttpResponseRedirect('../../login', locals())

@login_required(login_url="login")
def doctorprofile_not_approve(request, uidb64):
    if request.user.is_superuser == 1:
        doctor_profile = doctor_profile_db.objects.filter(doctor_profile_id=uidb64).update(admin_verify=2)


        return HttpResponseRedirect('../../superuser/doctorprofile/' + uidb64, locals())
    else:
        return HttpResponseRedirect('../../login', locals())




@login_required(login_url="login")
def Patientlist(request):
    if request.user.is_superuser == 1:
        patient_list = user_db.objects.all()
        return render(request, 'super-admin/Patientlist.html', locals())
    else:
        return HttpResponseRedirect('../../login', locals())


@login_required(login_url="login")
def PatientProfile(request, uidb64):
    if request.user.is_superuser == 1:
        PatientProfile = user_db.objects.filter(id=uidb64)
        return render(request, 'super-admin/Patientprofile.html', locals())
    else:
        return HttpResponseRedirect('../../login', locals())


@login_required(login_url="login")
def Hospitallist(request):
    if request.user.is_superuser == 1:
        return render(request, 'super-admin/Hospitallist.html')
    else:
        return HttpResponseRedirect('../../login', locals())


@login_required(login_url="login")
def Lablist(request):
    if request.user.is_superuser == 1:
        return render(request, 'super-admin/Lablist.html')
    else:
        return HttpResponseRedirect('../../login', locals())


@login_required(login_url="login")
def Chemistlist(request):
    if request.user.is_superuser == 1:
        return render(request, 'super-admin/Chemistlist.html')
    else:
        return HttpResponseRedirect('../../login', locals())


@login_required(login_url="login")
def Cliniclist(request):
    if request.user.is_superuser == 1:
        clinic_List = clinic_details_db.objects.all()
    else:
        return HttpResponseRedirect('../../login', locals())
    return render(request, 'super-admin/Cliniclist.html', locals())


@login_required(login_url="login")
def delete_Clinic(request, string):
    if request.user.is_superuser == 1:
        if len(smart_str(string)) != 0:
            clinic_details_db.objects.filter(id=string).delete()
            return redirect('../cliniclist')
    else:
        return HttpResponseRedirect('../../login', locals())


@login_required(login_url="login")
def delete_Super_Appointment(request, string):
    if request.user.is_superuser == 1:
        if len(smart_str(string)) != 0:
            patient_appointment_db.objects.filter(id=string).delete()
            return redirect('../appointmentlist')
    else:
        return HttpResponseRedirect('../../login', locals())



#-----------------------------------------------------------------------------------------------------------------------
@login_required(login_url="login")
def categorylist(request):
    if request.user.is_superuser == 1:
        categories_data = categories.objects.all().order_by('-id')
        return render(request, 'super-admin/categorylist.html', locals())

    else:
        return HttpResponseRedirect('../../login', locals())


@login_required(login_url="login")
def category(request):
    if request.user.is_superuser == 1:
        return render(request, 'super-admin/category.html')
    else:
        return HttpResponseRedirect('../../login', locals())


@login_required(login_url="login")
def savecategories(request):
    if request.user.is_superuser == 1:
        savedcategories = False
        if request.method == "POST":
            user_id = User.objects.get(id=request.user.id)
            MycategoriesForm = categoriesForm(request.POST)
            if MycategoriesForm.is_valid():
                new_book = MycategoriesForm.save(commit=False)  # Don't save it yet
                new_book.user = user_id
                new_book.save()
                savedcategories = True
                messages.success(request, 'Your Categories Was Saved successfully.')
                return HttpResponseRedirect('../categorylist', locals())
        else:
            categoriesForm()
            messages.error(request, 'Your Categories Was Not  Saved.')
        return HttpResponseRedirect('../categorylist', locals())
    else:
        return HttpResponseRedirect('../../login', locals())


@login_required(login_url="login")
def categorydelete(request, uidb64):
    if request.user.is_superuser == 1:
        emp = categories.objects.get(id=uidb64)
        emp.delete()
        messages.success(request, 'Your Categories Delete successfully.')
        return HttpResponseRedirect('../categorylist', locals())
    else:
        return HttpResponseRedirect('../../login', locals())


def editcategory(request, uidb64):
    if request.user.is_superuser == 1:
        categories_data = categories.objects.filter(id=uidb64)
        return render(request, 'super-admin/editcategory.html', locals())
    else:
        return HttpResponseRedirect('../../login', locals())


@login_required(login_url="login")
def saveeditcategories(request):
    if request.user.is_superuser == 1:
        savedcategories = False
        if request.method == "POST":
            id = request.POST.get("id", "")
            instance = get_object_or_404(categories, id=id)
            form = categorieseditForm(request.POST or None, instance=instance)
            if form.is_valid():
                form.save()
                savedcategories = True
                messages.success(request, 'Your Categories Was Update.')
        else:
            form = categorieseditForm()
            messages.error(request, 'Your Categories Was Not  Update.')
        return HttpResponseRedirect('../categorylist', locals())
    else:
        return HttpResponseRedirect('../../login', locals())


def Bloglist(request):
    if request.user.is_superuser == 1:
        bloglisting = blog.objects.all().order_by('-id')
        return render(request, 'super-admin/Bloglist.html', locals())
    else:
        return HttpResponseRedirect('../../login', locals())


def Addblog(request):
    if request.user.is_superuser == 1:
        categorieslisting = categories.objects.all()
        return render(request, 'super-admin/Addblog.html', locals())
    else:
        return HttpResponseRedirect('../../login', locals())


@login_required(login_url="login")
def Saveblog(request):
    if request.user.is_superuser == 1:
        saved = False
        if request.method == "POST":
            categories_id = request.POST.get("categories", "")
            user_id = User.objects.get(id=request.user.id)
            categories_id = categories.objects.get(id=categories_id)
            MyblogForm = blogForm(request.POST or None, request.FILES)
            if MyblogForm.is_valid():
                new_book = MyblogForm.save(commit=False)  # Don't save it yet
                new_book.user = user_id
                new_book.categories_id = categories_id
                new_book.save()
                saved = True
                messages.success(request, 'Your Blog Was Saved.')
        else:
            MyblogForm = blogForm()
            messages.error(request, 'Your Blog Was Not  Saved.')
        return HttpResponseRedirect('../bloglist', locals())
    else:
        return HttpResponseRedirect('../../login', locals())


@login_required(login_url="login")
def blogdelete(request, uidb64):
    if request.user.is_superuser == 1:
        emp = blog.objects.get(id=uidb64)
        emp.delete()
        messages.success(request, 'Your Blog Delete successfully.')
        return HttpResponseRedirect('../bloglist', locals())
    else:
        return HttpResponseRedirect('../../login', locals())


def editblog(request, uidb64):
    if request.user.is_superuser == 1:
        categorieslisting = categories.objects.all()
        blog_list = blog.objects.filter(id=uidb64)
        return render(request, 'super-admin/editblog.html', locals())
    else:
        return HttpResponseRedirect('../../login', locals())


@login_required(login_url="login")
def saveeditblog(request):
    if request.user.is_superuser == 1:
        savedblog = False
        if request.method == "POST":
            id = request.POST.get("id", "")
            instance = get_object_or_404(blog, id=id)
            form = blogseditForm(request.POST or None, request.FILES or None, instance=instance)
            if form.is_valid():
                form.save()
                savedblog = True
                messages.success(request, 'Your blog Was Update.')
        else:
            form = blogseditForm()
            messages.error(request, 'Your blog Was Not  Update.')
        return HttpResponseRedirect('../bloglist', locals())
    else:
        return HttpResponseRedirect('../../login', locals())





#----------------------------------------------------------------------------------------------------

def Appointmentlist(request):
    if request.user.is_superuser == 1:
        patient_appointment_List = patient_appointment_db.objects.all()
        return render(request, 'super-admin/Appointmentlist.html', locals())
    else:
        return HttpResponseRedirect('../../login', locals())
