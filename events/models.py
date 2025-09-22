from django.db import models
from accounts.models import CustomUser

# Create your models here.
class Event(models.Model):
  category_choices = (
    ('conference', 'Conference'),
    ('workshop', 'Workshop'),
    ('concert', 'Concert'),
    ('festival', 'Festival'),
  )
  
  name = models.CharField(max_length=50)
  location = models.CharField(max_length=50)
  organizer = models.CharField(max_length=50)
  category = models.CharField(max_length=50, choices=category_choices)
  start_date = models.DateField()
  end_date = models.DateField()
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)


  def __str__(self):
    return f"{self.name} - {self.organizer} ({self.category})"

class Booking(models.Model):
  name = models.CharField(max_length=50)  # more realistic
  email = models.EmailField()  # no need for max_length
  phone = models.CharField(max_length=15)  # enough for international numbers
  tickets = models.PositiveIntegerField()  # avoids negative ticket values
  event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name="bookings")
  user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="bookings")
  created_at = models.DateTimeField(auto_now_add=True)  # booking time

  def __str__(self):
    return f"{self.name} - {self.tickets} tickets for {self.event}"
  
