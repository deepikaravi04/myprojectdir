from django.db import models
from django.core.validators import RegexValidator

class RoomDetails(models.Model):
    hostel_number = models.CharField(max_length=100)
    floor_number = models.CharField(max_length=100)
    room_no = models.CharField(max_length=100)
    bed_number = models.CharField(max_length=100)

    class Meta:
        unique_together = ('hostel_number', 'floor_number', 'room_no', 'bed_number')

    def __str__(self):
        return f"Room {self.hostel_number} - Floor {self.floor_number} - Bed {self.bed_number}"


class Hosteller(models.Model):
    full_name = models.CharField(max_length=100)
    joint_fee = models.CharField(max_length=100)
    advance_amount = models.IntegerField()
    rent_amount = models.CharField(max_length=100)
    phone_number = models.CharField(
        max_length=10,
        validators=[RegexValidator(r'^\d{10}$', 'Enter a valid 10-digit phone number')]
    )
    join_date = models.DateField()
    is_active = models.BooleanField(default=True)
    room_details = models.ForeignKey(RoomDetails, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.full_name


class RentHistory(models.Model):
    PAYMENT_METHOD_CHOICES = [
        ('CASH', 'Cash'),
        ('CARD', 'Card'),
        ('BANK_TRANSFER', 'Bank Transfer'),
        ('UPI', 'UPI'),
    ]

    hosteller = models.ForeignKey(Hosteller, on_delete=models.CASCADE)
    payment_method = models.CharField(max_length=100, choices=PAYMENT_METHOD_CHOICES)
    payer_phone_number = models.CharField(
        max_length=10,
        validators=[RegexValidator(r'^\d{10}$', 'Enter a valid 10-digit phone number')]
    )
    payment_date = models.DateField()

    def __str__(self):
        return f"Rent history for {self.hosteller.full_name} on {self.payment_date}"
