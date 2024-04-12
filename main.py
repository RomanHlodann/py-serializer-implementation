import io

from rest_framework.exceptions import ValidationError
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer

from car.models import Car

from car.serializers import CarSerializer


def serialize_car_object(car: Car) -> bytes:
    serializer = CarSerializer(car)
    if serializer.is_valid():
        return JSONRenderer().render(data=serializer.data)
    raise ValidationError(serializer.errors)


def deserialize_car_object(json: bytes) -> Car:
    stream = io.BytesIO(json)
    data = JSONParser().parse(stream)
    serializer = CarSerializer(data=data)
    if serializer.is_valid():
        return serializer.save()
    raise ValidationError(serializer.errors)
