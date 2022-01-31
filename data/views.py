
from rest_framework.viewsets import ReadOnlyModelViewSet
from .serializers import TownSerializer
from .permissions import IsAdminAuthenticated

from .models import Town

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
    
    

    