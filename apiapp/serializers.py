from rest_framework import serializers
from aivaidapp.models import symptoms_db, disease_db, questions_db, user_db


class symptoms_dbSerializer(serializers.ModelSerializer):
    class Meta:
        model = symptoms_db
        fields = '__all__'



class disease_dbSerializer(serializers.ModelSerializer):
    class Meta:
        model = disease_db
        fields = '__all__'

        # def get_queryset(self):
        #     """
        #     This view should return a list of all the purchases for
        #     the user as determined by the username portion of the URL.
        #     """
        #     unique_id = self.kwargs['unique_id']
        #     return disease_db.objects.filter(unique_id=unique_id)
        # abc = disease_db.objects.filter(symptoms_id=unique_id)


class questions_dbSerializer(serializers.ModelSerializer):
    class Meta:
        model = questions_db
        fields = ['questions_name']



class CheckUP_db_serializers(serializers.ModelSerializer):
    class Meta:
        model = user_db
        fields ='__all__'


# class Perdictions_serializers(serializers.Serializer):
#     user_id = serializers.CharField(max_length=100)
#     symptoms_id = serializers.CharField(max_length=1000)
#     list_count_ans = serializers.CharField(max_length=1000)
#     ans_list =serializers.CharField(max_length=900000)


