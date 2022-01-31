from .serializers import TownSerializer
from .permissions import IsAdminAuthenticated
from .models import Town


from django.core.exceptions import FieldError

from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.response import Response
from rest_framework import serializers, status

# Create your views here.

#API Town
class TownViewset(ReadOnlyModelViewSet):

    #Defined serializer_class
    serializer_class = TownSerializer

    #Defined permissions
    permission_classes = [IsAdminAuthenticated]

    #Define the queryset we will use
    def get_queryset(self):

        queryset = Town.objects.all()

        return queryset
    
    #Redefine what to do when GET call on list
    def list(self,request, *args, **kwargs):
        
        # Cleaning filters
        tmpFilters = self.request.GET.get('filters')
  
        #Check if filters not empty
        if (not(tmpFilters == None)) and (not(tmpFilters == "")):
            filters = {}

            #Formating
            tmpFilters = tmpFilters.replace("\n", "").replace('"', '').replace("{", "").replace("}", "").replace(":", ",")
            tmpFilters = tmpFilters.split(",")

            #Store values in a dict
            for i in range(0,len(tmpFilters)-1,2):
                filters[tmpFilters[i]] = tmpFilters[i+1].lstrip()
                #Check if query is correctly formatted
                if ("field" in tmpFilters[i+1]) or ("value" in tmpFilters[i+1]) or ("predicate" in tmpFilters[i+1]):
                    raise serializers.ValidationError({"Error" : "wrong format for '{}' you might have forgotten a comma or a colon.".format(tmpFilters[i])})
            
            #Check for field parameter
            if 'field' in filters:
                field = filters['field']
            else:
                raise serializers.ValidationError({"Error" : "'field' is required."})

            #Check for value parameter
            if 'value' in filters:
                value = filters['value']
            else:
                raise serializers.ValidationError({"Error": "'value' is required."})

            #Check for predicate parameter
            if 'predicate' in filters:
                predicate = filters['predicate']
            #If there is no value then we will use 'eq'
            else:
                predicate = "eq"
            
            #If the predicate is eq then its queryset will be filtered with "__exact"
            if predicate == "eq" :
                #Catch errors in order to send them to the user
                try:
                    queryset = self.get_queryset().filter(**{field+'__exact': value})
                except (ValueError, FieldError)as e:
                    raise serializers.ValidationError({"Error" : str(e)})
            
            #If the predicate is eq then its queryset will be filtered with "__gt"
            if predicate == "gt" :
                #Catch errors in order to send them to the user
                try:
                    queryset = self.get_queryset().filter(**{field+'__gt': value})
                except (ValueError, FieldError) as e:
                    raise serializers.ValidationError({"Error" : str(e)})
            
            #If the predicate is eq then its queryset will be filtered with "__lt"
            if predicate == "lt" :
                #Catch errors in order to send them to the user
                try:
                    queryset = self.get_queryset().filter(**{field+'__lt': value})
                except (ValueError, FieldError) as e:
                    raise serializers.ValidationError({"Error" : str(e)})
            
            #If the predicate is eq then its queryset will be filtered with "__contains"
            if predicate == "contains" :
                #Catch errors in order to send them to the user
                try:
                    queryset = self.get_queryset().filter(**{field+'__contains': value})
                except (ValueError, FieldError) as e:
                    raise serializers.ValidationError({"Error" : str(e)})
            
            #Check if the request got any result in the queryset
            if len(queryset) > 0:
                #Finally we serialize the queryset we've just filtered
                serializer = TownSerializer(queryset,context={'request': request}, many=True)
                return Response(serializer.data)
            else:
                return Response({"Error" : "No result found."}, status=status.HTTP_404_NOT_FOUND)

        # If there is no filter, just get the query from get_queryset() and serialize them
        else:
            queryset = self.get_queryset()
            serializer = TownSerializer(queryset,context={'request': request}, many=True)
            return Response(serializer.data)
    
    

    