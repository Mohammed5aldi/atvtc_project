from django.shortcuts import render
from django.http import HttpResponse
from .models import table
from rest_framework import viewsets
from .serializers import TableSerialiser

# Create your views here.



class TableViewSet(viewsets.ModelViewSet):

    queryset = table.objects.all()
    serializer_class = TableSerialiser





def index(request):
    tables = table.objects.all()

    data = {
        'tables': tables
    }
    return render(request , 'index.html' , context=data)