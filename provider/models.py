from django.db import models


class ProviderType(models.IntegerChoices):
    Factory = 1, "Завод"
    Retailer = 2, "Розничная сеть"
    Entrepreneur = 3, "Индивидуальный предприниматель"


class Provider(models.Model):
    name = models.CharField(
        max_length=100, unique=True, verbose_name="Provider"
    )
    parent_provider = models.ForeignKey(
        "self",
        on_delete=models.CASCADE,
        null=True,
        verbose_name="Parent provider",
    )
    provider_type = models.IntegerField(
        choices=ProviderType.choices,
        verbose_name="Provider type",
    )
    dept = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, verbose_name="Dept"
    )
    update_at = models.DateTimeField(auto_now=True, verbose_name="Update date")
    create_at = models.DateTimeField(
        auto_now_add=True, verbose_name="Create date"
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Provider"
        verbose_name_plural = "Providers"
