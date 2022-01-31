from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import Town
from rest_framework.response import Response
from rest_framework import status

class DynamicFieldsTownSerializer(serializers.ModelSerializer):
    """
    A ModelSerializer that takes an additional 'fields' argument that
    controls which fields should be displayed.
    """

    def __init__(self, *args, **kwargs):
        super(DynamicFieldsTownSerializer, self).__init__(*args, **kwargs)

        #Get Field parameter from request
        fields = self.context['request'].query_params.get('fields')

        if fields:

            #Check if query is correctly formatted
            if (fields.replace('"', '') == fields) or (fields.replace('[', '') == fields) or (fields.replace(']', '') == fields) :
                raise serializers.ValidationError({"Error" : "Wrong format, 'fields' key value should be ['fields1','fields2',...]."})
            fields = fields.replace('"', '').replace(" ", "").replace("[", "").replace("]", "")
            fields = fields.split(",")

            #Get requested fields from the request and existing fields in the model 'Town'
            requested = set(fields)
            existing = set(self.fields.keys())
            
            #Check if requested field exists in schema 
            if not requested.issubset(existing):
                errorSet = set()
                for field_name in requested - existing:
                    errorSet.add(field_name)
                raise serializers.ValidationError({"Error" : "{} not found, valid fields are : {}.".format(errorSet,existing)})

            #Keep only requested fields
            for field_name in existing - requested:
                self.fields.pop(field_name)
                



class TownSerializer(DynamicFieldsTownSerializer, serializers.HyperlinkedModelSerializer):
    """
    The Serializer for the 'Town' model.
    """

    class Meta:
        model = Town
        fields = ['code','name','population','average_age','district_code','department_code','region_code','region_name'] 
        