from django import forms
from django.contrib.auth.models import User

from aivaidapp.models import symptoms_db, questions_db, disease_db, doctor_profile_db, doctor_patient_db, \
    doctor_schedule_db, doctor_appointment_db, accept_terms_db, Contact_db, doctor_patient_report, \
    patient_appointment_db, user_db, user_medical_record_db, clinic_details_db, clinic_pic_db, review_db

from django.contrib.auth.forms import UserCreationForm, PasswordResetForm


# admin panel forms here _____________________|||||||||||||||||||||

class symptoms_form(forms.ModelForm):
    symptoms_name = forms.CharField(max_length=100)
    pkl_file = forms.FileField(required=True)

    class Meta:
        model = symptoms_db
        fields = ['symptoms_name', 'pkl_file']


class symptoms_edit_Form(forms.ModelForm):
    class Meta:
        model = symptoms_db
        fields = ['id', 'symptoms_name', 'pkl_file']

symptom_list = symptoms_db.objects.all()
SYMPTOMS_CHOICES = [(ix.id, ix.symptoms_name) for ix in symptom_list]

disease_list = disease_db.objects.all()
DISEASE_CHOICES = [(ix.id, ix.disease_name) for ix in disease_list]


class disease_form(forms.ModelForm):
    disease_name = forms.CharField(max_length=100)
    symptoms_id = forms.IntegerField(label='Symptoms', widget=forms.Select(choices=SYMPTOMS_CHOICES))

    class Meta:
        model = disease_db
        fields = ['disease_name', 'symptoms_id']


class questions_form(forms.ModelForm):
    questions_name = forms.CharField(max_length=100)
    symptoms_id = forms.CharField(label='Symptoms', widget=forms.Select(choices=SYMPTOMS_CHOICES))

    class Meta:
        model = questions_db
        fields = ['questions_name', 'symptoms_id']


class questions_edit_form(forms.ModelForm):
    class Meta:
        model = questions_db
        fields = ['questions_name']



class EmailValidationOnForgotPassword(PasswordResetForm):
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    def clean_email(self):
        email = self.cleaned_data['email']
        if not User.objects.filter(email__iexact=email, is_active=True).exists():
            raise forms.ValidationError("There is no user registered with the specified email address!")
            # messeage =("There is no user registered with the specified email address!")
            # return redirect('../password_reset',locals())

            # return 'no'
        return email



class Contact_db_Form(forms.ModelForm):
    name = forms.CharField(max_length=1000, widget=forms.TextInput(attrs={'class': 'form-field'}))
    email = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-field'}))
    mobile = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-field'}))
    message = forms.CharField(max_length=1000, widget=forms.Textarea(attrs={'class': ''}))

    class Meta:
        model = Contact_db
        fields = ['name', 'email', 'mobile', 'message']


# front panel form  here ___________________________||||||||||||||||





class accept_terms_form(forms.ModelForm):
    accept_terms = forms.BooleanField(label='')

    class Meta:
        model = accept_terms_db
        fields = ['accept_terms']


class user_Form(forms.Form):
    name = forms.CharField(max_length=100)
    location = forms.CharField(max_length=100)
    weight = forms.CharField(max_length=100)
    height = forms.CharField(max_length=100)
    age = forms.CharField(max_length=100)
    gender = forms.CharField(max_length=100)
    body_mass_index = forms.CharField(max_length=100)
    results = forms.CharField(max_length=100)


# Doctor form login panel form here ---------------------

USER_TYPE = [
    ('1', 'Doctor',),
    ('0', 'Patient'),
]


class doctor_SignupForm(UserCreationForm):
    username = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'class': 'forms_field-input userinput02'}))
    first_name = forms.CharField(max_length=30, help_text='Optional.')
    last_name = forms.CharField(max_length=30, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    is_staff = forms.CharField(label='USER TYPE', widget=forms.RadioSelect(choices=USER_TYPE, ))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'is_staff', 'email', 'password1', 'password2',)

    def clean_email(self):
        email = self.cleaned_data.get('email')
        username = self.cleaned_data.get('username')
        if email and User.objects.filter(email=email).exclude(username=username).exists():
            raise forms.ValidationError(u'Email already exists.')
        return email


class UserLoginForm(forms.Form):
    email = forms.CharField(required=True)
    password = forms.CharField(widget=forms.PasswordInput)


# ---------------------------------------------------------------------



class user_medical_record_Form(forms.ModelForm):
    medrecord = forms.FileField()
    rtitle = forms.CharField(max_length=1000, required=False)
    rname = forms.CharField(max_length=1000, required=False)
    rselect_date = forms.CharField(max_length=1000, required=False)
    rrecord = forms.CharField(max_length=100, required=False)

    class Meta:
        model = user_medical_record_db
        fields = ['medrecord', 'rtitle', 'rname', 'rselect_date', 'rrecord']


class PayForm(forms.Form):
    Name = forms.CharField(label='Your name', max_length=100)
    Email = forms.EmailField(label='Email Address')
    Phone = forms.IntegerField(label='Phone Number', min_value=7000000000, max_value=9999999999)
    Amount = forms.IntegerField(label='Amount')
    Purpose = forms.CharField(label="Purpose", max_length=100)


class doctor_user_edit_profile_form(forms.ModelForm):
    first_name = forms.CharField(max_length=1000, required=False)
    last_name = forms.CharField(max_length=1000, required=False)
    class Meta:
        model = User
        fields = ['first_name', 'last_name']


class patient_user_edit_profile_form(forms.ModelForm):
    first_name = forms.CharField(max_length=1000, required=False)
    last_name = forms.CharField(max_length=1000, required=False)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', ]


class doctor_profile_edit_form(forms.ModelForm):
    udob = forms.CharField(max_length=100, )
    umobile = forms.CharField(max_length=1000, required=False)
    ugender = forms.CharField(max_length=1000, required=False)
    state = forms.CharField(max_length=1000, required=False)
    selectcity = forms.CharField(max_length=1000, required=False)
    uregNumber = forms.CharField(max_length=1000, required=False)
    ucounsil = forms.CharField(max_length=1000, required=False)
    regyear = forms.CharField(max_length=1000, required=False)
    selectdegree = forms.CharField(max_length=1000, required=False)
    uinstitute = forms.CharField(max_length=1000, required=False)
    degreecompletion = forms.CharField(max_length=1000, required=False)
    uexperience01 = forms.CharField(max_length=1000, required=False)
    uexperience_month = forms.CharField(max_length=1000, required=False)
    uexperience02 = forms.CharField(max_length=1000, required=False)
    # uexperience03 = forms.CharField(max_length=1000, required=False)
    pic = forms.FileField(max_length=1000, required=False)
    doctor_idproof = forms.FileField(max_length=1000, required=False)
    doctor_idproof2 = forms.FileField(max_length=1000, required=False)
    Description = forms.CharField(max_length=1000, required=False)

    class Meta:
        model = doctor_profile_db
        fields = ['udob', 'umobile', 'ugender', 'state', 'selectcity', 'uregNumber', 'ucounsil', 'regyear',
                  'selectdegree'
            , 'uinstitute', 'degreecompletion', 'uexperience01', 'uexperience_month', 'uexperience02', 'pic','doctor_idproof','doctor_idproof2', 'Description']


class clinic_details_Form(forms.ModelForm):
    # doctor_profile_id = models.ForeignKey(User)
    Ctype = forms.CharField(max_length=100, required=False)
    Cname = forms.CharField(max_length=1000, required=False)
    Ctitle = forms.CharField(max_length=1000, required=False)
    Cfee = forms.CharField(max_length=1000, required=False)
    Online_Cfee = forms.CharField(max_length=1000, required=False)
    Cphone01 = forms.CharField(max_length=1000, required=False)
    Cphone02 = forms.CharField(max_length=1000, required=False)
    Cstate = forms.CharField(max_length=1000, required=False)
    Ccity = forms.CharField(max_length=1000, required=False)
    Caddress = forms.CharField(max_length=1000, required=False)
    Cphotos = forms.FileField(required=False)
    # Sunday_from = forms.CharField(max_length=1000, required=False)
    # Sunday_to = forms.CharField(max_length=1000, required=False)
    # Monday_from = forms.CharField(max_length=1000, required=False)
    # Monday_to = forms.CharField(max_length=1000, required=False)
    # Tuesday_from = forms.CharField(max_length=1000, required=False)
    # Tuesday_to = forms.CharField(max_length=1000, required=False)
    # Wednesday_from = forms.CharField(max_length=1000, required=False)
    # Wednesday_to = forms.CharField(max_length=1000, required=False)
    # Thursday_from = forms.CharField(max_length=1000, required=False)
    # Thursday_to = forms.CharField(max_length=1000, required=False)
    # Friday_from = forms.CharField(max_length=1000, required=False)
    # Friday_to = forms.CharField(max_length=1000, required=False)
    # Saturday_from = forms.CharField(max_length=1000, required=False)
    # Saturday_to = forms.CharField(max_length=1000, required=False)
    Cproof = forms.FileField(required=False)
    # Cidproof = forms.FileField(required=False)
    Cmedproof = forms.FileField(required=False)

    class Meta:
        model = clinic_details_db
        fields = ['Ctype', 'Cname', 'Ctitle', 'Cfee','Online_Cfee', 'Cphone01', 'Cphone02', 'Cstate', 'Ccity', 'Caddress', 'Cphotos',
                   'Cproof','Cmedproof']





class clinic_pic_forms(forms.ModelForm):
    Cphotos1 = forms.FileField(required=False)
    Cphotos2 = forms.FileField(required=False)
    Cphotos3 = forms.FileField(required=False)
    Cphotos4 = forms.FileField(required=False)
    Cphotos5 = forms.FileField(required=False)
    Cphotos6 = forms.FileField(required=False)
    class Meta:
        model = clinic_pic_db
        fields =['Cphotos1','Cphotos2','Cphotos3','Cphotos4','Cphotos5','Cphotos6',]



class review_forms(forms.ModelForm):
    name = forms.CharField(max_length=1000,required=False)
    email = forms.CharField(max_length=100,required=False)
    description = forms.CharField(max_length=1000,required=False)
    rating1 = forms.CharField(max_length=1000,required=False)
    class Meta:
        model = review_db
        fields =['name','email','description','rating1']





class patient_profile_edit_form(forms.ModelForm):
    first_name = forms.CharField(max_length=1000, required=False)
    last_name = forms.CharField(max_length=1000, required=False)
    phone = forms.CharField(max_length=1000, required=False)
    gender = forms.CharField(max_length=1000, required=False)
    myfile = forms.FileField(max_length=1000, required=False)
    blood_group = forms.CharField(max_length=1000, required=False)
    age = forms.CharField(max_length=1000, required=False)
    occupation = forms.CharField(max_length=1000, required=False)
    address = forms.CharField(max_length=1000, required=False)
    state = forms.CharField(max_length=1000, required=False)
    city = forms.CharField(max_length=1000, required=False)
    weight = forms.CharField(max_length=1000, required=False)
    height_cm = forms.CharField(max_length=1000, required=False)
    body_mass_index = forms.CharField(max_length=1000, required=False)
    results = forms.CharField(max_length=1000, required=False)

    class Meta:
        model = user_db
        fields = ['first_name', 'last_name', 'phone', 'gender', 'myfile', 'blood_group', 'age', 'occupation', 'address',
                  'state', 'city', 'weight','height_cm','body_mass_index','results']


class doctor_patient_form(forms.ModelForm):
    first_name = forms.CharField(max_length=100, required=False)
    last_name = forms.CharField(max_length=100, required=False)
    email = forms.CharField(max_length=100, required=False)
    gender = forms.CharField(max_length=100, required=False)
    birthdate = forms.CharField(max_length=100, required=False)
    age = forms.CharField(max_length=1000, required=False)
    mobile = forms.CharField(max_length=100, required=False)
    martial_status = forms.CharField(max_length=100, required=False)
    blood_group = forms.CharField(max_length=100, required=False)
    address = forms.CharField(max_length=100, required=False)
    injury = forms.CharField(max_length=100, required=False)
    upload_profile = forms.FileField(max_length=100, required=False)

    class Meta:
        model = doctor_patient_db
        fields = ['first_name', 'last_name', 'email', 'gender', 'birthdate', 'age', 'mobile', 'martial_status',
                  'blood_group', 'address', 'injury', 'upload_profile']


class edit_patient_form(forms.ModelForm):
    first_name = forms.CharField(max_length=100, required=False)
    last_name = forms.CharField(max_length=100, required=False)
    email = forms.CharField(max_length=100, required=False)
    gender = forms.CharField(max_length=100, required=False)
    birthdate = forms.CharField(max_length=100, required=False)
    age = forms.CharField(max_length=1000, required=False)
    mobile = forms.CharField(max_length=100, required=False)
    martial_status = forms.CharField(max_length=100, required=False)
    blood_group = forms.CharField(max_length=100, required=False)
    address = forms.CharField(max_length=100, required=False)
    injury = forms.CharField(max_length=100, required=False)
    upload_profile = forms.FileField(max_length=100, required=False)

    class Meta:
        model = doctor_patient_db
        fields = ['first_name', 'last_name', 'email', 'gender', 'birthdate', 'age', 'mobile', 'martial_status',
                  'blood_group', 'address', 'injury', 'upload_profile']


class doctor_schedule_form(forms.ModelForm):
    days = forms.CharField(max_length=1000, required=False)
    date = forms.CharField(max_length=1000, required=False)
    start_time = forms.CharField(max_length=100, required=False)
    end_time = forms.CharField(max_length=1000, required=False)
    patient_time = forms.CharField(max_length=1000, required=False)
    active_inactive = forms.CharField(max_length=1000, required=False)

    class Meta:
        model = doctor_schedule_db
        fields = ['days', 'date', 'start_time', 'end_time', 'patient_time', 'active_inactive']


class save_edit_form(forms.ModelForm):
    days = forms.CharField(max_length=1000, required=False)
    date = forms.CharField(max_length=1000, required=False)
    start_time = forms.CharField(max_length=100, required=False)
    end_time = forms.CharField(max_length=1000, required=False)
    patient_time = forms.CharField(max_length=1000, required=False)
    active_inactive = forms.CharField(max_length=1000, required=False)

    class Meta:
        model = doctor_schedule_db
        fields = ['days', 'date', 'start_time', 'end_time', 'patient_time', 'active_inactive']


class doctor_appointment_form(forms.ModelForm):
    # mr_mrs = forms.CharField(max_length=1000,required=False)
    first_name = forms.CharField(max_length=1000, required=False)
    last_name = forms.CharField(max_length=1000, required=False)
    email = forms.CharField(max_length=100, required=False)
    mobile = forms.CharField(max_length=100, required=False)
    birtdate = forms.CharField(max_length=100, required=False)
    date_of_appointment = forms.CharField(max_length=100, required=False)
    start_time = forms.CharField(max_length=100, required=False)
    end_time = forms.CharField(max_length=1000, required=False)
    address = forms.CharField(max_length=1000, required=False)
    problmes = forms.CharField(max_length=1000, required=False)
    type_what_you_want = forms.CharField(max_length=1000, required=False)

    class Meta:
        model = doctor_appointment_db
        fields = ['first_name', 'last_name', 'email', 'mobile', 'birtdate', 'date_of_appointment', 'start_time',
                  'end_time', 'address', 'problmes', 'type_what_you_want']


class edit_appointment_form(forms.ModelForm):
    first_name = forms.CharField(max_length=1000, required=False)
    last_name = forms.CharField(max_length=1000, required=False)
    email = forms.CharField(max_length=100, required=False)
    mobile = forms.CharField(max_length=100, required=False)
    birtdate = forms.CharField(max_length=100, required=False)
    date_of_appointment = forms.CharField(max_length=100, required=False)
    start_time = forms.CharField(max_length=100, required=False)
    end_time = forms.CharField(max_length=1000, required=False)
    address = forms.CharField(max_length=1000, required=False)
    problmes = forms.CharField(max_length=1000, required=False)
    type_what_you_want = forms.CharField(max_length=1000, required=False)

    class Meta:
        model = doctor_appointment_db
        fields = ['first_name', 'last_name', 'email', 'mobile', 'birtdate', 'date_of_appointment', 'start_time',
                  'end_time', 'address', 'problmes', 'type_what_you_want']


class doctor_patient_report_form(forms.ModelForm):
    date = forms.CharField(max_length=100, required=False)
    descrition = forms.CharField(max_length=1000, required=False)

    class Meta:
        model = doctor_patient_report
        fields = ['date', 'descrition']


# --------------------amit sir code here -----------------------------------
class patient_appointment_form(forms.ModelForm):
    # mr_mrs = forms.CharField(max_length=1000, required=False)
    first_name = forms.CharField(max_length=1000, required=True)
    # last_name = forms.CharField(max_length=1000, required=True)
    email = forms.CharField(max_length=100, required=True)
    mobile = forms.CharField(max_length=100, required=True)
    # clinic = forms.CharField(max_length=100, required=False)
    # doctor = forms.CharField(max_length=100, required=True)
    # age = forms.CharField(max_length=100, required=False)
    date_of_appointment = forms.CharField(max_length=100, required=False)
    start_time = forms.CharField(max_length=100, required=False)

    # end_time = forms.CharField(max_length=1000, required=False)
    # address = forms.CharField(max_length=1000, required=False)
    # problmes = forms.CharField(max_length=1000, required=False)
    # type_what_you_want = forms.CharField(max_length=1000, required=False)

    class Meta:
        model = patient_appointment_db
        fields = ['first_name', 'email', 'mobile', 'date_of_appointment', 'start_time']

#
# class edit_appointment_form(forms.ModelForm):
#     mr_mrs = forms.CharField(max_length=1000)
#     first_name = forms.CharField(max_length=1000)
#     last_name = forms.CharField(max_length=1000)
#     email = forms.CharField(max_length=100)
#     mobile = forms.CharField(max_length=100)
#     birthdate = forms.CharField(max_length=100)
#     date_of_appointment = forms.CharField(max_length=100)
#     start_time = forms.CharField(max_length=100)
#     end_time = forms.CharField(max_length=1000)
#     address = forms.CharField(max_length=1000)
#     problmes = forms.CharField(max_length=1000)
#     type_what_you_want = forms.CharField(max_length=1000)
#
#     class Meta:
#         model = doctor_appointment_db
#         fields = ['mr_mrs', 'first_name', 'last_name', 'email', 'mobile', 'birtdate', 'date_of_appointment',
#                   'start_time', 'end_time', 'address', 'problmes', 'type_what_you_want']
