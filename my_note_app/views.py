from django.shortcuts import render
from rest_framework import viewsets
from my_note_app.models import StateList
from my_note_app.serializers import StateSerializer

# Create your views here.
class StateViewSet(viewsets.ModelViewSet):

    queryset = StateList.objects.all()
    serializer_class = StateSerializer
    # print(serializer_class,'ddddddddddddd')