from django.urls import path
from .views import EventView, BookingView

urlpatterns = [
    path('admin/book/<int:id>/', BookingView.as_view(), name='get_book'),
    path('admin/book/', BookingView.as_view(), name='create_book'),
    path('admin/crud/', EventView.as_view(), name='crud'),
    path('admin/crud/<int:id>/', EventView.as_view(), name='delete'),
]
