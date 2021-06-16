
from django.conf.urls import include, url



# from myapp.views import get_queryset
from apiapp.views import Symptoms_list, Disease_Filter_by_Symptoms_id, questions_Filter_by_disease_id, Check_up_save, \
    result_api

urlpatterns = [
    # # url('device/(?P<device_name>[\w\-]+)', UserViewSet.as_view(), name="device")
    # url('filter_by_symptoms_id/(?P<unique_id>[0-9A-Za-z_\-!@#$%^&*()]+)', Listquestions_Filter_by_Symptoms_id.as_view(), name="filter_by_symptoms_id"),
    url('Disease_Filter_by_Symptoms_id/(?P<unique_id>[0-9A-Za-z_\-!@#$%^&*()]+)', Disease_Filter_by_Symptoms_id, name="Disease_Filter_by_Symptoms_id"),
    url('questions_Filter/(?P<symptoms_id>[0-9A-Za-z_\-!@#$%^&*()]+)/(?P<disease_id>[0-9A-Za-z_\-!@#$%^&*()]+)', questions_Filter_by_disease_id, name="questions_Filter"),
    # url('list_symptoms', List_symptoms_db.as_view(), name="list_symptoms"),
    url('Symptoms_list', Symptoms_list, name="Symptoms_list"),
    url('Check_up_save', Check_up_save.as_view(), name="Check_up_save"),
    url('result_api', result_api, name="result_api"),

    # url('central/(?P<unique_id>[0-9A-Za-z_\-!@#$%^&*()]+)', Central_Device_Api_check, name="central"),
    # url('central_post', Central_Device_Api_Post, name="central"),
]