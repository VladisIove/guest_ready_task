from django.db import models
from django.db.models import OuterRef, Subquery
from django.db.models.functions.window import LastValue

from rental.typings import RentalTableTyping


class Rental(models.Model):
    
    name = models.CharField(max_length=220, null=False, blank=False)
    
    def __str__(self) -> str:
        return self.name
    
    class Meta:
        ordering = ['id']
        db_table = 'rental_rental'
        
class Reservation(models.Model):
    
    rental = models.ForeignKey(Rental, on_delete=models.CASCADE)
    checkin = models.DateField(null=False, blank=False)
    checkout = models.DateField(null=False, blank=False)
    
    @classmethod
    def get_reservation_report(cls) -> RentalTableTyping:
        previous_reservation_query = cls.objects.filter(rental=OuterRef('rental'), checkout__lt=OuterRef('checkout')).order_by('-checkout')
        reservation_report = cls.objects.annotate(
            previous_reservation_id = Subquery(previous_reservation_query.values('id')[:1])
        ).values(
            'id', 'previous_reservation_id', 'checkin', 'checkout', 'rental__name'
        )

        return list(reservation_report)
    
    class Meta:
        ordering = ['id']
        db_table = 'rental_reservation'
    