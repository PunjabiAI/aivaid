# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils.encoding import smart_str
from reportlab.pdfgen import canvas

from aivaid.settings import BASE_DIR
from aivaidapp.models import user_db
from aivaidapp.pkl import load_pickle_model
import numpy as np
from django.contrib.auth.models import User



def pdf_creation(request,predicted_list, pdf_mainlist):
    # print(pdf_mainlist,predicted_list)
    # patient_id = request.user.id
    user_id = request.session['user_id']
    # patient_id = User.objects.get(id=patient_id)
    user_id = user_db.objects.get(user_id=user_id)
    request.session['id'] = user_id.id
    email_Holder = smart_str(user_id.first_name)
    request.session['email_holder'] = email_Holder
    c = canvas.Canvas(BASE_DIR+"/static/pdf_folder/" + smart_str(user_id.id) + ".pdf")
    seal =BASE_DIR+ '/static/pdf_image/ai-vaid-logo.png'
    c.drawImage(seal, 235, 740, width=100, height=100)
    # c.drawString(238, 730, "Disease Prediction")

    c.setFont('Helvetica', 12)
    c.drawString(30, 700, "Name : " + user_id.first_name)
    c.setFont('Helvetica', 12)
    c.drawString(30, 685, "Age group : " + user_id.age)
    c.setFont('Helvetica', 12)
    c.drawString(30, 670, "Location : " + str(user_id.city))
    # c.drawString(30, 670, "Gender : " + request.session['sex'])

    c.setFont('Helvetica', 12)
    c.drawString(450, 700, "Height : " + user_id.height_feet)
    c.setFont('Helvetica', 12)
    c.drawString(450, 685, "Weight : " + user_id.weight)
    c.setFont('Helvetica', 12)
    c.drawString(450, 670, "Gender : " + user_id.gender)
    # c.drawString(450, 670, "Location : " + request.session['location'][0])
    disclamer = " Note: The information you see describes what usually happens with a medical condition, but doesn't apply to everyone."
    disclamer2 = "This information isn't medical advice, so make sure that you contact  health care provider if you have a medical problem. "
    disclamer3 = "If you think you may have a medical emergency, call your doctor or a emergency number immediately."
    if len(predicted_list) != 0:
        c.setLineWidth(.3)
        c.setFont('Helvetica-Bold', 20)
        # print("select_disease2",select_disease2[0])
        c.drawString(238, 640, request.session['selected_disease'])
        y = 620
        smart_str(u'•') == smart_str(u'\u2022')

        for a in range(len(predicted_list)):

            c.setFillColorRGB(0, 0, 0)
            c.setFont('Helvetica-Bold', 16)
            y = y - 30
            c.drawString(15, y, predicted_list[a][0])

            c.setFont('Helvetica-Bold', 16)
            x_len = len(predicted_list[a][0]) * 10
            percent = '54'
            if int(predicted_list[a][1]) > 80:
                c.setFillColorRGB(1, 0, 0)
                percent = 'Severe'
            elif int(predicted_list[a][1]) >= 35 and int(predicted_list[a][1]) <= 80:
                c.setFillColorRGB(0, 0, 1)
                percent = 'Moderate'
            elif int(predicted_list[a][1]) < 35:
                c.setFillColorRGB(0, 1, 0)
                percent = 'Mild'
            c.drawString(x_len, y, '   (' + percent + ')')
            y = y - 20
            pdf_list = str(pdf_mainlist[a])
            pdf_list = pdf_list.split(',')

            for q in range(len(pdf_list)):
                qq = pdf_list[q].replace("['", '').replace("']", '').replace("’", '')
                c.setFont('Helvetica', 12)
                c.setFillColorRGB(0, 0, 0)
                c.drawString(30, y, u'\u2022  ' + qq)
                y = y - 16
                if y < 50:
                    c.showPage()
                    y = 760

        c.setFillColorRGB(0, 0, 0)
        c.setFont('Helvetica', 8)
        y = y - 50
        c.drawString(20, y, disclamer)
        y = y - 11
        c.drawString(20, y, disclamer2)
        y = y - 11
        c.drawString(20, y, disclamer3)

    else:
        c.setFont('Helvetica', 15)
        y = 600
        c.drawString(15, y, "You are fit,if you are still concerned about your health than contact to doctor")

        c.setFillColorRGB(0, 0, 0)
        c.setFont('Helvetica', 8)
        y = y - 50
        c.drawString(20, y, disclamer)
        y = y - 11
        c.drawString(20, y, disclamer2)
        y = y - 11
        c.drawString(20, y, disclamer3)

    c.save()



def predict_disease(request,listas):
    print('hhhhhhhhhhh')
    loaded_model = load_pickle_model(request.session['selected_disease'])
    predicted1 = []
    pdfListMain = []
    print('list_answer_main',listas)
    for ads in range(len(listas)):
        pdfList = []
        pred = listas[ads]
        pred = np.asarray(pred)
        pred = pred.reshape(1, -1)
        result = str(loaded_model.predict(pred))
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
    pdf_creation(request,predicted1, pdfListMain)
    print(predicted1,'kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk')
    return predicted1
