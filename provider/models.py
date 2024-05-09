from django.db import models


class ProviderType(models.IntegerChoices):
    Factory = 0, "Завод"
    Retailer = 1, "Розничная сеть"
    Entrepreneur = 2, "Индивидуальный предприниматель"


class Provider(models.Model):
    name = models.CharField(
        max_length=100, unique=True, verbose_name="Provider"
    )
    parent_provider = models.ForeignKey(
        "self",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Parent provider",
    )
    provider_type = models.IntegerField(
        choices=ProviderType.choices,
        verbose_name="Provider type",
    )
    dept = models.DecimalField(
        max_digits=10, decimal_places=2, default=0.0, verbose_name="Dept"
    )

    updated_at = models.DateTimeField(
        auto_now=True, verbose_name="Updated date"
    )
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name="Created date"
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Поставщик"
        verbose_name_plural = "Поставщики"


class Contact(models.Model):
    email = models.EmailField(max_length=100, verbose_name="Email")
    country = models.CharField(max_length=50, verbose_name="Country")
    city = models.CharField(max_length=50, verbose_name="City")
    street = models.CharField(max_length=255, verbose_name="Street")
    home = models.CharField(max_length=50, verbose_name="Home")
    provider = models.OneToOneField(
        Provider,
        on_delete=models.CASCADE,
        primary_key=True,
    )

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = "Контакт"
        verbose_name_plural = "Контакты"
