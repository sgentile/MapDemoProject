from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from MapDemo.models import Note
from MapDemo.serializers import NoteSerializer


class NoteList(APIView):
    def get(self, request, format=None):
        notes = Note.objects.all()
        serializer = NoteSerializer(notes)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = NoteSerializer(data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
