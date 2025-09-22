from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import EventSerializer, BookingSerializer
from rest_framework.response import Response
from rest_framework import status
from .models import Event, Booking
from accounts.models import CustomUser

# Create your views here.
class EventView(APIView):

  def post(self, request):
    serializer = EventSerializer(data = request.data)
    if serializer.is_valid():
      serializer.save()
      return Response({'message': "Event created successfully"}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

  def get(self, request, id = None):
    try:
      if id:
        data = Event.objects.get(pk=id)
        serializer = EventSerializer(data)
        return Response({'event': serializer.data}, status=status.HTTP_200_OK)
      else:
        data = Event.objects.all()
        serializer = EventSerializer(data, many=True)
        return Response({'results': serializer.data}, status=status.HTTP_200_OK)
    except Exception as e:
      return Response({'error': 'Could not retrieve events. Please try again later.'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

  def delete(self, request, id):
    try:
      data = Event.objects.get(pk=id)
      data.delete()
      return Response({'success': 'Event Deleted Successfully!'}, status=status.HTTP_204_NO_CONTENT)
    except Event.DoesNotExist as e:
      return Response({'error': str(e.err)}, status=status.HTTP_404_NOT_FOUND)

  def put(self, request, id):
    try:
      data = Event.objects.get(pk=id)
      serializer = EventSerializer(data, data = request.data)
      if serializer.is_valid():
        serializer.save()
        return Response({'success': 'Event Updated Successfully', 'event': serializer.data}, status=status.HTTP_200_OK)
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
      return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

class BookingView(APIView):
  def post(self, request):
    try:
      serializer = BookingSerializer(data=request.data)
      if(serializer.is_valid()):
        serializer.save()
        return Response({'success': 'Successfully Booked Tickets'}, status=status.HTTP_201_CREATED)
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
      return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

  def get(self, request, id):
    try:
      user = CustomUser.objects.get(pk=id)
      bookings = user.bookings.all()
      serializer = BookingSerializer(bookings, many=True)
      print(serializer.data)
      return Response({'results': serializer.data},status=status.HTTP_200_OK)
    except CustomUser.DoesNotExist:
        return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
      return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
