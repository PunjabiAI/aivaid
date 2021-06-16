import pickle
from django.utils.encoding import smart_str

from aivaid.settings import BASE_DIR
from aivaidapp.models import symptoms_db, disease_db, questions_db


def load_pickle_model(disease_name):
    symptom_list = symptoms_db.objects.filter(symptoms_name=disease_name)
    for symptom_list in symptom_list:
        with open(BASE_DIR+'/uploads/'+smart_str(symptom_list.pkl_file), 'rb') as fid:
            loaded_model = pickle.load(fid)
            return loaded_model


def question_number_point(disease_name):
    list_count = 0
    question_index =[]
    # print(question_index,list_count)
    symptom_list = symptoms_db.objects.filter(symptoms_name=disease_name)
    for symptom_list in symptom_list:
        disease_list = disease_db.objects.filter(symptoms_id=symptom_list.id)
        for disease_list in disease_list:
            questions_list = questions_db.objects.filter(disease_id=disease_list.id)
            list =questions_list.count()
            # print(list)
            list_count = list_count + list
            # print(list_count)
            question_index.append(list_count)

        # print(question_index)
        return question_index

