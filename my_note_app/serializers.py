from rest_framework import serializers
from my_note_app.models import StateList

class StateSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = StateList
        fields = ['id','name','code']
