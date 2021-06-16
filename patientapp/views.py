from __future__ import unicode_literals
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import update_session_auth_hash

# Create your views here.




# -------------------------------AMit sir code -----------------------------------
from django.utils.encoding import smart_str

from aivaidapp.form import user_medical_record_Form, patient_profile_edit_form
from aivaidapp.models import user_db, notification_Db, doctor_profile_db, reports_Db, patient_appointment_db, \
    user_medical_record_db, doctor_Services


@login_required(login_url="login")
def patient_admin(request):
    if request.user.is_staff == 0:
        if user_db.objects.filter(auth_user_id=request.user.id):
            # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#
            notification_List = notification_Db.objects.filter(patient=request.user.id, status=None, sender=1).order_by(
                '-id')
            notification_Length = notification_Db.objects.filter(patient=request.user.id, status=None, sender=1).count()
            # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#
            doctor_len = doctor_profile_db.objects.all().count()
            reports_len = reports_Db.objects.filter(patient=request.user.id).count()
            patient_appointment_len = patient_appointment_db.objects.filter(patient=request.user.id).count()
            patient_appointment_len = patient_appointment_db.objects.filter(patient=request.user.id).count()
            patient_appointment_acc_len = patient_appointment_db.objects.filter(patient=request.user.id,status='accept').count()
            patient_appointment_dec_len = patient_appointment_db.objects.filter(patient=request.user.id,status='decline').count()
            user_list = user_db.objects.filter(auth_user_id=request.user.id)
            for i in user_list:
                if len(smart_str(i.myfile)) != 0:
                    request.session['profile_pic'] = smart_str(i.myfile)
            return render(request, "patient-admin/index.html", locals())
        else:
            # return render(request, "patient-admin/profile.html", locals())
            return redirect('../profile', {'message': 'PLease Fill the Profile First'})
    else:
        return HttpResponseRedirect('../login', locals())


@login_required(login_url="login")
def delete_patient_Appointment(request, string):
    # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#
    notification_List = notification_Db.objects.filter(patient=request.user.id, status=None, sender=1).order_by('-id')
    temp = []
    for i in notification_List:
        temp.append(i.id)
    notification_Length = len(temp)
    # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#
    if smart_str(string) != None:
        if patient_appointment_db.objects.filter(id=smart_str(string)):
            patient_appointment_db.objects.filter(id=smart_str(string)).delete()
            return redirect('../appointments-list')
    else:
        return redirect('../appointments-list')

@login_required(login_url="login")
def del_Service(request, string):
    if request.user.is_staff == 1:
        # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#
        notification_List = notification_Db.objects.filter(patient=request.user.id, status=None, sender=1).order_by('-id')
        temp = []
        for i in notification_List:
            temp.append(i.id)
        notification_Length = len(temp)
        # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#
        if smart_str(string) != None:
            if doctor_Services.objects.filter(id=smart_str(string)):
                doctor_Services.objects.filter(id=smart_str(string)).delete()
                return redirect('../serviceslist')
        else:
            return redirect('../serviceslist')
    else:
        return HttpResponseRedirect('../login', locals())

@login_required(login_url="login")
def profile(request):
    if request.user.is_staff == 0:
        # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#
        notification_List = notification_Db.objects.filter(patient=request.user.id, status=None, sender=1).order_by(
            '-id')
        notification_Length = notification_Db.objects.filter(patient=request.user.id, status=None, sender=1).count()
        # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#
        user_list = user_db.objects.filter(auth_user_id=request.user.id)
        list = User.objects.filter(id=request.user.id)
        total = 0
        for i in user_list:
            if len(smart_str(i.first_name)) != 0:
                total += 10
            if len(smart_str(i.phone)) != 0:
                total += 10
            if len(smart_str(i.address)) != 0:
                total += 10
            if len(smart_str(i.weight)) != 0:
                total += 10
            if len(smart_str(i.blood_group)) != 0:
                total += 10
            if len(smart_str(i.myfile)) != 0:
                request.session['profile_pic'] = smart_str(i.myfile)
                total += 10
            if len(smart_str(i.state)) != 0:
                total += 10
            if len(smart_str(i.height_cm)) != 0:
                total += 10
            if len(smart_str(i.gender)) != 0:
                total += 10
            if len(smart_str(i.body_mass_index)) != 0:
                total += 10
        colour = ''
        if 0 <= total <= 50:
            colour = 'red'
        elif 60 <= total <= 80:
            colour = 'orange'
        else:
            colour = 'green'
        return render(request, "patient-admin/profile.html", locals())

    else:
        return HttpResponseRedirect('../login', locals())



def notice_list_pat(request):
    if request.user.is_staff == 0:
        # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#
        notification_List = notification_Db.objects.filter(patient=request.user.id, status=None, sender=1).order_by(
            '-id')
        notification_Length = notification_Db.objects.filter(patient=request.user.id, status=None, sender=1).count()
        # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#

        notification_List_Pat_Old = notification_Db.objects.filter(patient=request.user.id, sender=1).order_by(
            '-id')
        notification_List_Patient = []
        for i in notification_List_Pat_Old:
            temp = []
            temp.append(i)
            doctordata = User.objects.filter(id=i.doctor)
            for j in doctordata:
                temp.append(smart_str(j.first_name) + ' ' + smart_str(j.last_name))
            notification_List_Patient.append(temp)
    return render(request, 'patient-admin/notifications.html', locals())


def profile_edit(request):
    if request.method == "POST":
        # print('okkkkkkkkk')
        patient_id = request.user.id
        patient_id = User.objects.get(id=patient_id)
        # print(patient_id.id)
        if user_db.objects.filter(auth_user_id=patient_id.id):
            # print(patient_id)
            instance = get_object_or_404(user_db, auth_user_id=patient_id.id)
            MyForm2 = patient_profile_edit_form(request.POST or None, request.FILES or None,instance=instance)
            new_book = MyForm2.save(commit=False)  # Don't save it yet
            new_book.auth_user_id = patient_id
            new_book.save()
            MyForm2.save()
            # print('hllo')
            # instance = get_object_or_404(user_db, auth_user_id=patient_id.id)
            # first_name = request.POST.get("first_name", "")
            # last_name = request.POST.get("last_name", "")
            # print(last_name)
            # phone = request.POST.get("phone", "")
            # age = request.POST.get("age", "")
            # gender = request.POST.get("gender", "")
            # weight = request.POST.get("weight", "")
            # height_cm = request.POST.get("height_cm", "")
            # # height_feet = request.POST.get("htf", "") + request.POST.get("hti", "")
            # blood_group = request.POST.get("blood_group", "")
            # address = request.POST.get("address", "")
            # occupation = request.POST.get("occupation", "")
            # state = request.POST.get("state", "")
            # city = request.POST.get("city", "")
            # body_mass_index = request.POST.get("body_mass_index", "")
            # results = request.POST.get("results", "")
            # request.session['gender'] = gender
            # abc = instance
            # abc.auth_user_id = patient_id
            # abc.first_name = first_name
            # abc.last_name = last_name
            # abc.phone = phone
            # abc.age = age
            # abc.gender = gender
            # abc.weight = weight
            # abc.height_cm = height_cm
            # abc.blood_group = blood_group
            # abc.address = address
            # abc.occupation = occupation
            # abc.state = state
            # abc.city = city
            # abc.body_mass_index = body_mass_index
            # abc.results = results
            # abc.save()
            return HttpResponseRedirect('../profile')


        else:
            # print('hllooooooooooooooooooooo')
            MyForm2 = patient_profile_edit_form(request.POST or None, request.FILES)
            new_book = MyForm2.save(commit=False)  # Don't save it yet
            new_book.auth_user_id = patient_id
            new_book.save()
            MyForm2.save()
            # print('hllooooooooooooooooooooo')
            # first_name = request.POST.get("first_name", "")
            # last_name = request.POST.get("last_name", "")
            # phone = request.POST.get("phone", "")
            # age = request.POST.get("age", "")
            # gender = request.POST.get("gender", "")
            # weight = request.POST.get("weight", "")
            # height_cm = request.POST.get("height_cm", "")
            # # height_feet = request.POST.get("htf", "") + request.POST.get("hti", "")
            # blood_group = request.POST.get("blood_group", "")
            # address = request.POST.get("address", "")
            # occupation = request.POST.get("occupation", "")
            # state = request.POST.get("state", "")
            # city = request.POST.get("city", "")
            # body_mass_index = request.POST.get("body_mass_index", "")
            # results = request.POST.get("results", "")
            # request.session['gender'] = gender
            # abc = user_db()
            # abc.auth_user_id = patient_id
            # abc.first_name = first_name
            # abc.last_name = last_name
            # abc.phone = phone
            # abc.age = age
            # abc.gender = gender
            # abc.weight = weight
            # abc.height_cm = height_cm
            # abc.blood_group = blood_group
            # abc.address = address
            # abc.occupation = occupation
            # abc.state = state
            # abc.city = city
            # abc.body_mass_index = body_mass_index
            # abc.results = results
            # abc.save()
            return HttpResponseRedirect('../profile')


            # else:
            # return HttpResponseRedirect('../profile')
    else:
        print('else')


@login_required(login_url="login")
def account_details(request):
    # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#
    notification_List = notification_Db.objects.filter(patient=request.user.id, status=None, sender=1).order_by(
        '-id')
    notification_Length = notification_Db.objects.filter(patient=request.user.id, status=None, sender=1).count()
    # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#
    return render(request, "patient-admin/account-details.html", locals())


@login_required(login_url="login")
def online_consultation(request):
    # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#
    notification_List = notification_Db.objects.filter(patient=request.user.id, status=None, sender=1).order_by(
        '-id')
    notification_Length = notification_Db.objects.filter(patient=request.user.id, status=None, sender=1).count()
    # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#
    return render(request, "patient-admin/online-consultation.html", locals())


@login_required(login_url="login")
def appointments_list(request):
    # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#
    notification_List = notification_Db.objects.filter(patient=request.user.id, status=None, sender=1).order_by(
        '-id')
    notification_Length = notification_Db.objects.filter(patient=request.user.id, status=None, sender=1).count()
    # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#
    appointment_list = patient_appointment_db.objects.filter(patient=request.user.id).order_by('-id')
    return render(request, "patient-admin/appointments-list.html", locals())


@login_required(login_url="login")
def medical_record(request):
    # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#
    notification_List = notification_Db.objects.filter(patient=request.user.id, status=None, sender=1).order_by(
        '-id')
    notification_Length = notification_Db.objects.filter(patient=request.user.id, status=None, sender=1).count()
    # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#
    medical_list = user_medical_record_db.objects.filter(user_id=request.user.id).order_by('-id')

    return render(request, "patient-admin/medical-record.html", locals())


@login_required(login_url="login")
def add_medical_record(request):
    if request.user.is_staff == 0:
        if request.method == "POST":
            user_id = User.objects.get(id=request.user.id)
            MyForm = user_medical_record_Form(request.POST or None, request.FILES)
            if MyForm.is_valid():
                new_book = MyForm.save(commit=False)  # Don't save it yet
                new_book.user_id = user_id
                new_book.save()
                saved = True
                return HttpResponseRedirect('../medical-record', locals())

        else:
            x = ''
    else:
        return HttpResponseRedirect('../login', locals())

    return HttpResponseRedirect('../medical-record', locals())


@login_required(login_url="login")
def edit_medical_record(request):
    if request.user.is_staff == 0:
        if request.method == "POST":
            id = request.POST.get("id", "")
            user_id = User.objects.get(id=request.user.id)
            instance = get_object_or_404(user_medical_record_db, id=id)
            MyForm = user_medical_record_Form(request.POST or None, request.FILES or None, instance=instance)
            if MyForm.is_valid():
                new_book = MyForm.save(commit=False)  # Don't save it yet
                new_book.user_id = user_id
                new_book.save()
                saved = True
                print('kkkkkkkkkkkkkkkkkkkkkkkkkkkkk')
                return HttpResponseRedirect('../medical-record', locals())

        else:
            x = ''
    else:
        return HttpResponseRedirect('../login', locals())

    return HttpResponseRedirect('../medical-record', locals())


@login_required(login_url="login")
def medical_record_delete(request, record_id):
    if request.user.is_staff == 0:
        emp = user_medical_record_db.objects.get(id=record_id)
        emp.delete()
        messages.error(request, 'medical record was succesfully delete')
    else:
        return HttpResponseRedirect('../login', locals())

    return HttpResponseRedirect('../medical-record', locals())


@login_required(login_url="login")
def notifications(request):
    # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#
    notification_List = notification_Db.objects.filter(patient=request.user.id, status=None, sender=1).order_by(
        '-id')
    notification_Length = notification_Db.objects.filter(patient=request.user.id, status=None, sender=1).count()
    # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#
    return render(request, "patient-admin/notifications.html", locals())


@login_required(login_url="login")
def transaction_list(request):
    # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#
    notification_List = notification_Db.objects.filter(patient=request.user.id, status=None, sender=1).order_by(
        '-id')
    notification_Length = notification_Db.objects.filter(patient=request.user.id, status=None, sender=1).count()
    # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#
    return render(request, "patient-admin/transactions-list.html", locals())


@login_required(login_url="login")
def read_notification_pat(request, string):
    if smart_str(string) != None:
        id, check = smart_str(string).split('__')
        notification_Db.objects.filter(id=id).update(status='Read')
        if check == 'appointment_accepted':
            return redirect('../appointments-list')
        elif check == 'appointment_declined':
            return redirect('../appointments-list')
        elif check == 'report_added':
            return redirect('../notice-list-pat')
        elif check == 'rechedule_appointment':
            return redirect('../appointment-list-pat')
        else:
            return redirect('../notice-list-pat')


def faqs(request):
    return render(request, 'patient-admin/faqs.html')
