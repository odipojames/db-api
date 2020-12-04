from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from . models import *
from .serializers import TrackingSerializer
# Create your views here.


class TrackingAPIView(generics.ListAPIView):
    """listing all traccking history,sample reg_number { KAB254B,KAQ254Q }"""

    serializer_class =TrackingSerializer
    renderer_classes = (JSONRenderer,)

    def get_queryset(self):
        reg_number = self.kwargs['reg_number']
        return Track.objects.filter(tracking__reg_number=reg_number)

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data, status.HTTP_200_OK)
