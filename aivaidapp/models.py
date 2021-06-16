# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.utils.datetime_safe import datetime
from django.contrib.auth.models import User

# #
class symptoms_type(models.Model):
    symptoms_type_name = models.CharField(max_length=100, unique=True)
    class Meta:
        db_table = "symptoms_type"

    def __str__(self):
        return self.symptoms_type_name


class symptoms_db(models.Model):
    symptoms_name = models.CharField(max_length=100, unique=True)
    pkl_file = models.FileField(upload_to='pkl_model')
    symptoms_type_id = models.ForeignKey(symptoms_type ,default=1,null=True, blank=True)

    class Meta:
        db_table = "symptoms_db"

    def __str__(self):
        return self.symptoms_name


class disease_db(models.Model):
    disease_name = models.CharField(max_length=100, unique=True)
    symptoms_id = models.ForeignKey(symptoms_db)

    class Meta:
        db_table = "disease_db"

    def __str__(self):
        return self.disease_name


class questions_db(models.Model):
    questions_name = models.CharField(max_length=1000)
    symptoms_id = models.ForeignKey(symptoms_db)
    disease_id = models.ForeignKey(disease_db)

    class Meta:
        db_table = "questions_db"

    def __str__(self):
        return self.questions_name


class Contact_db(models.Model):
    name = models.CharField(max_length=1000)
    email = models.CharField(max_length=100)
    mobile = models.CharField(max_length=100)
    message = models.CharField(max_length=1000)

    class Meta:
        db_table = "Contact_db"


# front panel model here



class accept_terms_db(models.Model):
    accept_terms = models.CharField(max_length=100)
    user_id = models.CharField(max_length=100)

    # user_id = models.ForeignKey(User)

    class Meta:
        db_table = "accept_terms_db"


class user_db(models.Model):
    auth_user_id = models.ForeignKey(User, null=True, blank=True)
    user_id = models.CharField(max_length=100, null=True, blank=True)
    first_name = models.CharField(max_length=100, null=True, blank=True)
    last_name = models.CharField(max_length=100, null=True, blank=True)

    # ==============================================================
    phone = models.CharField(max_length=100, null=True, blank=True)
    address = models.CharField(max_length=1000, null=True, blank=True)
    occupation = models.CharField(max_length=100, null=True, blank=True)
    myfile = models.FileField(upload_to='patient_profile', null=True, blank=True)
    blood_group = models.CharField(max_length=100, null=True, blank=True)
    # ==============================================================

    state = models.CharField(max_length=100, null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    weight = models.CharField(max_length=100, null=True, blank=True)
    height_cm = models.CharField(max_length=100, null=True, blank=True)
    height_feet = models.CharField(max_length=100, null=True, blank=True)
    age = models.CharField(max_length=100, null=True, blank=True)
    gender = models.CharField(max_length=100, null=True, blank=True)
    body_mass_index = models.CharField(max_length=100, null=True, blank=True)
    results = models.CharField(max_length=100, null=True, blank=True)
    your_symptoms = models.CharField(max_length=1000, null=True, blank=True)
    Recently_Visited_Locations = models.CharField(max_length=1000, null=True, blank=True)

    class Meta:
        db_table = "user_db"


class user_medical_record_db(models.Model):
    user_id = models.ForeignKey(User)
    medrecord = models.FileField(upload_to='medrecord', null=True, blank=True)
    rtitle = models.CharField(max_length=1000, null=True, blank=True)
    rname = models.CharField(max_length=1000, null=True, blank=True)
    rselect_date = models.CharField(max_length=1000, null=True, blank=True)
    rrecord = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        db_table = "user_medical_record_db"


# Docter Model here ----------------------------------------------------------------------

class doctor_profile_db(models.Model):
    doctor_profile_id = models.ForeignKey(User)
    udob = models.CharField(max_length=100, null=True, blank=True)
    umobile = models.CharField(max_length=1000, null=True, blank=True)
    ugender = models.CharField(max_length=1000, null=True, blank=True)
    state = models.CharField(max_length=1000, null=True, blank=True)
    selectcity = models.CharField(max_length=1000, null=True, blank=True)
    uregNumber = models.CharField(max_length=1000, null=True, blank=True)
    ucounsil = models.CharField(max_length=1000, null=True, blank=True)
    regyear = models.CharField(max_length=1000, null=True, blank=True)
    selectdegree = models.CharField(max_length=1000, null=True, blank=True)
    uinstitute = models.CharField(max_length=1000, null=True, blank=True)
    degreecompletion = models.CharField(max_length=1000, null=True, blank=True)
    uexperience01 = models.CharField(max_length=1000, null=True, blank=True)
    uexperience_month = models.CharField(max_length=1000, null=True, blank=True)
    uexperience02 = models.CharField(max_length=1000, null=True, blank=True)
    # uexperience03 = models.CharField(max_length=1000, null=True, blank=True)
    pic = models.FileField(upload_to='doctor_profile', null=True, blank=True)
    Description = models.CharField(max_length=1000, null=True, blank=True)
    mobile_verify = models.CharField(max_length=10,default=0)
    otp = models.CharField(max_length=10, null=True, blank=True)
    admin_verify = models.CharField(max_length=10,default=0)
    doctor_idproof = models.FileField(upload_to='doctor_idproof', null=True, blank=True)
    doctor_idproof2 = models.FileField(upload_to='doctor_idproof', null=True, blank=True)



    # image = models.FileField(upload_to='doctor_profile', null=True, blank=True)
    # languages = models.CharField(max_length=1000, null=True, blank=True)
    # residential_address = models.CharField(max_length=1000, null=True, blank=True)
    # qualification = models.CharField(max_length=1000, null=True, blank=True)
    # specility = models.CharField(max_length=1000, null=True, blank=True)
    # hospital_name = models.CharField(max_length=1000, null=True, blank=True)
    # experience = models.CharField(max_length=1000, null=True, blank=True)
    # first_name = models.CharField(max_length=1000,null=True,blank=True)
    # last_name = models.CharField(max_length=1000,null=True,blank=True)
    # country = models.CharField(max_length=1000,null=True,blank=True)

    class Meta:
        db_table = "doctor_profile_db"


class clinic_details_db(models.Model):
    doctor_profile_id = models.ForeignKey(User)
    Ctype = models.CharField(max_length=100, null=True, blank=True)
    Cname = models.CharField(max_length=1000, null=True, blank=True)
    Ctitle = models.CharField(max_length=1000, null=True, blank=True)
    Cfee = models.CharField(max_length=1000, null=True, blank=True)
    Online_Cfee = models.CharField(max_length=1000, null=True, blank=True)
    Cphone01 = models.CharField(max_length=1000, null=True, blank=True)
    Cphone02 = models.CharField(max_length=1000, null=True, blank=True)
    Cstate = models.CharField(max_length=1000, null=True, blank=True)
    Ccity = models.CharField(max_length=1000, null=True, blank=True)
    Caddress = models.CharField(max_length=1000, null=True, blank=True)
    Cphotos = models.FileField(upload_to='clinic_profile', null=True, blank=True)
    sunday_appt_time1 = models.CharField(max_length=1000, null=True, blank=True)
    sunday_appt_time2 = models.CharField(max_length=1000, null=True, blank=True)
    monday_appt_time1 = models.CharField(max_length=1000, null=True, blank=True)
    monday_appt_time2 = models.CharField(max_length=1000, null=True, blank=True)
    tuesday_appt_time1 = models.CharField(max_length=1000, null=True, blank=True)
    tuesday_appt_time2 = models.CharField(max_length=1000, null=True, blank=True)
    wednesday_appt_time1 = models.CharField(max_length=1000, null=True, blank=True)
    wednesday_appt_time2 = models.CharField(max_length=1000, null=True, blank=True)
    thursday_appt_time1 = models.CharField(max_length=1000, null=True, blank=True)
    thursday_appt_time2 = models.CharField(max_length=1000, null=True, blank=True)
    friday_appt_time1 = models.CharField(max_length=1000, null=True, blank=True)
    friday_appt_time2 = models.CharField(max_length=1000, null=True, blank=True)
    saturday_appt_time1 = models.CharField(max_length=1000, null=True, blank=True)
    saturday_appt_time2 = models.CharField(max_length=1000, null=True, blank=True)
    Cproof = models.FileField(upload_to='clinic_idproof', null=True, blank=True)
    # Cidproof = models.FileField(upload_to='clinic_idproof', null=True, blank=True)
    Cmedproof = models.FileField(upload_to='clinic_idproof', null=True, blank=True)

    class Meta:
        db_table = "clinic_details_db"




class clinic_pic_db(models.Model):
    doctor_profile_id = models.ForeignKey(User)
    clinic_id = models.ForeignKey(clinic_details_db)
    Cphotos1 = models.FileField(upload_to='clinic_profile', null=True, blank=True)
    Cphotos2 = models.FileField(upload_to='clinic_profile', null=True, blank=True)
    Cphotos3 = models.FileField(upload_to='clinic_profile', null=True, blank=True)
    Cphotos4 = models.FileField(upload_to='clinic_profile', null=True, blank=True)
    Cphotos5 = models.FileField(upload_to='clinic_profile', null=True, blank=True)
    Cphotos6 = models.FileField(upload_to='clinic_profile', null=True, blank=True)
    class Meta:
        db_table = "clinic_pic_db"


class review_db(models.Model):
    doctor_profile_id = models.ForeignKey(User)
    name = models.CharField(max_length=1000,null=True, blank=True)
    email = models.CharField(max_length=100,null=True, blank=True)
    description = models.CharField(max_length=1000,null=True, blank=True)
    rating1 = models.CharField(max_length=1000,null=True, blank=True)
    date = models.CharField(max_length=100, default=datetime.today().strftime('%Y-%m-%d'), blank=True)
    class Meta:
        db_table = "review_db"





class doctor_patient_db(models.Model):
    doctor_profile_id = models.ForeignKey(User)
    first_name = models.CharField(max_length=1000)
    last_name = models.CharField(max_length=1000)
    email = models.CharField(max_length=100, unique=True)
    gender = models.CharField(max_length=1000)
    birthdate = models.CharField(max_length=1000)
    age = models.CharField(max_length=1000)
    mobile = models.CharField(max_length=1000)
    martial_status = models.CharField(max_length=1000)
    blood_group = models.CharField(max_length=1000)
    address = models.CharField(max_length=1000)
    injury = models.CharField(max_length=1000)
    upload_profile = models.FileField(upload_to='patient_profile')

    class Meta:
        db_table = "doctor_patient_db"


class doctor_schedule_db(models.Model):
    doctor_profile_id = models.ForeignKey(User)
    days = models.CharField(max_length=1000)
    date = models.CharField(max_length=1000)
    start_time = models.CharField(max_length=100)
    end_time = models.CharField(max_length=1000)
    patient_time = models.CharField(max_length=1000)
    active_inactive = models.CharField(max_length=1000)

    class Meta:
        db_table = "doctor_schedule_db"


class doctor_appointment_db(models.Model):
    doctor_profile_id = models.ForeignKey(User)
    # mr_mrs = models.CharField(max_length=1000)
    first_name = models.CharField(max_length=1000)
    last_name = models.CharField(max_length=1000)
    email = models.CharField(max_length=100, unique=True)
    mobile = models.CharField(max_length=100, unique=True)
    birtdate = models.CharField(max_length=100, null=True, blank=True)
    date_of_appointment = models.CharField(max_length=100, null=True, blank=True)
    start_time = models.CharField(max_length=100, null=True, blank=True)
    end_time = models.CharField(max_length=1000, null=True, blank=True)
    address = models.CharField(max_length=1000, null=True, blank=True)
    problmes = models.CharField(max_length=1000, null=True, blank=True)
    type_what_you_want = models.CharField(max_length=1000, null=True, blank=True)

    class Meta:
        db_table = "doctor_appointment_db"


class doctor_patient_report(models.Model):
    doctor_profile_id = models.ForeignKey(User)
    doctor_patient_id = models.ForeignKey(doctor_patient_db)
    date = models.CharField(max_length=100, null=True, blank=True)
    Disease = models.ForeignKey(disease_db)
    descrition = models.CharField(max_length=1000, null=True, blank=True)

    class Meta:
        db_table = "doctor_patient_report"


# ----------------------------amit sir code here ------------------------------
class patient_appointment_db(models.Model):
    patient = models.ForeignKey(User)
    clinic = models.ForeignKey(clinic_details_db, null=True, blank=True)
    doctor = models.ForeignKey(doctor_profile_db, null=True, blank=True)
    # mr_mrs = models.CharField(max_length=1000, null=True, blank=True)
    first_name = models.CharField(max_length=1000, null=True, blank=True)
    last_name = models.CharField(max_length=1000, null=True, blank=True)
    email = models.CharField(max_length=100, null=True, blank=True)
    mobile = models.CharField(max_length=100, null=True, blank=True)
    age = models.CharField(max_length=100, null=True, blank=True)
    date_of_appointment = models.CharField(max_length=100, null=True, blank=True)
    start_time = models.CharField(max_length=100, null=True, blank=True)
    end_time = models.CharField(max_length=1000, null=True, blank=True)
    address = models.CharField(max_length=1000, null=True, blank=True)
    problmes = models.CharField(max_length=1000, null=True, blank=True)
    status = models.CharField(max_length=1000, null=True, blank=True)
    treatment = models.CharField(max_length=1000, null=True, blank=True)
    payment = models.CharField(max_length=100, null=True, blank=True)
    type_what_you_want = models.CharField(max_length=1000, null=True, blank=True)
    confirm = models.CharField(max_length=1000,default=0)

    class Meta:
        db_table = "patient_appointment_db"


class messages_db(models.Model):
    patient = models.ForeignKey(User)
    doctor_id = models.CharField(max_length=10, null=True, blank=True)
    message = models.CharField(max_length=10000, null=True, blank=True)
    msg_sender = models.CharField(max_length=10, null=True, blank=True)

    class Meta:
        db_table = "messages_db"


class departments(models.Model):
    dep_Name = models.CharField(max_length=100, unique=True)
    description = models.CharField(max_length=100, unique=True)

    class Meta:
        db_table = "departments"


class reports_Db(models.Model):
    patient = models.ForeignKey(User)
    doctor_id = models.CharField(max_length=100, null=True, blank=True)
    appointment_id = models.CharField(max_length=100, null=True, blank=True)
    disease = models.CharField(max_length=100, null=True, blank=True)
    prescription = models.CharField(max_length=100, null=True, blank=True)
    date = models.CharField(max_length=100, null=True, blank=True)


    class Meta:
        db_table = "reports_Db"


class notification_Db(models.Model):
    patient = models.ForeignKey(User)
    doctor = models.CharField(max_length=100, null=True, blank=True)
    date = models.CharField(max_length=100, null=True, blank=True)
    time = models.CharField(max_length=100, null=True, blank=True)
    notification = models.CharField(max_length=100, null=True, blank=True)
    sender = models.CharField(max_length=100, null=True, blank=True)
    status = models.CharField(max_length=100, null=True, blank=True)
    date_1 = models.CharField(max_length=100, default=datetime.today().strftime('%Y-%m-%d'), blank=True)


    class Meta:
        db_table = "notification_Db"


class payment(models.Model):
    user_id = models.ForeignKey(User, null=True, blank=True)
    email = models.EmailField()
    amount = models.CharField(max_length=100)
    item_name = models.CharField(max_length=100)
    item_id = models.CharField(max_length=100)
    date = models.CharField(max_length=100, default=datetime.today().strftime('%Y-%m-%d'), blank=True)


    class Meta:
        db_table = "payment"


class instamojo_payment(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    amount = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    item_name = models.CharField(max_length=100)
    payment_request_id = models.CharField(max_length=100)
    date = models.CharField(max_length=100, default=datetime.today().strftime('%Y-%m-%d'), blank=True)


    class Meta:
        db_table = "instamojo_payment"


class instamojo_payment_done(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    amount = models.CharField(max_length=100)
    item_name = models.CharField(max_length=100)
    payment_request_id = models.CharField(max_length=255, unique=True)
    status = models.CharField(max_length=500)
    payment_id = models.CharField(max_length=255, unique=True)
    user_id = models.ForeignKey(User, null=True, blank=True)
    doctor_id = models.CharField(max_length=255,null=True, blank=True)
    date = models.CharField(max_length=100, default=datetime.today().strftime('%Y-%m-%d'), blank=True)


    class Meta:
        db_table = "instamojo_payment_done"


class doctor_Services(models.Model):
    doctor = models.ForeignKey(User)
    service = models.CharField(max_length=10000, null=True, blank=True)
    price = models.CharField(max_length=10, null=True, blank=True)
    discount = models.CharField(max_length=10, null=True, blank=True)
    date = models.CharField(max_length=100, default=datetime.today().strftime('%Y-%m-%d'), blank=True)

    class Meta:
        db_table = "doctor_Services"
