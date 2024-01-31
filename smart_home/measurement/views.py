# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.response import Response

from .serializers import SensorSerializer, SensorDetailSerializer, MeasuremetDetailSerializer
from .models import Sensor, Measurement

class SensorsView(ListAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer

    def post(self, request):
        Sensor.objects.create(
            name=request.POST.get('name'),
            descripcion=request.POST.get('description')
        )
        return ({'status':'Ok'})

class SensorView(RetrieveAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer

    def patch(self, request, pk):
        sensor = Sensor.objects.get(id=pk)
        sensor.description = request.data['description']
        sensor.save()
        return Response({'Status':'Ok'})

class MearsurementsView(ListAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasuremetDetailSerializer

    def post(self, request):
        Measurement.objects.create(
            sensor_id=request.POST.get('sensor'),
            temperature=request.POST.get('temperature')
        )
        return Response({'status':'Ok'})