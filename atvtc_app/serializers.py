from rest_framework import serializers
from .models import table


class TableSerialiser(serializers.ModelSerializer):

    class Meta:
        
        model = table
        fields = '__all__'