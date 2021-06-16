# Create your views here.
import pickle
from django.utils.encoding import smart_str
from django.views.decorators.csrf import csrf_exempt
from rest_framework import generics, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
import numpy as np
from aivaid.settings import BASE_DIR
from aivaidapp.models import user_db, questions_db, symptoms_db, disease_db, symptoms_type
from apiapp.serializers import symptoms_dbSerializer, CheckUP_db_serializers
import ast

from django.utils.translation import gettext as _


class Check_up_save(APIView):
    def post(self ,request, *args, **kwargs):
        serializer = CheckUP_db_serializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            aaaaaa = serializer.data
            return Response({'status': True, 'message':'sucessfully', 'user':aaaaaa }, status=status.HTTP_200_OK)
        return Response({'status': False, 'message':serializer.errors}, status=status.HTTP_400_BAD_REQUEST,)

@csrf_exempt
@api_view(["GET"])
def Symptoms_list(request,*args, **kwargs):
    queryset = symptoms_type.objects.all()
    list =[]
    for queryset in queryset:
        dic = {}
        dic.update(id=queryset.id)
        dic.update(symptoms_type_name=queryset.symptoms_type_name)
        symptoms_list = symptoms_db.objects.filter(symptoms_type_id=queryset.id)
        main_list =[]
        for symptoms_list in symptoms_list:
            abc={}
            abc.update(id=symptoms_list.id)
            abc.update(name=symptoms_list.symptoms_name)
            main_list.append(abc)
        dic.update(symptoms=main_list)
        list.append(dic)
    return Response({'status': True, 'id_list':list}, status=status.HTTP_200_OK)


@csrf_exempt
@api_view(["GET"])
def Disease_Filter_by_Symptoms_id(request,*args, **kwargs):
    unique_id =kwargs['unique_id']
    abc = disease_db.objects.filter(symptoms_id=unique_id)
    list = []
    count___ =0
    for abc in abc:
        dic ={}
        dic.update(id=abc.id )
        questions = questions_db.objects.filter(disease_id=abc.id)
        questions_list =[]
        for questions in questions:
            ans ={}
            ans.update(questions=questions.questions_name)
            count___ += 1
            ans.update(count=count___)
            questions_list.append(ans)
        dic.update(questions=questions_list)
        list.append(dic)
    return Response({'status': True, 'id_list':list,'list_count':count___}, status=status.HTTP_200_OK)


@csrf_exempt
@api_view(["GET"])
def questions_Filter_by_disease_id(request,*args, **kwargs):
    symptoms_id =kwargs['symptoms_id']
    disease_id =kwargs['disease_id']
    list_count= questions_db.objects.filter(symptoms_id=symptoms_id).count()
    abc = questions_db.objects.filter(disease_id=disease_id)
    list = []
    for abc in abc:
        list.append(abc.questions_name)
    return Response({'status': True, 'qustions_list':list,'list_count':list_count}, status=status.HTTP_200_OK)

def predict_disease_api(listas,loaded_model):
    predicted1 = []
    pdfListMain = []
    for ads in range(len(listas)):
        pdfList = []
        pred = listas[ads]
        pred = np.asarray(pred)
        pred = pred.reshape(1, -1)
        result = str(loaded_model.predict(pred))
        print(result,'+++++++++++++++++++++++++')
        result = result.replace('[', '').replace(']', '').replace("'", '')
        if str(result) == 'No Result ,0' or str(result) == 'No Result,0':
            pass
        else:
            result = result.split('-')
            pdfList.append(result[1])
        if len(pdfList) != 0:
            pdfListMain.append(pdfList)
        if str(result) == 'No Result ,0' or str(result) == 'No Result,0':
            print("no result")
        else:
            predicted1.append(result[0].split(','))
    if int(len(predicted1)) == 0:
        print("You are fit,if you are still concerned about your health than contact to doctor")
    else:
        print("model_predict", predicted1)
    return predicted1


def model_loads(symptoms_id):
    symptom_list = symptoms_db.objects.filter(id=symptoms_id)
    for symptom_list in symptom_list:
        with open(BASE_DIR + '/uploads/' + smart_str(symptom_list.pkl_file), 'rb') as fid:
            loaded_model = pickle.load(fid)
            return loaded_model


@csrf_exempt
@api_view(["POST"])
def result_api(request,*args, **kwargs):
        ans_list = request.data['ans_list']
        ans_list = ast.literal_eval(ans_list)
        user_id =int(request.data['user_id'])
        symptoms_id =int(request.data['symptoms_id'])
        list_count_ans =int(request.data['list_count'])
        loaded_model= model_loads(symptoms_id)
        li = ans_list
        main_list=[]
        for i in range(len(li)):
            temp = []
            for i in range(list_count_ans):
                temp.append(0)
            main_list.append(temp)
        for i in range(len(li)):
            for j in range(len(li[i])):
                main_list[i][li[i][j] - 1] = 1
        result111= predict_disease_api(main_list,loaded_model)

        temp = []
        lis = []

        for i in result111:
            dict = {}
            if i[0] not in temp:
                dict.update(name=i[0])
                dict.update(value=i[1])
                temp.append(i[0])
                lis.append(dict)
        return Response({'status': True, 'result111':lis}, status=status.HTTP_200_OK)

