from django.db import models
from django.contrib.auth.models import User


class TaxDeclaration(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    code = models.CharField(max_length=20, unique=True)
    declaration_type = models.CharField(max_length=100)
    submitted_at = models.DateTimeField()
    amount_declared = models.DecimalField(max_digits=12, decimal_places=2)
    amount_paid = models.DecimalField(max_digits=12, decimal_places=2, default=0)

    def __str__(self):
        return self.user
    
    class Meta:
        verbose_name = "Mokėsčiai"
        verbose_name_plural = "Mokėsčiai"


