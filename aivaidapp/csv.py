# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from aivaidapp.models import symptoms_db, disease_db, questions_db


def load_csv(disease):
    all_list = []
    symptom_list = symptoms_db.objects.filter(symptoms_name=disease)
    for symptom_list in symptom_list:
        disease_list = disease_db.objects.filter(symptoms_id=symptom_list.id)
        for disease_list in disease_list:
            questions_list = questions_db.objects.filter(disease_id=disease_list.id)
            final_questions_list = []
            for questions_list in questions_list:
                final_questions_list.append(questions_list.questions_name)
                # print(final_questions_list)
            all_list.append(final_questions_list)
    return all_list


