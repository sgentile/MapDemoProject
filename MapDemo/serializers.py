from django.forms import widgets
from rest_framework import serializers
from django.db import models


class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        def __init__(self):
            pass

        model = models.Note