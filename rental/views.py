from django.views.generic import TemplateView

from rental.models import Rental, Reservation


class ReservationReportView(TemplateView):
    template_name = "reservation_report.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['reservation_report'] = Reservation.get_reservation_report()
        return context
