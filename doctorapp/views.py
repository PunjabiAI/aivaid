from __future__ import unicode_literals

import urllib

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.utils.encoding import smart_str

from aivaid import settings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from aivaidapp.form import clinic_details_Form, doctor_patient_report_form, doctor_user_edit_profile_form, \
    doctor_profile_edit_form, clinic_pic_forms
from aivaidapp.models import notification_Db, clinic_details_db, doctor_profile_db, patient_appointment_db, user_db, \
    reports_Db, doctor_patient_report, doctor_patient_db, disease_db, doctor_Services, instamojo_payment_done, \
    clinic_pic_db, review_db
from django.contrib.auth.models import User

from superuser.forms import blogseditForm, blogForm, categorieseditForm, categoriesForm
from superuser.models import blog, categories

def handler(request, *args, **argv):
    return render(request, "404.html", locals())


def handler50(request):
    return render(request, "404.html", locals())


@login_required(login_url="login")
def aivaid_admin(request):
    if request.user.is_staff == 1:
        total = 0
        user_table_list = User.objects.filter(id=request.user.id)
        profile_list = doctor_profile_db.objects.filter(doctor_profile_id=request.user.id)
        for i in profile_list:
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

        if total == 100:

            if clinic_details_db.objects.filter(doctor_profile_id=request.user.id):

                doctor = doctor_profile_db.objects.filter(doctor_profile_id=request.user.id)
                # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#
                notification_List = notification_Db.objects.filter(doctor=request.user.id, status=None, sender=0).order_by(
                    '-id')
                notification_Length = notification_Db.objects.filter(doctor=request.user.id, status=None, sender=0).count()
                # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#
                for doctor in doctor:
                    appointment_decline_list = patient_appointment_db.objects.filter(doctor=doctor.id, status='decline',
                                                                                     treatment=None).count()
                    appointment_accept_list = patient_appointment_db.objects.filter(doctor=doctor.id, status='accept',
                                                                                    treatment=None).count()
                    book_appointment_list = patient_appointment_db.objects.filter(doctor=doctor.id, status=None,
                                                                                  treatment=None).count()
                    patient_list = patient_appointment_db.objects.filter(doctor=doctor.id,
                                                                         treatment='Under_Treatment').count()
                return render(request, "doctor-panel/index.html", locals())
            else:
                value =0
                return HttpResponseRedirect('../clinic-details/', locals())
        else:
            return HttpResponseRedirect('../doctor-profile/', locals())


    else:
        return HttpResponseRedirect('../login', locals())


def notice_list_doc(request):
    # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#
    notification_List = notification_Db.objects.filter(doctor=request.user.id, status=None, sender=0).order_by(
        '-id')
    notification_Length = notification_Db.objects.filter(doctor=request.user.id, status=None, sender=0).count()
    # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#
    notification_List_Doctor = notification_Db.objects.filter(doctor=request.user.id, sender=0).order_by(
        '-id')

    return render(request, 'doctor-panel/notice-list.html', locals())


def clinic_details(request):
    if request.user.is_staff == 1:

        # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#
        notification_List = notification_Db.objects.filter(doctor=request.user.id, status=None, sender=0).order_by(
            '-id')
        notification_Length = notification_Db.objects.filter(doctor=request.user.id, status=None, sender=0).count()
        # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#
        review_list_count = review_db.objects.filter(doctor_profile_id=request.user.id).count()
        review_list_5 = review_db.objects.filter(doctor_profile_id=request.user.id, rating1='5').count()
        review_list_4 = review_db.objects.filter(doctor_profile_id=request.user.id, rating1='4').count()
        review_list_3 = review_db.objects.filter(doctor_profile_id=request.user.id, rating1='3').count()
        review_list_2 = review_db.objects.filter(doctor_profile_id=request.user.id, rating1='2').count()
        review_list_1 = review_db.objects.filter(doctor_profile_id=request.user.id, rating1='1').count()
        if review_list_count:

            review_list_avrage = (5 * review_list_5 + 4 * review_list_4 + 3 * review_list_3 + 2 * review_list_2 + 1 * review_list_1) / review_list_count
        else:
            review_list_avrage = 0

        doctor_profile_list = doctor_profile_db.objects.filter(doctor_profile_id=request.user.id)
        clinic_list = clinic_details_db.objects.filter(doctor_profile_id=request.user.id)
        clinic_pic_list = clinic_pic_db.objects.filter(doctor_profile_id=request.user.id)
        total = 0
        for i in doctor_profile_list:
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
            if 0 <= total <= 50:
                colour = 'red'
            elif 60 <= total <= 80:
                colour = 'orange'
            else:
                colour = 'green'
            print('+++++++++++++++')
            print(i.selectdegree)
            print('+++++++++++++++')
        return render(request, 'doctor-panel/clinic-detail.html', locals())

    else:
        return HttpResponseRedirect('../login', locals())



@login_required(login_url="login")
def delete_clinic_details(request, string):
    if smart_str(string) != None:
        if clinic_details_db.objects.filter(id=smart_str(string)):
            clinic_details_db.objects.filter(id=smart_str(string)).delete()
            return redirect('../clinic-details')
    else:
        return redirect('../clinic-details')






@login_required(login_url="login")
def read_notification_doc(request, string):
    if smart_str(string) != None:
        id, check = smart_str(string).split('__')
        notification_Db.objects.filter(id=id).update(status='Read')
        if check == 'new_appointment':
            return redirect('../appointment-list')
        else:
            return redirect('../notice-list-doc')
            # else:
            #     return HttpResponseRedirect('../login', locals())


@login_required(login_url="login")
def add_clinic_details(request):
    if request.user.is_staff == 1:
        if request.method == "POST":
            if request.POST.getlist("sunday_appt_time1"):
                sunday_appt_time1=[]

                sunday_appt_time1 = request.POST.getlist("sunday_appt_time1")
                sunday_appt_time2 = request.POST.getlist("sunday_appt_time2")
            else :
                sunday_appt_time1 = None
                sunday_appt_time2 = None
            if request.POST.getlist("monday_appt_time1"):
                monday_appt_time1 = request.POST.getlist("monday_appt_time1")
                monday_appt_time2 = request.POST.getlist("monday_appt_time2")
            else :
                monday_appt_time1 = None
                monday_appt_time2 = None
            if request.POST.getlist("tuesday_appt_time1"):
                tuesday_appt_time1 = request.POST.getlist("tuesday_appt_time1")
                tuesday_appt_time2 = request.POST.getlist("tuesday_appt_time2")
            else :
                tuesday_appt_time1 = None
                tuesday_appt_time2 = None
            if request.POST.getlist("wednesday_appt_time1"):
                wednesday_appt_time1 = request.POST.getlist("wednesday_appt_time1")
                wednesday_appt_time2 = request.POST.getlist("wednesday_appt_time2")
            else :
                wednesday_appt_time1 = None
                wednesday_appt_time2 = None
            if request.POST.getlist("thursday_appt_time1"):
                thursday_appt_time1 = request.POST.getlist("thursday_appt_time1")
                thursday_appt_time2 = request.POST.getlist("thursday_appt_time2")
            else :
                thursday_appt_time1 = None
                thursday_appt_time2 = None
            if request.POST.getlist("friday_appt_time1"):
                friday_appt_time1 = request.POST.getlist("friday_appt_time1")
                friday_appt_time2 = request.POST.getlist("friday_appt_time2")
            else :
                friday_appt_time1 = None
                friday_appt_time2 = None
            if request.POST.getlist("saturday_appt_time1"):
                saturday_appt_time1 = request.POST.getlist("saturday_appt_time1")
                saturday_appt_time2 = request.POST.getlist("saturday_appt_time2")
            else :
                saturday_appt_time1 = None
                saturday_appt_time2 = None


            doctor_id = User.objects.get(id=request.user.id)
            MyForm = clinic_details_Form(request.POST or None, request.FILES)
            if MyForm.is_valid():
                new_book = MyForm.save(commit=False)  # Don't save it yet
                new_book.doctor_profile_id = doctor_id
                new_book.sunday_appt_time1 = sunday_appt_time1
                new_book.sunday_appt_time2 = sunday_appt_time2
                new_book.monday_appt_time1 = monday_appt_time1
                new_book.monday_appt_time2 = monday_appt_time2
                new_book.tuesday_appt_time1 = tuesday_appt_time1
                new_book.tuesday_appt_time2 = tuesday_appt_time2
                new_book.wednesday_appt_time1 = wednesday_appt_time1
                new_book.wednesday_appt_time2 = wednesday_appt_time2
                new_book.thursday_appt_time1 = thursday_appt_time1
                new_book.thursday_appt_time2 = thursday_appt_time2
                new_book.friday_appt_time1 = friday_appt_time1
                new_book.friday_appt_time2 = friday_appt_time2
                new_book.saturday_appt_time1 = saturday_appt_time1
                new_book.saturday_appt_time2 = saturday_appt_time2
                new_book.save()
                saved = True
                return HttpResponseRedirect('../clinic-details', locals())


        else:
            x = ''
            return HttpResponseRedirect('../clinic-details', locals())

    else:
        return HttpResponseRedirect('../login', locals())

    return HttpResponseRedirect('../clinic-details', locals())


@login_required(login_url="login")
def edit_clinic_details(request):
    if request.user.is_staff == 1:
        if request.method == "POST":
            id = request.POST.get("id", "")
            if request.POST.getlist("sunday_appt_time1"):
                sunday_appt_time1=[]
                sunday_appt_time1 = request.POST.getlist("sunday_appt_time1")
                sunday_appt_time2 = request.POST.getlist("sunday_appt_time2")
            else:
                sunday_appt_time1 = None
                sunday_appt_time2 = None
            if request.POST.getlist("monday_appt_time1"):
                monday_appt_time1 = request.POST.getlist("monday_appt_time1")
                monday_appt_time2 = request.POST.getlist("monday_appt_time2")
            else:
                monday_appt_time1 = None
                monday_appt_time2 = None
            if request.POST.getlist("tuesday_appt_time1"):
                tuesday_appt_time1 = request.POST.getlist("tuesday_appt_time1")
                tuesday_appt_time2 = request.POST.getlist("tuesday_appt_time2")
            else:
                tuesday_appt_time1 = None
                tuesday_appt_time2 = None
            if request.POST.getlist("wednesday_appt_time1"):
                wednesday_appt_time1 = request.POST.getlist("wednesday_appt_time1")
                wednesday_appt_time2 = request.POST.getlist("wednesday_appt_time2")
            else:
                wednesday_appt_time1 = None
                wednesday_appt_time2 = None
            if request.POST.getlist("thursday_appt_time1"):
                thursday_appt_time1 = request.POST.getlist("thursday_appt_time1")
                thursday_appt_time2 = request.POST.getlist("thursday_appt_time2")
            else:
                thursday_appt_time1 = None
                thursday_appt_time2 = None
            if request.POST.getlist("friday_appt_time1"):
                friday_appt_time1 = request.POST.getlist("friday_appt_time1")
                friday_appt_time2 = request.POST.getlist("friday_appt_time2")
            else:
                friday_appt_time1 = None
                friday_appt_time2 = None
            if request.POST.getlist("saturday_appt_time1"):
                saturday_appt_time1 = request.POST.getlist("saturday_appt_time1")
                saturday_appt_time2 = request.POST.getlist("saturday_appt_time2")
            else:
                saturday_appt_time1 = None
                saturday_appt_time2 = None

            doctor_id = User.objects.get(id=request.user.id)
            instance = get_object_or_404(clinic_details_db, id=id)

            MyForm = clinic_details_Form(request.POST or None, request.FILES or None, instance=instance)
            if MyForm.is_valid():
                new_book = MyForm.save(commit=False)  # Don't save it yet
                new_book.doctor_profile_id = doctor_id
                new_book.sunday_appt_time1 = sunday_appt_time1
                new_book.sunday_appt_time2 = sunday_appt_time2
                new_book.monday_appt_time1 = monday_appt_time1
                new_book.monday_appt_time2 = monday_appt_time2
                new_book.tuesday_appt_time1 = tuesday_appt_time1
                new_book.tuesday_appt_time2 = tuesday_appt_time2
                new_book.wednesday_appt_time1 = wednesday_appt_time1
                new_book.wednesday_appt_time2 = wednesday_appt_time2
                new_book.thursday_appt_time1 = thursday_appt_time1
                new_book.thursday_appt_time2 = thursday_appt_time2
                new_book.friday_appt_time1 = friday_appt_time1
                new_book.friday_appt_time2 = friday_appt_time2
                new_book.saturday_appt_time1 = saturday_appt_time1
                new_book.saturday_appt_time2 = saturday_appt_time2
                new_book.save()
                saved = True
                return HttpResponseRedirect('../clinic-details', locals())


        else:
            x = ''
            return HttpResponseRedirect('../clinic-details', locals())

    else:
        return HttpResponseRedirect('../login', locals())

    return HttpResponseRedirect('../clinic-details', locals())





@login_required(login_url="login")
def save_clinic_pic(request):
    print('------------------------------------')
    if request.user.is_staff == 1:
        if request.method == "POST":
            print('------------------------------------')

            clinic_id=request.POST.get("clinic_id", "")


            if clinic_pic_db.objects.filter(clinic_id=clinic_id):
                instance = clinic_pic_db.objects.get(clinic_id=clinic_id)
                doctor_id = User.objects.get(id=request.user.id)
                clinic_id = clinic_details_db.objects.get(id=clinic_id)
                MyForm = clinic_pic_forms(request.POST or None, request.FILES or None,instance=instance)
                if MyForm.is_valid():
                    new_book = MyForm.save(commit=False)  # Don't save it yet
                    new_book.doctor_profile_id = doctor_id
                    new_book.clinic_id = clinic_id
                    new_book.save()
                    saved = True
            else:
                doctor_id = User.objects.get(id=request.user.id)
                clinic_id = clinic_details_db.objects.get(id=clinic_id)
                MyForm = clinic_pic_forms(request.POST or None, request.FILES)
                if MyForm.is_valid():
                    new_book = MyForm.save(commit=False)  # Don't save it yet
                    new_book.doctor_profile_id = doctor_id
                    new_book.clinic_id = clinic_id
                    new_book.save()
                    saved = True

            return HttpResponseRedirect('../clinic-details', locals())


        else:
            x = ''
            return HttpResponseRedirect('../clinic-details', locals())

    else:
        return HttpResponseRedirect('../login', locals())

    return HttpResponseRedirect('../clinic-details', locals())











@login_required(login_url="login")
def appointment_list(request):
    if request.user.is_staff == 1:
        # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#
        notification_List = notification_Db.objects.filter(doctor=request.user.id, status=None, sender=0).order_by('-id')
        notification_Length = notification_Db.objects.filter(doctor=request.user.id, status=None, sender=0).count()
        # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#
        doctor_profile_id = doctor_profile_db.objects.filter(doctor_profile_id=request.user.id)
        for doctor_profile_id in doctor_profile_id:
            book_appointment_list = patient_appointment_db.objects.filter(doctor=doctor_profile_id.id,confirm=1).order_by('-id')
    else:
        return HttpResponseRedirect('../login', locals())
    return render(request, "doctor-panel/appointment-list.html", locals())


def appointments_today(request):
    if request.user.is_staff == 1:
        # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#
        notification_List = notification_Db.objects.filter(doctor=request.user.id, sender=0).order_by('-id')
        notification_Length = notification_Db.objects.filter(doctor=request.user.id, status=None, sender=0).count()
        # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#
        doctor_list_id = doctor_profile_db.objects.filter(doctor_profile_id=request.user.id)
        for doctor_list_id in doctor_list_id:
            import datetime
            now = datetime.datetime.now()
            today_date = now.strftime("%m/%d/%Y")
            book_appointment_list = patient_appointment_db.objects.filter(doctor=doctor_list_id.id,date_of_appointment=today_date,confirm=1).order_by('-id')
    else:
        return HttpResponseRedirect('../login', locals())
    return render(request, 'doctor-panel/today-appointment-list.html', locals())


@login_required(login_url="login")
def appointment_Check(request, string):
    if request.user.is_staff == 1:
        doctor = doctor_profile_db.objects.filter(doctor_profile_id=request.user.id)
        for doctor in doctor:
            # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#
            notification_List = notification_Db.objects.filter(patient=request.user.id, status=None, sender=1).order_by(
                '-id')
            temp = []
            for i in notification_List:
                temp.append(i.id)
            notification_Length = len(temp)
            # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#
            # print string
            if string != None:
                status, id = smart_str(string).split('__')
                if patient_appointment_db.objects.filter(id=id):
                    patient_appointment_db.objects.filter(id=id).update(status=status)
            if smart_str(string).startswith('accept'):
                patient_appointment = patient_appointment_db.objects.filter(id=id)
                for i in patient_appointment:
                    patient_id = i.patient
                import datetime
                now = datetime.datetime.now()
                date = now.strftime("%m/%d/%Y")
                time = now.strftime("%H:%M")
                object_notify = notification_Db()
                object_notify.time = time
                object_notify.date = date
                object_notify.patient = patient_id
                object_notify.doctor = request.user.id
                object_notify.notification = "Your Appointment has been accepted"
                object_notify.sender = 1
                object_notify.save()

                if User.objects.all():
                    doctor_name_List = User.objects.filter(id=request.user.id)

                patient_New_List = User.objects.get(id=patient_id.id)
                patient_email = patient_New_List.email
                d = ({'email': patient_email, 'patient_appointment_List': patient_appointment,
                      'doctor_name_List': doctor_name_List})
                plaintext = get_template('email.txt')
                htmly = get_template('frontpanel-template/RequestAccepted.html')
                subject, from_email, to = 'Congratulations,Your Appointment has been approved', settings.DEFAULT_FROM_EMAIL, patient_email
                text_content = plaintext.render(d)
                html_content = htmly.render(d)
                msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
                msg.attach_alternative(html_content, "text/html")
                msg.send()

            elif smart_str(string).startswith('decline'):
                patient_appointment = patient_appointment_db.objects.filter(id=id)
                for i in patient_appointment:
                    patient_id = i.patient
                import datetime
                now = datetime.datetime.now()
                date = now.strftime("%m/%d/%Y")
                time = now.strftime("%H:%M")
                object_notify = notification_Db()
                object_notify.time = time
                object_notify.date = date
                object_notify.patient = patient_id
                object_notify.doctor = request.user.id
                object_notify.notification = "Sorry,Your Appointment has been declined"
                object_notify.sender = 1
                object_notify.save()

                if User.objects.all():
                    doctor_name_List = User.objects.filter(id=request.user.id)

                patient_New_List = User.objects.get(id=patient_id.id)
                patient_email = patient_New_List.email
                d = ({'email': patient_email, 'patient_appointment_List': patient_appointment,
                      'doctor_name_List': doctor_name_List})
                plaintext = get_template('email.txt')
                htmly = get_template('frontpanel-template/decline.html')
                subject, from_email, to = 'Sorry,Your Appointment has been declined', settings.DEFAULT_FROM_EMAIL, patient_email
                text_content = plaintext.render(d)
                html_content = htmly.render(d)
                msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
                msg.attach_alternative(html_content, "text/html")
                msg.send()
            elif smart_str(string).startswith('reschedule'):
                patient_appointment = patient_appointment_db.objects.filter(id=id)
                for i in patient_appointment:
                    patient_id = i.patient

                import datetime
                now = datetime.datetime.now()
                date = now.strftime("%m/%d/%Y")
                time = now.strftime("%H:%M")
                object_notify = notification_Db()
                object_notify.time = time
                object_notify.date = date
                object_notify.patient = patient_id
                object_notify.doctor = request.user.id
                object_notify.notification = "Please Rescheduled your Appointment....!!!"
                object_notify.sender = 1
                object_notify.save()

            return redirect('../appointment-list', locals())
        else:
            return HttpResponseRedirect('../login', locals())


@login_required(login_url="login")
def appointment_accept(request):
    if request.user.is_staff == 1:
        doctor_list_id = doctor_profile_db.objects.filter(doctor_profile_id=request.user.id)
        for doctor_list_id in doctor_list_id:
            print(doctor_list_id.id)
            book_appointment_list = patient_appointment_db.objects.filter(doctor=doctor_list_id.id, status='accept',confirm=1).order_by('-id')

            # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#
            notification_List = notification_Db.objects.filter(doctor=request.user.id, status=None, sender=0).order_by(
                '-id')
            notification_Length = notification_Db.objects.filter(doctor=request.user.id, status=None, sender=0).count()
            # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#
    else:
        return HttpResponseRedirect('../login', locals())
    return render(request, "doctor-panel/appointment-list.html", locals())


@login_required(login_url="login")
def appointment_decline(request):
    if request.user.is_staff == 1:
        doctor_list_id = doctor_profile_db.objects.filter(doctor_profile_id=request.user.id)
        for doctor_list_id in doctor_list_id:
            book_appointment_list = patient_appointment_db.objects.filter(doctor=doctor_list_id.id, status='decline',
                                                                          treatment=None,confirm=1).order_by('-id')
            # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#
            notification_List = notification_Db.objects.filter(doctor=request.user.id, status=None, sender=0).order_by(
                '-id')
            notification_Length = notification_Db.objects.filter(doctor=request.user.id, status=None, sender=0).count()
            # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#
    else:
        return HttpResponseRedirect('../login', locals())
    return render(request, "doctor-panel/appointment-list.html", locals())


@login_required(login_url="login")
def add_to_patlist(request, string):
    if request.user.is_staff == 1:
        # print string
        patient_appointment_db.objects.filter(doctor=request.user.id, id=smart_str(string)).update(
            treatment='Under_Treatment')
        return redirect('../appointment-accept/')
    else:
        return HttpResponseRedirect('../login', locals())


@login_required(login_url="login")
def remove_from_patlist(request, string):
    # print string
    if request.user.is_staff == 1:
        patient_appointment_db.objects.filter(doctor=request.user.id, id=smart_str(string)).update(
            treatment='Treatment_Done')
        return redirect('../patient-list/')
    else:
        return HttpResponseRedirect('../login', locals())


# <-----------------appointment forms------------------------->

@login_required(login_url="login")
def appointmente_delete(request, appoitment_id):
    if request.user.is_staff == 1:
        emp = patient_appointment_db.objects.get(id=appoitment_id)
        emp.delete()
        messages.error(request, 'appointment was succesfully delete')
    else:
        return HttpResponseRedirect('../login', locals())

    return HttpResponseRedirect('../appointment-list', locals())


# <------------------------------end appoitment forms------------------------------->


@login_required(login_url="login")
def patient_list(request):
    if request.user.is_staff == 1:
        doctor_list_id = doctor_profile_db.objects.filter(doctor_profile_id=request.user.id)
        for doctor_list_id in doctor_list_id:
        # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#
            notification_List = notification_Db.objects.filter(doctor=request.user.id, status=None, sender=0).order_by(
                '-id')
            notification_Length = notification_Db.objects.filter(doctor=request.user.id, status=None, sender=0).count()
            # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#
            doctor_patient_list = patient_appointment_db.objects.filter(doctor=doctor_list_id.id, status='accept').order_by('-id')


    else:
        return HttpResponseRedirect('../login', locals())
    return render(request, "doctor-panel/patient-list.html", locals())


@login_required(login_url="login")
def patient_profile(request, patient_id):
    if request.user.is_staff == 1:
        # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#
        notification_List = notification_Db.objects.filter(doctor=request.user.id, status=None, sender=0).order_by(
            '-id')
        notification_Length = notification_Db.objects.filter(doctor=request.user.id, status=None, sender=0).count()
        # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#
        patient_appointment_list = patient_appointment_db.objects.filter(id=patient_id)
        for i in patient_appointment_list:
            patient_NEW_ID = i.patient

        patient_Data_list = user_db.objects.filter(user_id=patient_NEW_ID)
        report_list = reports_Db.objects.filter(appointment_id=patient_id)
    else:
        return HttpResponseRedirect('../login', locals())
    return render(request, "doctor-panel/patient-profile.html", locals())


@login_required(login_url="login")
def add_report(request):
    import datetime
    now = datetime.datetime.now()
    if request.user.is_staff == 1:
        if request.method == "POST":
            appointment_id = request.POST.get("appointment_id", "")
            patient_id = request.POST.get("patient", "")
            doctor_id = request.POST.get("doctor_id", "")
            disease = request.POST.get("disease", "")
            patient = User.objects.get(id=patient_id)
            prescription = request.POST.get("prescription", "")

            new_book = reports_Db()
            new_book.appointment_id = appointment_id
            new_book.patient = patient
            new_book.disease = disease
            new_book.prescription = prescription
            new_book.doctor_id = doctor_id
            new_book.date = now.strftime("%Y-%B-%d")
            new_book.save()
            saved = True

            import datetime
            now = datetime.datetime.now()
            date = now.strftime("%m/%d/%Y")
            time = now.strftime("%H:%M")
            object_notify = notification_Db()
            object_notify.time = time
            object_notify.date = date
            object_notify.patient = patient
            object_notify.doctor = doctor_id
            object_notify.notification = "Check your Reports on the Report Lists"
            object_notify.sender = 1
            object_notify.save()

            if User.objects.all():
                doctor_name_List = User.objects.filter(id=request.user.id)

            patient_New_List = User.objects.get(id=patient_id)
            patient_email = patient_New_List.email
            d = ({'patient_New_List': patient_New_List, 'doctor_name_List': doctor_name_List,
                  'disease': disease, 'prescription': prescription})
            plaintext = get_template('email.txt')
            htmly = get_template('aivaid_Mail/patient-report.html')
            subject, from_email, to = 'Check your Reports on the Report Lists', \
                                      settings.DEFAULT_FROM_EMAIL, patient_email
            text_content = plaintext.render(d)
            html_content = htmly.render(d)
            msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
            msg.attach_alternative(html_content, "text/html")
            msg.send()

        else:
            return render(request, "doctor-panel/add-report.html", locals())
    else:
        return HttpResponseRedirect('../login', locals())

    return HttpResponseRedirect("../patient-profile/" + appointment_id, locals())


@login_required(login_url="login")
def patient_report(request):
    if request.user.is_staff == 1:
        patient_report_list = doctor_patient_report.objects.filter(doctor_profile_id=request.user.id)
        # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#
        notification_List = notification_Db.objects.filter(doctor=request.user.id, status=None, sender=0).order_by(
            '-id')
        notification_Length = notification_Db.objects.filter(doctor=request.user.id, status=None, sender=0).count()
        # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#
    else:
        return HttpResponseRedirect('../login', locals())

    return render(request, "doctor-panel/patient-report.html", locals())


@login_required(login_url="login")
def report_update(request, id):
    if request.user.is_staff == 1:
        patient_list = doctor_patient_db.objects.filter(doctor_profile_id=request.user.id)
        disease_list = disease_db.objects.all()
        if request.method == "POST":
            Disease = request.POST.get("Disease", "")
            doctor_patient_id = request.POST.get("doctor_patient_id", "")
            doctor_patient_id = doctor_patient_db.objects.get(id=doctor_patient_id)
            Disease = disease_db.objects.get(id=Disease)
            doctor_id = User.objects.get(id=request.user.id)
            instance = get_object_or_404(doctor_patient_report, id=id)

            MyForm = doctor_patient_report_form(request.POST, instance=instance)
            if MyForm.is_valid():
                new_book = MyForm.save(commit=False)  # Don't save it yet
                new_book.doctor_profile_id = doctor_id
                new_book.Disease = Disease
                new_book.doctor_patient_id = doctor_patient_id
                new_book.save()
                saved = True
                return HttpResponseRedirect('../patient-report', locals())

        else:
            MyForm = doctor_patient_report_form()
            update_list = doctor_patient_report.objects.filter(id=id)

            patient_list = doctor_patient_db.objects.filter(doctor_profile_id=request.user.id)
            disease_list = disease_db.objects.all()
            return render(request, "doctor-panel/report-update.html", locals())

    else:
        return HttpResponseRedirect('../login', locals())

    return render(request, "doctor-panel/report-update.html", locals())


@login_required(login_url="login")
def report_update_save(request):
    if request.user.is_staff == 1:
        patient_list = doctor_patient_db.objects.filter(doctor_profile_id=request.user.id)
        disease_list = disease_db.objects.all()
        if request.method == "POST":
            id = request.POST.get("id", "")

            Disease = request.POST.get("Disease", "")
            doctor_patient_id = request.POST.get("doctor_patient_id", "")
            doctor_patient_id = doctor_patient_db.objects.get(id=doctor_patient_id)
            Disease = disease_db.objects.get(id=Disease)
            doctor_id = User.objects.get(id=request.user.id)
            instance = get_object_or_404(doctor_patient_report, id=id)

            MyForm = doctor_patient_report_form(request.POST, instance=instance)
            if MyForm.is_valid():
                new_book = MyForm.save(commit=False)  # Don't save it yet
                new_book.doctor_profile_id = doctor_id
                new_book.Disease = Disease
                new_book.doctor_patient_id = doctor_patient_id
                new_book.save()
                saved = True
        else:
            MyForm = doctor_patient_report_form()
            patient_list = doctor_patient_db.objects.filter(doctor_profile_id=request.user.id)
            disease_list = disease_db.objects.all()
            return render(request, "doctor-panel/add-report.html", locals())



    else:
        return HttpResponseRedirect('../login', locals())

    return render(request, "doctor-panel/add-report.html", locals())


@login_required(login_url="login")
def doctor_profile(request):
    if request.user.is_staff == 1:
        total = 0

        user_table_list = User.objects.filter(id=request.user.id)
        review_list_count = review_db.objects.filter(doctor_profile_id=request.user.id).count()
        review_list_5 = review_db.objects.filter(doctor_profile_id=request.user.id, rating1='5').count()
        review_list_4 = review_db.objects.filter(doctor_profile_id=request.user.id, rating1='4').count()
        review_list_3 = review_db.objects.filter(doctor_profile_id=request.user.id, rating1='3').count()
        review_list_2 = review_db.objects.filter(doctor_profile_id=request.user.id, rating1='2').count()
        review_list_1 = review_db.objects.filter(doctor_profile_id=request.user.id, rating1='1').count()
        if review_list_count:

            review_list_avrage = ( 5 * review_list_5 + 4 * review_list_4 + 3 * review_list_3 + 2 * review_list_2 + 1 * review_list_1) / review_list_count
        else:
            review_list_avrage = 0
        profile_list = doctor_profile_db.objects.filter(doctor_profile_id=request.user.id)
        for i in profile_list:
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
        # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#
        notification_List = notification_Db.objects.filter(doctor=request.user.id, status=None, sender=0).order_by(
            '-id')
        notification_Length = notification_Db.objects.filter(doctor=request.user.id, status=None, sender=0).count()
        # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#
    else:
        return HttpResponseRedirect('../login', locals())
    return render(request, "doctor-panel/doctor-profile.html", locals())




import random
# import urllib # Python URL functions
# import urllib.request




@login_required(login_url="login")
def mobile_verify_doctor(request):
    if request.method == "POST":
        doctor_id = User.objects.get(id=request.user.id)
        if doctor_profile_db.objects.filter(doctor_profile_id=doctor_id.id):
            instance = get_object_or_404(doctor_profile_db, doctor_profile_id=doctor_id.id)

            mobile =smart_str(request.POST.get("mobile", ""))
            print('=======================',mobile)
            abc = smart_str(random.randint(000000,999999))

            instance.otp =abc
            instance.mobile_verify =0
            instance.umobile=mobile
            instance.save()
            abc = 'Your Mobile number Verification code for AIVAID is : ' +abc

            url= "http://sms.smslab.in/api/sendhttp.php?authkey=231573AVIY1Y3q155b71e024&mobiles="+ mobile + "&message= " +abc + "&sender=Aivaid&route=4&country=91"


            response = urllib.request.urlopen(url)
            output = response.read()  # Get Response
            # return 'ok'


        return render(request, "doctor-panel/otp_time.html", locals())



@login_required(login_url="login")
def resend_otp_verify_doctor(request):
        doctor_id = User.objects.get(id=request.user.id)
        if doctor_profile_db.objects.filter(doctor_profile_id=doctor_id.id):
            instance = get_object_or_404(doctor_profile_db, doctor_profile_id=doctor_id.id)
            mobile =instance.umobile
            print('=======================',mobile)
            abc = smart_str(random.randint(000000,999999))
            instance.otp =abc
            instance.mobile_verify =0
            instance.umobile=mobile
            instance.save()
            abc = 'Your Mobile number Verification code for AIVAID is : ' +abc
            url= "http://sms.smslab.in/api/sendhttp.php?authkey=231573AVIY1Y3q155b71e024&mobiles="+ mobile + "&message= " +abc + "&sender=Aivaid&route=4&country=91"
            response = urllib.request.urlopen(url)
            output = response.read()  # Get Response
        return render(request, "doctor-panel/otp_time.html", locals())

        # return render(request, "doctor-panel/otp_time_resend.html", locals())



@login_required(login_url="login")
def otp_verify_doctor(request):
    if request.method == "POST":
        doctor_id = User.objects.get(id=request.user.id)
        if doctor_profile_db.objects.filter(doctor_profile_id=doctor_id.id):
            otp =request.POST.get("otp", "")
            time =request.POST.get("time", "")

            print('+++++++++++',time)
            if time != '000':
                instance = get_object_or_404(doctor_profile_db, doctor_profile_id=doctor_id.id)
                if instance.otp == otp:
                    instance.mobile_verify =1
                    instance.save()
                    messages = 1

                else:
                    messages = 0
                    return render(request, "doctor-panel/otp_message.html", locals())
                return render(request, "doctor-panel/otp_message.html", locals())
            else:
                messages = 2
                return render(request, "doctor-panel/otp_message.html", locals())


@login_required(login_url="login")
def edit_doctor_profile(request, doctor_id):
    if request.user.is_staff == 1:
        # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#
        notification_List = notification_Db.objects.filter(doctor=request.user.id, status=None, sender=0).order_by(
            '-id')
        notification_Length = notification_Db.objects.filter(doctor=request.user.id, status=None, sender=0).count()
        # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#

        user_table_list = User.objects.filter(id=doctor_id)
        profile_list = doctor_profile_db.objects.filter(doctor_profile_id=doctor_id)
    else:
        return HttpResponseRedirect('../login', locals())

    return render(request, "doctor-panel/edit-profile.html", locals())


@login_required(login_url="login")
def save_doctor_profile_edit_data(request):
    if request.user.is_staff == 1:
        # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#
        notification_List = notification_Db.objects.filter(doctor=request.user.id, status=None, sender=0).order_by(
            '-id')
        notification_Length = notification_Db.objects.filter(doctor=request.user.id, status=None, sender=0).count()
        # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#
        if request.method == "POST":
            id = request.POST.get("id", "")
            doctor_id = User.objects.get(id=request.user.id)
            instance = get_object_or_404(User, id=id)
            MyForm = doctor_user_edit_profile_form(request.POST or None, instance=instance)
            MyForm.save()
            if doctor_profile_db.objects.filter(doctor_profile_id=id):
                instance = get_object_or_404(doctor_profile_db, doctor_profile_id=id)
                MyForm2 = doctor_profile_edit_form(request.POST or None, request.FILES or None, instance=instance)
                MyForm2.save()
            else:
                MyForm2 = doctor_profile_edit_form(request.POST or None, request.FILES)
                new_book = MyForm2.save(commit=False)  # Don't save it yet
                new_book.doctor_profile_id = doctor_id
                new_book.save()
                MyForm2.save()

            return HttpResponseRedirect('../doctor-profile', locals())
    else:
        return HttpResponseRedirect('../login', locals())
    return render(request, "doctor-panel/doctor-profile.html", locals())


def notice_list(request):
    return render(request, "doctor-panel/notice-list.html", locals())


def add_notice(request):
    return render(request, "doctor-panel/add-notice.html", locals())

@login_required(login_url="login")
def addservices(request):
    if request.user.is_staff == 1:
        # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#
        notification_List = notification_Db.objects.filter(doctor=request.user.id, status=None, sender=0).order_by(
            '-id')
        notification_Length = notification_Db.objects.filter(doctor=request.user.id, status=None, sender=0).count()
        # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#
        if request.method == "POST":
            discount = request.POST.get("discount", "")
            service = request.POST.get("service_name", "")
            price = request.POST.get("price", "")
            doctor_id = User.objects.get(id=request.user.id)
            object_Service = doctor_Services()
            object_Service.doctor = doctor_id
            object_Service.service = service
            object_Service.price = price
            object_Service.discount = discount
            object_Service.save()
            return HttpResponseRedirect('../serviceslist', locals())
    else:
        return HttpResponseRedirect('../login', locals())
    return render(request, "doctor-panel/addservices.html", locals())


def serviceslist(request):
    if request.user.is_staff == 1:
        # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#
        notification_List = notification_Db.objects.filter(doctor=request.user.id, status=None, sender=0).order_by(
            '-id')
        notification_Length = notification_Db.objects.filter(doctor=request.user.id, status=None, sender=0).count()
        # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#
        doctor_id = User.objects.get(id=request.user.id)
        if doctor_Services.objects.filter(doctor=doctor_id):
            doctor_Services_List = doctor_Services.objects.filter(doctor=doctor_id)
            return render(request, "doctor-panel/serviceslist.html", locals())

    else:
        return HttpResponseRedirect('../login', locals())
    return render(request, "doctor-panel/serviceslist.html", locals())


def report_list(request):
    return render(request, "doctor-panel/report-list.html", locals())


def transactions(request):
    instamojo_List = instamojo_payment_done.objects.filter(doctor_id=request.user.id).order_by('-id')

    return render(request, "doctor-panel/transaction.html", locals())




#-----------------------------------------------------------------------------------------------------------------------
@login_required(login_url="login")
def categorylist(request):
    if request.user.is_staff == 1:
        categories_data = categories.objects.all().order_by('-id')
        return render(request, 'doctor-panel/categorylist.html', locals())

    else:
        return HttpResponseRedirect('../../login', locals())


@login_required(login_url="login")
def category(request):
    if request.user.is_staff == 1:
        return render(request, 'doctor-panel/category.html')
    else:
        return HttpResponseRedirect('../../login', locals())


@login_required(login_url="login")
def savecategories(request):
    if request.user.is_staff == 1:
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
    if request.user.is_staff == 1:
        emp = categories.objects.get(id=uidb64)
        emp.delete()
        messages.success(request, 'Your Categories Delete successfully.')
        return HttpResponseRedirect('../categorylist', locals())
    else:
        return HttpResponseRedirect('../../login', locals())


def editcategory(request, uidb64):
    if request.user.is_staff == 1:
        categories_data = categories.objects.filter(id=uidb64)
        return render(request, 'doctor-panel/editcategory.html', locals())
    else:
        return HttpResponseRedirect('../../login', locals())


@login_required(login_url="login")
def saveeditcategories(request):
    if request.user.is_staff == 1:
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
    if request.user.is_staff == 1:
        bloglisting = blog.objects.filter(user=request.user.id).order_by('-id')
        return render(request, 'doctor-panel/Bloglist.html', locals())
    else:
        return HttpResponseRedirect('../../login', locals())


def Addblog(request):
    if request.user.is_staff == 1:
        categorieslisting = categories.objects.all()
        return render(request, 'doctor-panel/Addblog.html', locals())
    else:
        return HttpResponseRedirect('../../login', locals())


@login_required(login_url="login")
def Saveblog(request):
    if request.user.is_staff == 1:
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
    if request.user.is_staff == 1:
        emp = blog.objects.get(id=uidb64)
        emp.delete()
        messages.success(request, 'Your Blog Delete successfully.')
        return HttpResponseRedirect('../bloglist', locals())
    else:
        return HttpResponseRedirect('../../login', locals())


def editblog(request, uidb64):
    if request.user.is_staff == 1:
        categorieslisting = categories.objects.all()
        blog_list = blog.objects.filter(id=uidb64)
        return render(request, 'doctor-panel/editblog.html', locals())
    else:
        return HttpResponseRedirect('../../login', locals())


@login_required(login_url="login")
def saveeditblog(request):
    if request.user.is_staff == 1:
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
