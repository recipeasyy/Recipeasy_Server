from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from measure.models import Measurement
from measure.serializers import MeasurementSerializer


class MeasurementView(APIView):
    def get(self):
        measurements = Measurement.objects.all()
        measurements_serializer = MeasurementSerializer(measurements, many=True)

        return Response({"Measurements": measurements_serializer.data}, status=status.HTTP_200_OK)