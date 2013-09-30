from django.forms import widgets
from rest_framework import serializers
from MapDemo import models


class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        def __init__(self):
            pass

        model = models.Note