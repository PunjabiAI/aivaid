from superuser import views
from django.conf.urls import url

urlpatterns = [

    url(r'^dashboard/$', views.dashboard, name='dashboard'),
    url(r'^doctorlist/$', views.Doctorlist, name='doctorlist'),
    url(r'^patientlist/$', views.Patientlist, name='patientlist'),
    url(r'^hospitallist/$', views.Hospitallist, name='hospitallist'),
    url(r'^lablist/$', views.Lablist, name='lablist'),
    url(r'^chemistlist/$', views.Chemistlist, name='chemistlist'),
    url(r'^cliniclist/$', views.Cliniclist, name='cliniclist'),
    url(r'^delete-Clinic/(?P<string>[0-9]+)', views.delete_Clinic,
        name='delete_Clinic'),
    ################################################################
    url(r'^addblog/$', views.Addblog, name='addblog'),
    url(r'^bloglist/$', views.Bloglist, name='bloglist'),
    url(r'^Saveblog/$', views.Saveblog, name='Saveblog'),
    url(r'^blogdelete/(?P<uidb64>[0-9A-Za-z_\-]+)$', views.blogdelete, name='blogdelete'),
    url(r'^editblog/(?P<uidb64>[0-9A-Za-z_\-]+)$', views.editblog, name='editblog'),
    url(r'^saveeditblog/$', views.saveeditblog, name='saveeditblog'),
    url(r'^doctorprofile/(?P<uidb64>[0-9A-Za-z_\-]+)$', views.doctorprofile, name='doctorprofile'),
    url(r'^doctorprofile_approve/(?P<uidb64>[0-9A-Za-z_\-]+)$', views.doctorprofile_approve, name='doctorprofile_approve'),
    url(r'^doctorprofile_not_approve/(?P<uidb64>[0-9A-Za-z_\-]+)$', views.doctorprofile_not_approve, name='doctorprofile_not_approve'),
    url(r'^PatientProfile/(?P<uidb64>[0-9A-Za-z_\-]+)$', views.PatientProfile, name='PatientProfile'),

    ##################################################################
    url(r'^category/$', views.category, name='category'),
    url(r'^savecategories/$', views.savecategories, name='savecategories'),
    url(r'^categorydelete/(?P<uidb64>[0-9A-Za-z_\-]+)$', views.categorydelete, name='categorydelete'),
    url(r'^editcategory/(?P<uidb64>[0-9A-Za-z_\-]+)$', views.editcategory, name='editcategory'),
    url(r'^saveeditcategories/$', views.saveeditcategories, name='saveeditcategories'),
    url(r'^categorylist/$', views.categorylist, name='categorylist'),
    ###########################################################################################
    url(r'^appointmentlist/$', views.Appointmentlist, name='appointmentlist'),
    url(r'^delete-Super-Appointment/(?P<string>[0-9]+)', views.delete_Super_Appointment,
        name='delete_Super_Appointment'),
]
