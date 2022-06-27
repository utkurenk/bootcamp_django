from django.db.models import Sum
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# class Account(models.Model):
#    Name = models.CharField(max_length=20, unique=True)
#    balance =
#   def __str__(self):
#       return self.Name


class Transaction(models.Model):
    Type = (("Gelir", "Gelir"),
            ("Gider", "Gider"),
    )
    CategoryChoices = (
        (" ", " "),
        ('Kira', 'Kira'),
        ('Faturalar', 'Faturalar'),
        ('Yemek', 'Yemek'),
        ('Kişisel Harcama', 'Kişisel Harcama'),
        ("Vergi", "Vergi"),
        ('Diğer', 'Diğer'),
    )
    Amount = models.DecimalField(max_digits=20, decimal_places=2)
    Date = models.DateTimeField(default=timezone.now)
    Category = models.CharField(max_length=20, default=" ", choices=CategoryChoices)
    Type = models.CharField(max_length=10, choices=Type)
    Client = models.ForeignKey(User, on_delete=models.CASCADE, null=True)


    class Meta:
        ordering = ('Date',)


