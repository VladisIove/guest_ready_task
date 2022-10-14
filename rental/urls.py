from django.urls import path

from rental.views import ReservationReportView

urlpatterns = [
    path('', ReservationReportView.as_view(), name='reservation-report')
]
