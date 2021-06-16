# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views.decorators.csrf import csrf_exempt
import pandas as pd
from django.shortcuts import render, get_object_or_404
import numpy as np

from aivaid import settings
from aivaidapp.csv import load_csv
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from aivaidapp.pkl import question_number_point
from aivaidapp.prediction import predict_disease
from django.http import HttpResponse
from django.contrib.auth import login
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from superuser.models import blog, categories
from .tokens import account_activation_token
from django.core.mail import EmailMessage
from aivaidapp.form import accept_terms_form, \
    user_Form, Contact_db_Form, doctor_SignupForm, patient_appointment_form, PayForm, UserLoginForm, review_forms
from aivaidapp.models import user_db, doctor_profile_db, patient_appointment_db, notification_Db, instamojo_payment, \
    instamojo_payment_done, clinic_details_db, doctor_Services, clinic_pic_db, review_db
import uuid

from django.utils.encoding import smart_str
from aivaid.settings import BASE_DIR
from django.contrib import messages, auth
from django.contrib.auth import authenticate
from django.contrib.auth.models import User

from django.core.urlresolvers import reverse
from django.shortcuts import render, redirect, HttpResponseRedirect
from django.template.context_processors import csrf
from django.contrib.auth.decorators import login_required

from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import render, redirect
from aivaidapp.instamojo_wrapper import Instamojo
import datetime

API_KEY = '6086345522f244ba5aca84e9ce5236a5'
AUTH_TOKEN = 'ded1e149a4c9ee3e41e7f8dd79304bfe'
api = Instamojo(api_key=API_KEY, auth_token=AUTH_TOKEN, endpoint='https://www.instamojo.com/api/1.1/')

from rest_framework.response import Response


def setlanguage(request):
    return render(request, 'set-language.html',
                  {'LANGUAGES': settings.LANGUAGES, 'SELECTEDLANG': request.LANGUAGE_CODE})


from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.utils.translation import LANGUAGE_SESSION_KEY
from django.utils import translation


def corona(request):
    return render(request,'corona.html')


def switch_language(request):
    """
    Switch the LANGUAGE_SESSION_KEY in request object from 'tl' to 'en' or 'en' to 'tl'

    Args:
        request (obj) : HttpRequest object

    Returns:
        The request object with its LANGUAGE_SESSION_KEY switched to whichever language was not used
    """
    if request.session[LANGUAGE_SESSION_KEY] == "tl":
        request.session[LANGUAGE_SESSION_KEY] = "en"
        translation.activate("en")
    elif request.session[LANGUAGE_SESSION_KEY] == "en":
        request.session[LANGUAGE_SESSION_KEY] = "tl"
        translation.activate("tl")

    return request



def handler(request, *args, **argv):
    return render(request, "404error.html", locals())


def handler50(request):
    return render(request, "404error.html", locals())



def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            if request.user.is_staff == 0:
                return redirect('../dashboard-patient')
            else:
                return redirect('../doctor-panel')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'password/change_password.html', {
    'form': form
    })













def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        user.backend = 'django.contrib.auth.backends.ModelBackend'
        login(request, user)
        register_send_mails(request.user.email)

        if request.user.is_staff == 1:
            return redirect(reverse('doctor-panel'))
        else:
            return redirect(reverse('start-checkup'))
    else:
        return HttpResponse('Activation link is invalid!')


def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            email = request.POST['email']
            password = request.POST['password']
            try:
                username = User.objects.get(email=email.lower()).username
                user = authenticate(username=username, password=password)
            except:
                user = None
                # messages.error(request, "Your email or password was not recognised")

            if user is not None:
                auth.login(request, user)
                messages.error(request, "You have successfully logged in")
                if request.GET and 'next' in request.GET:
                    next = request.GET['next']
                    return HttpResponseRedirect(next)
                else:
                    if request.user.is_staff == 1:
                        return redirect(reverse('doctor-panel'))
                    else:
                        return redirect(reverse('start-checkup'))
            else:
                messages.error(request, "Your email or password was not recognised")

                # form.add_error(None, "")

    else:
        # this handles the initial get request
        # return a blank form for user to login
        form = UserLoginForm()

    # prepare args to pass to render function
    #   form:   this is the form which will be rendered to html (UserLoginForm)
    #   next:   if the url of the request included a next query string '?next=' pass it to the form
    #           so that it can be included in the url when the form is resubmitted
    #           see handling of post method: next = request.GET['next']
    args = {'form': form, 'next': request.GET['next'] if request.GET and 'next' in request.GET else ''}
    args.update(csrf(request))
    return render(request, 'login.html', args)


def register_send_mails(emails):
    d = ({'email': emails})
    plaintext = get_template('email.txt')
    htmly = get_template('frontpanel-template/signup-template.html')
    subject, from_email, to = 'Welcome To Aivaid', settings.DEFAULT_FROM_EMAIL, emails
    text_content = plaintext.render(d)
    html_content = htmly.render(d)
    msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
    msg.attach_alternative(html_content, "text/html")
    msg.send()


def send_subscription(request):
    if request.method == 'POST':
        email_Subscribe = request.POST.get('email_Subscribe', '')
        d = ({'email': email_Subscribe})
        plaintext = get_template('email.txt')
        htmly = get_template('frontpanel-template/Suscribe-temlate.html')
        subject, from_email, to = 'Thanks for Subscription!!!', settings.DEFAULT_FROM_EMAIL, email_Subscribe
        text_content = plaintext.render(d)
        html_content = htmly.render(d)
        msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
        msg.attach_alternative(html_content, "text/html")
        msg.send()
        return HttpResponseRedirect('../')
    else:
        return HttpResponseRedirect('../')


def register(request):
    if request.method == 'POST':
        form = doctor_SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            to_email = form.cleaned_data.get('email')
            current_site = get_current_site(request)
            # mail_subject = 'Activate your  account.'
            # message = render_to_string('frontpanel-template/acc_active_email.html', {
            #     'user': user,
            #     'domain': current_site.domain,
            #     'uid': urlsafe_base64_encode(force_bytes(user.pk)),
            #     'token': account_activation_token.make_token(user),
            # })
            # email = EmailMessage(
            #     mail_subject, message, to=[to_email]
            # )
            # email.send()
            d = ({
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            plaintext = get_template('email.txt')
            htmly = get_template('frontpanel-template/acc_active_email.html')
            subject, from_email, to = 'Welcome To Aivaid', settings.DEFAULT_FROM_EMAIL, to_email
            text_content = plaintext.render(d)
            html_content = htmly.render(d)
            msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
            msg.attach_alternative(html_content, "text/html")
            msg.send()

            return render(request, "account-verify.html", locals())

    else:
        form = doctor_SignupForm()
    return render(request, "signup.html", {'MyForm': form})


def patient_password_reset(request):
    return render(request, "patient/patient-password-reset.html")


# from django.contrib.gis.geoip import GeoIP


def index(request):
    if request.method == 'POST':
        request = switch_language(request)
    else:
        request.session[LANGUAGE_SESSION_KEY] = "en"
        translation.activate("en")

    return render(request, "index.html")


def start_checkup(request):
    if request.method == "POST":
        MyForm = accept_terms_form(request.POST)
        if MyForm.is_valid():
            MyForm = MyForm.save(commit=False)
            my_uuid = uuid.uuid4()
            MyForm.user_id = smart_str(my_uuid)
            request.session['user_id'] = smart_str(my_uuid)
            MyForm.save()
            return HttpResponseRedirect('../patient')
    else:
        MyForm = accept_terms_form()
    return render(request, "start-checkup.html", locals())


def patient(request):
    if request.method == "POST":
        user_id = request.session['user_id']
        if user_db.objects.filter(user_id=user_id):
            instance = get_object_or_404(user_db, user_id=user_id)
            first_name = request.POST.get("first_name", "")
            age = request.POST.get("Years", "")
            state = request.POST.get("state", "")
            city = request.POST.get("city", "")
            gender = request.POST.get("gender", "")
            height_cm = request.POST.get("height", "")
            height_feet = request.POST.get("htf", "") + '.' + request.POST.get("hti", "")
            weight = request.POST.get("weight", "")
            body_mass_index = request.POST.get("bmi", "")
            results = request.POST.get("interp", "")
            request.session['gender'] = gender
            abc = instance
            abc.user_id = user_id
            abc.first_name = first_name
            abc.state = state
            abc.city = city
            abc.weight = weight
            abc.height_cm = height_cm
            abc.height_feet = height_feet
            abc.age = age
            abc.gender = gender
            abc.body_mass_index = body_mass_index
            abc.results = results
            abc.save()
            if gender == "male":
                return HttpResponseRedirect('../male')
            elif gender == "female":
                return HttpResponseRedirect('../female')
        else:

            first_name = request.POST.get("first_name", "")
            age = request.POST.get("Years", "")
            state = request.POST.get("state", "")
            city = request.POST.get("city", "")
            gender = request.POST.get("gender", "")
            height_cm = request.POST.get("height", "")
            height_feet = request.POST.get("htf", "") + request.POST.get("hti", "")
            weight = request.POST.get("weight", "")
            body_mass_index = request.POST.get("bmi", "")
            results = request.POST.get("interp", "")
            request.session['gender'] = gender
            abc = user_db()
            abc.user_id = user_id
            abc.first_name = first_name
            abc.state = state
            abc.city = city
            abc.weight = weight
            abc.height_cm = height_cm
            abc.height_feet = height_feet
            abc.age = age
            abc.gender = gender
            abc.body_mass_index = body_mass_index
            abc.results = results
            abc.save()
            if gender == "male":
                return HttpResponseRedirect('../male')
            elif gender == "female":
                return HttpResponseRedirect('../female')
                # ##print request.session['user_id']
    else:
        MyForm = user_Form()
    return render(request, "patient.html", locals())


def symtoms(request):
    if request.method == "POST":
        user_id = request.session['user_id']
        your_symptoms = request.POST.get("your_symptoms", "")
        your_symptoms = your_symptoms.split(',')
        your_symptoms = (smart_str(your_symptoms[0]))
        your_symptoms = your_symptoms.rstrip(' ')
        instance = get_object_or_404(user_db, user_id=user_id)
        request.session['selected_disease'] = your_symptoms
        abc = instance
        abc.your_symptoms = your_symptoms
        abc.save()
        return HttpResponseRedirect('../locations')
    elif "male" == request.session['gender']:
        return HttpResponseRedirect('../male')
    else:
        return HttpResponseRedirect('../female')
    return render(request, "symtoms.html")


def male(request):
    return render(request, "male.html")


def female(request):
    return render(request, "female.html")


def locations(request):
    if request.method == "POST":
        user_id = request.session['user_id']
        visitedLocations = request.POST.get("visitedLocations", "")
        visitedLocations = visitedLocations.split(',')
        visitedLocations = smart_str(visitedLocations[0])
        instance = get_object_or_404(user_db, user_id=user_id)
        abc = instance
        abc.Recently_Visited_Locations = visitedLocations
        abc.save()
        return HttpResponseRedirect('../question')
    else:
        abc = ''
    return render(request, "location.html")


def question(request):
    xyz = request.session['selected_disease']
    request.session['mylist'] = load_csv(xyz)
    print(request.session['mylist'])
    for i in request.session['mylist']:
        print(i)
        print(len(i))
    request.session['once'] = 0
    request.session['question_number'] = 0
    abc = request.session['mylist'][0][0]
    return render(request, 'questions.html', {'listJinja_All': abc})


@csrf_exempt
def questions(request):
    if request.method == "POST":
        request.session['question_point'] = 0
        if request.session['once'] == 0:
            request.session['count_question'] = 0
            request.session['count_list'] = 0
            request.session['question_number'] = 0
            request.session['question_index'] = question_number_point(request.session['selected_disease'])
            list_answer_main = []
            len_list = []
            for zxx in range(len(request.session['mylist'])):
                qws1 = request.session['mylist'][zxx]
                qws1 = pd.DataFrame(qws1)
                len_list.append(len(qws1))
            request.session['len_list'] = len_list
            for i in range(len(request.session['len_list'])):
                list_answer = []
                for j in range(np.sum(len_list)):
                    list_answer.append(0)
                list_answer_main.append(list_answer)
            request.session['list_answer_main'] = list_answer_main
            del list_answer_main
            del len_list

            request.session['once'] = request.session['once'] + 1
        change = 0
        try:
            ajax_answer = request.POST.get('radio_name', '')
            if ajax_answer == '0' or ajax_answer == '1':
                print()
            else:
                return render(request, 'question1.html',
                              {'listJinja_All': request.session['mylist'][request.session['count_list']][
                                  request.session['count_question']],
                               'message': "Please select the one of the following option.", 'change': change})

        except Exception as e:
            pass
        else:
            ajax_answer = int(ajax_answer)

            if ajax_answer == 1:

                if len(request.session['mylist']) - 1 == request.session['count_list'] and len(
                        request.session['mylist'][request.session['count_list']]) - 1 == request.session[
                    'count_question'] - 1:
                    return render(request, 'disease-results.html')

                if len(request.session['mylist'][request.session['count_list']]) == request.session[
                    'count_question'] + 1:

                    request.session['list_answer_main'][request.session['count_list']][
                        request.session['question_number']] = 1

                    request.session['question_point'] = 1

                    if len(request.session['mylist']) - 1 == request.session['count_list'] and len(
                            request.session['mylist'][request.session['count_list']]) == request.session[
                        'count_question'] + 1:
                        return render(request, 'check-results.html')
                        # return HttpResponseRedirect('../result/', locals())

                    request.session['count_list'] = request.session['count_list'] + 1
                    request.session['count_question'] = 0
                    request.session['question_number'] = request.session['question_index'][
                        request.session['count_list'] - 1]

                if request.session['question_point'] == 0:
                    request.session['list_answer_main'][request.session['count_list']][
                        request.session['question_number']] = 1
                    request.session['question_number'] = request.session['question_number'] + 1
                    request.session['count_question'] = request.session['count_question'] + 1


            elif ajax_answer == 0:

                if len(request.session['mylist']) - 1 == request.session['count_list']:

                    return render(request, 'check-results.html')
                    # return HttpResponseRedirect('../result/', locals())

                request.session['count_list'] = request.session['count_list'] + 1
                request.session['count_question'] = 0
                request.session['question_number'] = request.session['question_index'][
                    request.session['count_list'] - 1]

    return render(request, 'question1.html', {
        'listJinja_All': request.session['mylist'][request.session['count_list']][request.session['count_question']],
        'change': change})


def check_results(request):
  #  for i in request.session['list_answer_main']:
   #     print(i)
    #    print(len(i))
    print(request.session['list_answer_main'])
    pred = predict_disease(request, request.session['list_answer_main'])
    doctor_list = doctor_profile_db.objects.all()
    review_list = review_db.objects.all()
    pic_list = clinic_pic_db.objects.all()
    return render(request, "result.html", locals())


def send_mails(request):
    if request.method == "POST":
        email = request.POST.get('email_id', '')
        d = ({'email': email})
        plaintext = get_template('email.txt')
        htmly = get_template('frontpanel-template/report.html')
        subject, from_email, to = 'Welcome To Aivaid', settings.DEFAULT_FROM_EMAIL, email
        text_content = plaintext.render(d)
        html_content = htmly.render(d)
        msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
        msg.attach_alternative(html_content, "text/html")
        attachment = open(BASE_DIR + "/static/pdf_folder/" + smart_str(request.session['id']) + ".pdf", 'rb')
        msg.attach("health-report.pdf", attachment.read(), 'application/pdf')
        msg.send()
        request.session.modified = True
        return HttpResponseRedirect('/', locals())
    else:
        return HttpResponseRedirect('/')



@login_required(login_url="login")
def book_appointment_pat(request):
    # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#
    user_db_Data = user_db.objects.filter(auth_user_id=request.user.id)
    notification_List = notification_Db.objects.filter(patient=request.user.id, status=None, sender=1).order_by(
        '-id')
    notification_Length = notification_Db.objects.filter(patient=request.user.id, status=None, sender=1).count()
    # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#
    msg = ''
    # ++++++++++++++++++++++++++++++===========+++++++++++++++++++++++++++++++++#
    doctor_List = []
    if doctor_profile_db.objects.all():
        doctor_List = doctor_profile_db.objects.all()
    if request.method == "POST":
        clinic = request.POST.get('clinic', '')
        doctor = request.POST.get('doctor', '')
        doctor = doctor_profile_db.objects.get(id=doctor)
        patient_id = User.objects.get(id=request.user.id)
        clinic = clinic_details_db.objects.get(id=clinic)
        MyForm = patient_appointment_form(request.POST or None, request.FILES)
        if MyForm.is_valid():
            new_book = MyForm.save(commit=False)  # Don't save it yet
            new_book.patient = patient_id
            new_book.clinic = clinic
            new_book.doctor = doctor
            new_book.save()
            # print 'Success'
            saved = True

    #         patient = User.objects.get(id=request.user.id)
    #
    #         now = datetime.datetime.now()
    #         date = now.strftime("%m/%d/%Y")
    #         time = now.strftime("%H:%M")
    #         object_notify = notification_Db()
    #         object_notify.time = time
    #         object_notify.date = date
    #         object_notify.patient = patient
    #         object_notify.doctor = doctor.doctor_profile_id.id
    #         object_notify.notification = "You have new Appointment"
    #         object_notify.sender = 0
    #         object_notify.save()
    #
            first_name = request.POST.get('first_name', '')
            email = request.POST.get('email', '')
            mobile = request.POST.get('mobile', '')
            date_of_appointment = request.POST.get('date_of_appointment', '')
            start_time = request.POST.get('start_time', '')


            patient_appointment_List = patient_appointment_db.objects.filter(
                first_name=first_name,
                email=email, mobile=mobile,
                doctor=doctor, clinic=clinic,
                date_of_appointment=date_of_appointment,
                start_time=start_time
            )
            return render(request, "payment.html", locals())


    #         messages.success(request, 'Appointment booked sucessfully')
    #         msg = 'Success'
    #     else:
    #         messages.success(request, 'You already booked your Appointment to this Dr.')
    #         msg = 'Unsuccess'
    # # ++++++++++++++++++++++++++++++++==================+++++++++++++++++++++++++++++++#



    return HttpResponseRedirect('/doctordetail/' + doctor.doctor_profile_id.username)


def instamojo(request):
    if request.method == 'POST':
        print("\n\nPOST\n\n" + str(request.POST))
        # create a form instance and populate it with data from the request:
        form = PayForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            data = form.cleaned_data
            print(data)
            # Create a new Payment Request
            response = api.payment_request_create(
                amount=str(data['Amount']),
                purpose=data['Purpose'],
                send_email=True,
                send_sms=True,
                email=data['Email'],
                buyer_name=data['Name'],
                phone=data['Phone'],
                redirect_url=request.build_absolute_uri(reverse("list"))
            )
            obj = instamojo_payment()
            obj.name = data['Name']
            obj.email = data['Email']
            obj.amount = str(data['Amount'])
            obj.item_name = data['Purpose']
            obj.phone = data['Phone']
            obj.payment_request_id = response['payment_request']['id']
            obj.save()
            print(response)
            print(response['payment_request']['id'])

            # return HttpResponse(response)
            return HttpResponseRedirect(response['payment_request']['longurl'])

            # if a GET (or any other method) we'll create a blank form
    else:
        print("\n\nGET\n\n")
        form = PayForm()
        # form.fields['Amount'].clean(10)
        # form.fields['Amount']=10
        print("\n\n" + str(form) + "\n\n")

    return render(request, 'instamojo.html', {'form': form})
    # return HttpResponse("Hello, world. You're at the API TEST index.")


def list_payments(request):
    baseurl = request.get_full_path()
    payment_id = request.GET['payment_id']
    payment_request_id = request.GET['payment_request_id']
    print(payment_id, payment_request_id)
    response = api.payment_requests_list()
    # Loop over all of the payment requests
    # h = "<div><table><tr><th>ID</th><th>amount</th><th>Purpose</th><th>status</th></tr>"
    for payment_request in response['payment_requests']:
        item_name = payment_request['purpose']
        id = request.user.id
        id = str(id).replace('L', '')
        id = User.objects.get(id=id)
        a, appointment_id, doctor_id = item_name.split("_")
        obj = instamojo_payment_done()
        obj.name = payment_request['buyer_name']
        obj.email = payment_request['email']
        obj.amount = payment_request['amount']
        obj.item_name = item_name
        obj.payment_request_id = payment_request['id']
        obj.status = payment_request['status']
        obj.payment_id = payment_id
        obj.user_id = id
        obj.doctor_id = doctor_id
        obj.save()

        # print (a,appointment_id,c)
        # print ('hlooooooooooooooooooo')
        if patient_appointment_db.objects.filter(id=appointment_id):
            patient_appointment_db.objects.filter(id=appointment_id).update(payment='Paid')
            # appointment_list =patient_appointment_db.objects.filter(id=appointment_id)

        # h += "<tr>"
        # h += "<td>" + payment_request['id'] + "</td>"
        # h += "<td>" + payment_request['amount'] + "</td>"
        # h += "<td>" + payment_request['purpose'] + "</td>"
        # h += "<td>" + payment_request['status'] + "</td>"
        # h += "<td>" + payment_request['buyer_name'] + "</td>"
        # h += "<td>" + payment_request['email'] + "</td>"
        # # h += "<td>" + payment_request['phone'] + "</td>"
        # h += "</tr>"
        break
    # h += "</table></div>"
    return redirect("../confirm-appointment/" + appointment_id)


def pay_later(request, string):
    # if request.user.is_staff == 0:
    if smart_str(string) != None:
        patient_Id = User.objects.get(id=request.user.id)
        if patient_appointment_db.objects.filter(id=string):
            patient_appointment_db.objects.filter(id=string).update(payment='Unpaid')
            return HttpResponseRedirect('../confirm-appointment/' + string)






def confirm_appointment(request,uidb64):
    appointment_list= patient_appointment_db.objects.filter(id=uidb64)
    return render(request, "confirm-appointment.html", locals())


def confirm_appointment_save(request):
    if request.method == "POST":
        id = request.POST.get('id', '')
        first_name = request.POST.get('first_name', '')
        email = request.POST.get('email', '')
        mobile = request.POST.get('mobile', '')
        if patient_appointment_db.objects.filter(id=id):

            appointment_list_mail = patient_appointment_db.objects.filter(id=id)
            appointment_list = patient_appointment_db.objects.get(id=id)
            appointment_list.first_name= first_name
            appointment_list.email= email
            appointment_list.mobile= mobile
            appointment_list.confirm= 1
            appointment_list.save()
            if User.objects.all():
                doctors = User.objects.filter(is_staff=1)
            doctor_name_List = []
            for i in doctors:
                temp = []
                temp.append(smart_str(i.id))
                temp.append(smart_str(i.first_name))
                temp.append(smart_str(i.last_name))
                doctor_name_List.append(temp)

            doctor_New_List = User.objects.filter(id=appointment_list.doctor.doctor_profile_id.id)
            for i in doctor_New_List:
                doctor_email = i.email
                d = ({'email': doctor_email, 'patient_appointment_List': appointment_list_mail,
                      'doctor_name_List': doctor_name_List})
                plaintext = get_template('email.txt')
                htmly = get_template('frontpanel-template/bookappointment.html')
                subject, from_email, to = 'New Appointment', settings.DEFAULT_FROM_EMAIL, doctor_email
                text_content = plaintext.render(d)
                html_content = htmly.render(d)
                msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
                msg.attach_alternative(html_content, "text/html")
                msg.send()
    return HttpResponseRedirect('../appointment-success/' + id)


def appointment_success(request, uidb64):
    appointment_list = patient_appointment_db.objects.filter(id=uidb64)
    return render(request, "appointment-success.html", locals())


def contact_us(request):
    if request.method == "POST":
        MyForm = Contact_db_Form(request.POST)
        if MyForm.is_valid():
            name = MyForm.cleaned_data.get("name")
            email = MyForm.cleaned_data.get("email")
            mobile = MyForm.cleaned_data.get("mobile")
            message = MyForm.cleaned_data.get("message")
            MyForm.save()
            d = ({'email': email})
            plaintext = get_template('email.txt')
            htmly = get_template('frontpanel-template/contactus-template.html')
            subject, from_email, to = 'Contact Us For Aivaid', settings.DEFAULT_FROM_EMAIL, email
            text_content = plaintext.render(d)
            html_content = htmly.render(d)
            msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
            msg.attach_alternative(html_content, "text/html")
            msg.send()
            send_mail('Contact Us For Aivaid',
                      '\nName:' + name + '\nEmail:' + email + '\nMobile:' + mobile + '\nMessage:' + message,
                      settings.DEFAULT_FROM_EMAIL, [settings.DEFAULT_FROM_EMAIL], fail_silently=False)

    else:
        MyForm = Contact_db_Form()
    return render(request, "contactus.html", locals())


# <----------------------------------------Patient templates------------------------------------------>


def about_us(request):
    return render(request, "about-us.html")


def find_doctor(request):
    doctor_list = doctor_profile_db.objects.all()
    pic_list = clinic_pic_db.objects.all()
    review_list = review_db.objects.all()

    return render(request, "searchdoctor.html", locals())


def doctordetail(request, uidb64):
    list = User.objects.filter(username=uidb64)
    for list in list:
        doctor_list = doctor_profile_db.objects.filter(doctor_profile_id=list.id)
        clinic_list = clinic_details_db.objects.filter(doctor_profile_id=list.id)
        doctor_Services_List = doctor_Services.objects.filter(doctor=list.id)
        blog_List = blog.objects.filter(user=list.id)
        pic_list = clinic_pic_db.objects.filter(doctor_profile_id=list.id)
        review_list = review_db.objects.filter(doctor_profile_id=list.id).order_by('-id')[:5]
        review_list_count = review_db.objects.filter(doctor_profile_id=list.id).count()
        review_list_5 = review_db.objects.filter(doctor_profile_id=list.id,rating1='5').count()
        review_list_4 = review_db.objects.filter(doctor_profile_id=list.id,rating1='4').count()
        review_list_3 = review_db.objects.filter(doctor_profile_id=list.id,rating1='3').count()
        review_list_2 = review_db.objects.filter(doctor_profile_id=list.id,rating1='2').count()
        review_list_1 = review_db.objects.filter(doctor_profile_id=list.id,rating1='1').count()
        if review_list:

            review_list_avrage = (5 * review_list_5 + 4 * review_list_4 + 3 * review_list_3 + 2 * review_list_2 + 1 * review_list_1) / review_list_count
        else:
            review_list_avrage = 0
    return render(request, "doctordetail.html", locals())







def Review_feedback(request):
    if request.method == "POST":
        doctor_id = request.POST.get('doctor_id', '')
        doctor_id = User.objects.get(id=doctor_id)
        MyForm = review_forms(request.POST)
        if MyForm.is_valid():
            MyForm = MyForm.save(commit=False)
            MyForm.doctor_profile_id=doctor_id
            MyForm.save()
            return HttpResponseRedirect('../doctordetail/'+doctor_id.username)



def newcounsultation(request):
    doctor_list = doctor_profile_db.objects.all()
    return render(request, "newcounsultation.html", locals())


def doctor_full_profile(request, uidb64):
    doctor = User.objects.filter(username=uidb64)
    for doctor in doctor:
        doctor_list = doctor_profile_db.objects.filter(doctor_profile_id=doctor.id)
    return render(request, "doctor-profile.html", locals())


def for_doctor(request):
    return render(request, "for-doctor.html")


def patient_visitor_guide(request):
    return render(request, "patient-visitor.html")


def terms_conditions(request):
    return render(request, "terms-conditions.html")


def privacy(request):
    return render(request, "privacy-policy.html")


def blogs(request):
    bloglisting = blog.objects.all().order_by('-id')
    return render(request, "blogs.html", locals())


def blog_single(request, uidb64):
    single_blog = blog.objects.filter(slug=uidb64)
    bloglisting = blog.objects.all().order_by('-id')[:5]
    categories_data = categories.objects.all().order_by('-id')[:5]
    return render(request, "single-blog.html", locals())


#
# @login_required(login_url="login")
# def doctor_list_pat(request):
#     if request.user.is_staff == 0:
#         if user_db.objects.filter(user_id=request.user.id):
#             doctor_List = []
#             if doctor_profile_db.objects.all():
#                 doctor_List = doctor_profile_db.objects.all()
#
#             # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#
#             notification_List = notification_Db.objects.filter(patient=request.user.id, status=None, sender=1).order_by(
#                 '-id')
#             temp = []
#             for i in notification_List:
#                 temp.append(i.id)
#             notification_Length = len(temp)
#             # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#
#             return render(request, "patient-admin/doctor-list.html", locals())
#         else:
#             return redirect('../edit-pat-profile', {'message': 'PLease Fill the Profile First'})
#     else:
#         return HttpResponseRedirect('../login', locals())
#
#
# @login_required(login_url="login")
# def department_list_pat(request):
#     dept_List = []
#     if departments.objects.all():
#         dept_List = departments.objects.all()
#
#     # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#
#     notification_List = notification_Db.objects.filter(patient=request.user.id, status=None, sender=1).order_by('-id')
#     temp = []
#     for i in notification_List:
#         temp.append(i.id)
#     notification_Length = len(temp)
#     # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#
#     return render(request, "patient-admin/department-list.html", locals())
#
#
# @login_required(login_url="login")
# def appointment_list_pat(request):
#     if request.user.is_staff == 0:
#         if user_db.objects.filter(user_id=request.user.id):
#             doctor_List = []
#             if doctor_profile_db.objects.all():
#                 doctor_List = doctor_profile_db.objects.all()
#             doctor_Name_List = []
#             for i in doctor_List:
#                 temp = []
#                 temp.append(smart_str(i.doctor_profile_id.id))
#                 temp.append(smart_str(i.doctor_profile_id.first_name))
#                 temp.append(smart_str(i.doctor_profile_id.last_name))
#                 temp.append(smart_str(i.doctor_profile_id.email))
#                 doctor_Name_List.append(temp)
#             appointment_list = []
#             if patient_appointment_db.objects.filter(patient=request.user.id):
#                 appointment_list = patient_appointment_db.objects.filter(patient=request.user.id).order_by('-id')
#             # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#
#             notification_List = notification_Db.objects.filter(patient=request.user.id, status=None, sender=1).order_by(
#                 '-id')
#             temp = []
#             for i in notification_List:
#                 temp.append(i.id)
#             notification_Length = len(temp)
#             # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#
#             return render(request, "patient-admin/appointment-list.html", locals())
#         else:
#             return redirect('../edit-pat-profile', {'message': 'PLease Fill the Profile First'})
#     else:
#         return HttpResponseRedirect('../login', locals())
#
#

#
#
# @login_required(login_url="login")
# def total_reports_pat(request):
#     if request.user.is_staff == 0:
#         if user_db.objects.filter(user_id=request.user.id):
#             patient_id = User.objects.get(id=request.user.id)
#             if reports_Db.objects.filter(patient=patient_id):
#                 reports_List = reports_Db.objects.filter(patient=patient_id).order_by('-id')
#
#             # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#
#             notification_List = notification_Db.objects.filter(patient=request.user.id, status=None, sender=1).order_by(
#                 '-id')
#             temp = []
#             for i in notification_List:
#                 temp.append(i.id)
#             notification_Length = len(temp)
#             # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#
#             return render(request, "patient-admin/total-reports.html", locals())
#         else:
#             return redirect('../edit-pat-profile', {'message': 'PLease Fill the Profile First'})
#     else:
#         return HttpResponseRedirect('../login', locals())
#
#
# @login_required(login_url="login")
# def notice_list_pat(request):
#     if request.user.is_staff == 0:
#         if user_db.objects.filter(user_id=request.user.id):
#             if notification_Db.objects.filter(patient=request.user.id):
#                 all_notification_List = notification_Db.objects.filter(patient=request.user.id, sender=1).order_by(
#                     '-id')
#             if User.objects.all():
#                 doctors = User.objects.filter(is_staff=1)
#             doctor_List = []
#             for i in doctors:
#                 temp = []
#                 temp.append(smart_str(i.id))
#                 temp.append(smart_str(i.first_name))
#                 temp.append(smart_str(i.last_name))
#                 doctor_List.append(temp)
#             # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#
#             notification_List = notification_Db.objects.filter(patient=request.user.id, status=None, sender=1).order_by(
#                 '-id')
#             temp = []
#             for i in notification_List:
#                 temp.append(i.id)
#             notification_Length = len(temp)
#             # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#
#         else:
#             return redirect('../edit-pat-profile', {'message': 'PLease Fill the Profile First'})
#     return render(request, "patient-admin/notice-list.html", locals())

#
# @login_required(login_url="login")
# def mail_box_pat(request):
#     doctor_List = []
#     object_msg = messages_db()
#     if doctor_profile_db.objects.all():
#         doctor_List = doctor_profile_db.objects.all()
#     if request.user.is_staff == 0:
#         patient_id = User.objects.get(id=request.user.id)
#         if request.method == "POST":
#             doctor = request.POST.get('doctor', '')
#             message = request.POST.get('message', '')
#             object_msg.doctor_id = doctor
#             object_msg.patient = patient_id
#             object_msg.message = message
#             object_msg.msg_sender = 0
#             object_msg.save()
#             messages.success(request, 'Message Send sucessfully')
#             return redirect('../mail-box-pat', locals())
#         if messages_db.objects.filter(patient=patient_id):
#             messages_List = messages_db.objects.filter(patient=patient_id)
#     return render(request, "patient-admin/mail-box.html", locals())

#
# @login_required(login_url="login")
# def pat_profile(request):
#     if request.user.is_staff == 0:
#         patient_id = User.objects.get(id=request.user.id)
#         if user_db.objects.filter(user_id=patient_id):
#             user_Profile = user_db.objects.filter(user_id=patient_id)
#
#         # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#
#         notification_List = notification_Db.objects.filter(patient=request.user.id, status=None, sender=1).order_by(
#             '-id')
#         temp = []
#         for i in notification_List:
#             temp.append(i.id)
#         notification_Length = len(temp)
#         # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#
#         return render(request, "patient-admin/my-profile.html", locals())
#     else:
#         return HttpResponseRedirect('../login', locals())
#
#
# @login_required(login_url="login")
# def delete_patient_Appointment(request, string):
#     # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#
#     notification_List = notification_Db.objects.filter(patient=request.user.id, status=None, sender=1).order_by('-id')
#     temp = []
#     for i in notification_List:
#         temp.append(i.id)
#     notification_Length = len(temp)
#     # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#
#     if smart_str(string) != None:
#         if patient_appointment_db.objects.filter(id=smart_str(string)):
#             patient_appointment_db.objects.filter(id=smart_str(string)).delete()
#             return redirect('../appointment-list-pat')
#     else:
#         return redirect('../appointment-list-pat')

#
# @login_required(login_url="login")
# def edit_pat_appointment(request):
#     if request.user.is_staff == 0:
#         # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#
#         notification_List = notification_Db.objects.filter(patient=request.user.id, status=None, sender=1).order_by(
#             '-id')
#         temp = []
#         for i in notification_List:
#             temp.append(i.id)
#         notification_Length = len(temp)
#         # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#
#         if request.method == "POST":
#             mr_mrs = request.POST.get('mr_mrs', '')
#             first_name = request.POST.get('first_name', '')
#             last_name = request.POST.get('last_name', '')
#             email = request.POST.get('email', '')
#             mobile = request.POST.get('mobile', '')
#             department = request.POST.get('department', '')
#             doctor = request.POST.get('doctor', '')
#             age = request.POST.get('age', '')
#             date_of_appointment = request.POST.get('date_of_appointment', '')
#             start_time = request.POST.get('start_time', '')
#             address = request.POST.get('address', '')
#             problmes = request.POST.get('problmes', '')
#             type_what_you_want = request.POST.get('type_what_you_want', '')
#             if patient_appointment_db.objects.filter(doctor=doctor):
#                 patient_appointment_db.objects.filter(doctor=doctor).update(mr_mrs=mr_mrs, first_name=first_name,
#                                                                             last_name=last_name, email=email,
#                                                                             mobile=mobile, department=department,
#                                                                             doctor=doctor, age=age,
#                                                                             date_of_appointment=date_of_appointment,
#                                                                             start_time=start_time,
#                                                                             address=address, problmes=problmes,
#                                                                             type_what_you_want=type_what_you_want,
#                                                                             status=None)
#         return redirect('../appointment-list-pat', locals())
#     else:
#         return HttpResponseRedirect('../login', locals())

#
# @login_required(login_url="login")
# def edit_pat_profile(request):
#     if request.user.is_staff == 0:
#         # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#
#         notification_List = notification_Db.objects.filter(patient=request.user.id, status=None, sender=1).order_by(
#             '-id')
#         temp = []
#         for i in notification_List:
#             temp.append(i.id)
#         notification_Length = len(temp)
#         # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#
#         if user_db.objects.filter(user_id=request.user.id):
#             user_db_List = user_db.objects.filter(user_id=request.user.id)
#         if request.method == 'POST':
#             patient_id = User.objects.get(id=request.user.id)
#             instance = get_object_or_404(User, id=request.user.id)
#             MyForm = patient_user_edit_profile_form(request.POST or None, instance=instance)
#             MyForm.save()
#             if user_db.objects.filter(user_id=request.user.id):
#                 instance = get_object_or_404(user_db, user_id=patient_id)
#                 MyForm2 = patient_profile_edit_form(request.POST or None, request.FILES or None, instance=instance)
#                 MyForm2.save()
#                 if user_db.objects.filter(user_id=request.user.id):
#                     user_db_List = user_db.objects.filter(user_id=request.user.id)
#                 return redirect('../edit-pat-profile', locals())
#                 #     uploaded_file_url = None
#                 #     if len(smart_str(myfile)) != 0:
#                 #         fs = FileSystemStorage()
#                 #         filename = fs.save(myfile.name, myfile)
#                 #         uploaded_file_url = fs.url(filename)
#                 #         print uploaded_file_url
#                 #     user_db.objects.filter(user_id=request.user.id).update(name=name,phone=phone,gender=gender,blood_group=blood_group,
#                 #                                                            age=age,occupation=occupation,myfile=uploaded_file_url
#                 #                                                            ,address=address,location=location,weight=weight)
#                 #     if user_db.objects.filter(user_id=request.user.id):
#                 #         user_db_List = user_db.objects.filter(user_id=request.user.id)
#                 #     redirect('../edit-pat-profile')
#             else:
#                 MyForm2 = patient_profile_edit_form(request.POST or None, request.FILES)
#                 new_book = MyForm2.save(commit=False)  # Don't save it yet
#                 new_book.user_id = patient_id
#                 new_book.save()
#                 MyForm2.save()
#                 # uploaded_file_url = None
#                 # if len(smart_str(myfile)) != 0:
#                 #     fs = FileSystemStorage()
#                 #     filename = fs.save(myfile.name, myfile)
#                 #     uploaded_file_url = fs.url(filename)
#                 #     print uploaded_file_url
#                 # object_userDb = user_db()
#                 # object_userDb.name = name
#                 # object_userDb.phone = phone
#                 # object_userDb.gender = gender
#                 # object_userDb.blood_group = blood_group
#                 # object_userDb.age = age
#                 # object_userDb.occupation = name
#                 # object_userDb.myfile = uploaded_file_url
#                 # object_userDb.address = address
#                 # object_userDb.location = location
#                 # object_userDb.weight = weight
#                 # object_userDb.user_id = patient_id
#                 # object_userDb.save()
#
#                 if user_db.objects.filter(user_id=request.user.id):
#                     user_db_List = user_db.objects.filter(user_id=request.user.id)
#                 return redirect('../edit-pat-profile', locals())
#         return render(request, 'patient-admin/edit-profile.html', locals())
#     else:
#         return HttpResponseRedirect('../login', locals())

#
# @login_required(login_url="login")
# def doctor_profile_pat_show(request, string):
#     if request.user.is_staff == 0:
#         if doctor_profile_db.objects.filter(id=string):
#             doctor_Data = doctor_profile_db.objects.filter(id=string)
#
#         # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#
#         notification_List = notification_Db.objects.filter(patient=request.user.id, status=None, sender=1).order_by(
#             '-id')
#         temp = []
#         for i in notification_List:
#             temp.append(i.id)
#         notification_Length = len(temp)
#         # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#
#         return render(request, "patient-admin/doctor-profile.html", locals())
#     else:
#         return HttpResponseRedirect('../login', locals())
#

# @login_required(login_url="login")
# def read_notification(request, string):
#     if request.user.is_staff == 0:
#         if smart_str(string) != None:
#             id, check = smart_str(string).split('__')
#             notification_Db.objects.filter(id=id).update(status='Read')
#             if check == 'appointment_accepted':
#                 return redirect('../appointment-list-pat')
#             elif check == 'appointment_declined':
#                 return redirect('../appointment-list-pat')
#             elif check == 'report_added':
#                 return redirect('../total-reports-pat')
#             elif check == 'rechedule_appointment':
#                 return redirect('../appointment-list-pat')
#             else:
#                 return redirect('../notice-list-pat')
#     else:
#         return HttpResponseRedirect('../login', locals())
#
#
# @login_required(login_url="login")
# def read_notification_doctor(request, string):
#     if request.user.is_staff == 1:
#         if smart_str(string) != None:
#             id, dump = smart_str(string).split('__')
#             notification_Db.objects.filter(id=id).update(status='Read')
#             if dump == 'new_Appointment':
#                 return redirect('../appointment-list')
#             else:
#                 return redirect('../notice-list-doctor')
#     else:
#         return HttpResponseRedirect('../login', locals())
#
#

#
#
# def payment_list_pat(request):
#     if request.user.is_staff == 0:
#         payment_data = instamojo_payment_done.objects.filter(user_id=request.user.id)
#
#         return render(request, "patient-admin/payment-list.html", locals())
#     else:
#         return HttpResponseRedirect('../login', locals())
#
#
# def patient_payment(request):
#     if request.user.is_staff == 0:
#         return render(request, "patient-admin/patient-invoice.html", locals())
#     else:
#         return HttpResponseRedirect('../login', locals())
#
#


def undermaintenance(request):
    return render(request, 'patient-admin/undermaintenance.html', locals())


def google55fc80e83a72caed(request):
    return render(request, 'google55fc80e83a72caed.html', locals())
