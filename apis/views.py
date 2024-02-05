# import viewsets
from rest_framework import viewsets

from .models import GeekModel
# import local data
from .serializers import GeekSerializer

# create a viewset


class GeekViewSet(viewsets.ModelViewSet):
    # define queryset
    queryset = GeekModel.objects.all()

    # specify serializer to be used
    serializer_class = GeekSerializer
