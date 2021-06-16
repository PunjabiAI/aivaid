"""aivaid URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views as auth_views
from aivaid import settings
from aivaidapp.form import EmailValidationOnForgotPassword
from patientapp import views as patientapp_views
from doctorapp import views as doctorapp_views
from aivaidapp import views
from aivaid.settings import DEBUG
from django.views.static import serve

from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),
                url(r'^i18n/', include('django.conf.urls.i18n')),
                url(r'^language/', views.setlanguage, name='language'),

                # url(r'^rosetta/', include('rosetta.urls')),

               url('api/(?P<version>(v1|v2))/', include('apiapp.urls')),
               url(r'^auth/', include('social_django.urls', namespace='social')),  # <- Here
               url(r'^superuser/', include('superuser.super_urls', namespace='superuser')),  # <- Here
               url(r'^signup/$', views.register, name='signup'),
               url(r'^login/$', views.user_login, name='login'),
               url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
                   views.activate, name='activate'),
               url(r'^logout/$', auth_views.logout, {'next_page': '/'}, name='logout'),

               url(r'^$', views.index, name='index'),

               url(r'^password_reset/$', auth_views.password_reset,
                   {'template_name': 'password/password_reset_form.html',
                    'html_email_template_name': 'password/password_reset_email.html','password_reset_form': EmailValidationOnForgotPassword}, name='password_reset'),


               url(r'^password_reset/done/$', auth_views.password_reset_done,
                   {'template_name': 'password/password_reset_done.html'}, name='password_reset_done'),
               url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
                   auth_views.password_reset_confirm, {'template_name': 'password/password_reset_confirm.html'},
                   name='password_reset_confirm'),
               url(r'^reset/done/$', auth_views.password_reset_complete,
                   {'template_name': 'password/password_reset_complete.html'}, name='password_reset_complete'),
               url(r'^change_password/$', views.change_password, name='change_password'),

               url(r'^start-checkup/$', views.start_checkup, name='start-checkup'),
               url(r'^patient', views.patient, name='patient'),
               url(r'^Coronavirus', views.corona, name='Coronavirus'),
               url(r'^symtoms/$', views.symtoms, name='symtoms'),
               url(r'^male/$', views.male, name='male'),
               url(r'^female/$', views.female, name='female'),
               url(r'^locations/$', views.locations, name='locations'),
               url(r'^question/$', views.question, name='question'),
               url(r'^questions', views.questions, name='questions'),
               url(r'^result/$', views.check_results, name='result'),
               url(r'^send_mails/$', views.send_mails, name='send_mails'),
               url(r'^confirm-appointment/(?P<uidb64>[0-9A-Za-z_\-]+)/$', views.confirm_appointment,
                   name='confirm_appointment'),
               url(r'^instamojo', views.instamojo, name="instamojo"),
               url(r'^list', views.list_payments, name="list"),
               url(r'^pay-later/(?P<string>[\w\-]+)', views.pay_later),
               url(r'^book_appointment_pat/$', views.book_appointment_pat, name='book_appointment_pat'),
               url(r'^confirm_appointment_save/$', views.confirm_appointment_save, name='confirm_appointment_save'),

               url(r'^appointment-success/(?P<uidb64>[0-9A-Za-z_\-]+)$', views.appointment_success,
                   name='appointment_success'),

               url(r'^contact-us/$', views.contact_us, name='contact_us'),
               url(r'^about-us/$', views.about_us, name='about-us'),
               url(r'^visitor-guide/$', views.patient_visitor_guide, name='visitor_guide'),
               url(r'^terms-conditions/$', views.terms_conditions, name='terms-conditions'),
               url(r'^privacy-policy/$', views.privacy, name='privacy-policy'),
               url(r'^blogs/$', views.blogs, name='blogs'),
               url(r'^blog/(?P<uidb64>[0-9A-Za-z_\-]+)$', views.blog_single, name='blog'),

               url(r'^find-doctor/$', views.find_doctor, name='find_doctor'),
               url(r'^doctordetail/(?P<uidb64>[0-9A-Za-z_\-]+)$', views.doctordetail, name='doctordetail'),
               url(r'^newcounsultation/$', views.newcounsultation, name='newcounsultation'),
               url(r'^Review_feedback/$', views.Review_feedback, name='Review_feedback'),

               url(r'^doctor-full-profile/(?P<uidb64>[0-9A-Za-z_\-]+)$', views.doctor_full_profile,
                   name='doctor_full_profile'),
               url(r'^send-subscription/$', views.send_subscription, name='send-subscription'),

               url(r'^for-doctor/$', views.for_doctor, name='for-doctor'),

               # Doctor Folder url here -----------------------------------------
               url(r'^doctor-panel/$', doctorapp_views.aivaid_admin, name='doctor-panel'),
               url(r'^mobile_verify_doctor/$', doctorapp_views.mobile_verify_doctor, name='mobile_verify_doctor'),
               url(r'^otp_verify_doctor/$', doctorapp_views.otp_verify_doctor, name='otp_verify_doctor'),
               url(r'^resend_otp_verify_doctor/$', doctorapp_views.resend_otp_verify_doctor, name='resend_otp_verify_doctor'),
               url(r'^doctor-profile/$', doctorapp_views.doctor_profile, name='doctor-profile'),
               url(r'^clinic-details/$', doctorapp_views.clinic_details, name='clinic-details'),
               url(r'^delete_clinic_details/(?P<string>[0-9]+)', doctorapp_views.delete_clinic_details, name='delete_clinic_details'),
               url(r'^add_clinic_details/$', doctorapp_views.add_clinic_details, name='add_clinic_details'),
               url(r'^edit_clinic_details/$', doctorapp_views.edit_clinic_details, name='edit_clinic_details'),
               url(r'^save_clinic_pic/$', doctorapp_views.save_clinic_pic, name='save_clinic_pic'),



               url(r'^appointment-list/$', doctorapp_views.appointment_list, name='appointment-list'),
               url(r'^appointment-Check/(?P<string>[\w\-]+)', doctorapp_views.appointment_Check),
               url(r'^appointment-accept/', doctorapp_views.appointment_accept),
               url(r'^appointment-decline/', doctorapp_views.appointment_decline),
               url(r'^appointments-today/$', doctorapp_views.appointments_today, name='appointments-today'),
               url(r'^patient-profile/(?P<patient_id>[0-9]+)', doctorapp_views.patient_profile,
                   name='patient-profile'),
               url(r'^appointmente_delete/(?P<appoitment_id>[0-9]+)', doctorapp_views.appointmente_delete,
                   name='appointmente_delete'),
               url(r'^doctor-patient-list/$', doctorapp_views.patient_list, name='doctor-patient-list'),
               url(r'^patient-report/$', doctorapp_views.patient_report, name='patientreport'),
               url(r'^report-update/(?P<id>[0-9]+)', doctorapp_views.report_update, name='report-update'),
               url(r'^doctor-profile/$', doctorapp_views.doctor_profile, name='doctor-profile'),
               url(r'^edit-doctor-profile/(?P<doctor_id>[0-9]+)', doctorapp_views.edit_doctor_profile,
                   name='edit-doctor-profile'),
               url(r'^save_doctor_profile_edit_data', doctorapp_views.save_doctor_profile_edit_data,
                   name='save_doctor_profile_edit_data'),
               url(r'^add-to-patlist/(?P<string>[\w\-]+)', doctorapp_views.add_to_patlist),
               url(r'^remove-from-patlist/(?P<string>[\w\-]+)', doctorapp_views.remove_from_patlist),
               url(r'^add-report/$', doctorapp_views.add_report, name='add-report'),
               url(r'^read-notification-doc/(?P<string>[\w\-]+)', doctorapp_views.read_notification_doc),
               url(r'^notice-list-doc/$', doctorapp_views.notice_list_doc, name='notice-list-doc'),
               url(r'^notice-list/$', doctorapp_views.notice_list, name='notice-list'),
               url(r'^add-notice/$', doctorapp_views.add_notice, name='add-notice'),
               url(r'^report-list/$', doctorapp_views.report_list, name='report-list'),
               url(r'^addservices/$', doctorapp_views.addservices, name='addservices'),
               url(r'^serviceslist/$', doctorapp_views.serviceslist, name='serviceslist'),
               url(r'^transactions/$', doctorapp_views.transactions, name='transactions'),

               ################################################################
               url(r'^addblog/$', doctorapp_views.Addblog, name='addblog'),
               url(r'^bloglist/$', doctorapp_views.Bloglist, name='bloglist'),
               url(r'^Saveblog/$', doctorapp_views.Saveblog, name='Saveblog'),
               url(r'^blogdelete/(?P<uidb64>[0-9A-Za-z_\-]+)$', doctorapp_views.blogdelete, name='blogdelete'),
               url(r'^editblog/(?P<uidb64>[0-9A-Za-z_\-]+)$', doctorapp_views.editblog, name='editblog'),
               url(r'^saveeditblog/$', doctorapp_views.saveeditblog, name='saveeditblog'),

               ##################################################################
               url(r'^category/$', doctorapp_views.category, name='category'),
               url(r'^savecategories/$', doctorapp_views.savecategories, name='savecategories'),
               url(r'^categorydelete/(?P<uidb64>[0-9A-Za-z_\-]+)$', doctorapp_views.categorydelete, name='categorydelete'),
               url(r'^editcategory/(?P<uidb64>[0-9A-Za-z_\-]+)$', doctorapp_views.editcategory, name='editcategory'),
               url(r'^saveeditcategories/$', doctorapp_views.saveeditcategories, name='saveeditcategories'),
               url(r'^categorylist/$', doctorapp_views.categorylist, name='categorylist'),
               ###########################################################################################



               # +++++++++++++++++++++++++++++++++++++Patient Panel+++++++++++++++++++++++++++++++++++#

               url(r'^dashboard-patient/$', patientapp_views.patient_admin, name='dashboard_patient'),
               url(r'^account-details/$', patientapp_views.account_details, name='account-details'),
               url(r'^profile/$', patientapp_views.profile, name='profile'),
               url(r'^editpatient', patientapp_views.profile_edit, name='editpatient'),
               url(r'^online-consultation/$', patientapp_views.online_consultation, name='online-consultation'),
               url(r'^appointments-list/$', patientapp_views.appointments_list, name='appointments-list'),
               url(r'^medical-record/$', patientapp_views.medical_record, name='medical-record'),
               url(r'^add_medical_record/$', patientapp_views.add_medical_record, name='add_medical_record'),
               url(r'^edit_medical_record/$', patientapp_views.edit_medical_record, name='edit_medical_record'),
               url(r'^medical_record_delete/(?P<record_id>[0-9]+)$', patientapp_views.medical_record_delete,
                   name='medical_record_delete'),
               url(r'^notifications/$', patientapp_views.notifications, name='notifications'),
               url(r'^transaction-list/$', patientapp_views.transaction_list, name='transaction-list'),
               url(r'^notice-list-pat/$', patientapp_views.notice_list_pat, name='notice-list-pat'),
               url(r'^read-notification-pat/(?P<string>[\w\-]+)', patientapp_views.read_notification_pat),
               url(r'^delete-patient-Appointment/(?P<string>[\w\-]+)', patientapp_views.delete_patient_Appointment),
               url(r'^del-Service/(?P<string>[\w\-]+)', patientapp_views.del_Service),
               url(r'^faqs', patientapp_views.faqs),
               url(r'^undermaintenance/$', views.undermaintenance, name='undermaintenance'),
               url(r'^google55fc80e83a72caed.html/$', views.google55fc80e83a72caed,
                   name='google55fc80e83a72caed.html'),

               ] 
if DEBUG == True:
   urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

else:
   urlpatterns += [ url(r'^static/(?P<path>.*)$', serve, { 'document_root': settings.STATIC_ROOT }), ]

handler404 = views.handler
handler500 = views.handler50
