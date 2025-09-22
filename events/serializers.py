from rest_framework import serializers
from .models import Event, Booking

class EventSerializer(serializers.ModelSerializer):
  class Meta:
    model = Event
    fields = '__all__'
  
  def validate(self, data):
    if data['start_date'] > data['end_date']:
      raise serializers.ValidationError("End date cannot be before start date.")
    return data
  
  # def create(self, validated_data):
  #   event = Event.objects.create(
  #     name = validated_data['name'],
  #     location = validated_data['location'],
  #     organizer = validated_data['organizer'],
  #     category = validated_data['category'],
  #     start_date = validated_data['start_date'],
  #     end_date = validated_data['end_date'],
  #   )

  #   return event


class BookingSerializer(serializers.ModelSerializer):
  class Meta:
    model = Booking
    fields = '__all__'
  
    