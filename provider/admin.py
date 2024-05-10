from django.contrib import admin
from provider.models import Provider, Contact, Product
from django.db.models import QuerySet


class ContactInline(admin.TabularInline):
    """
    Panel for contact in provider admin
    """

    model = Contact


@admin.register(Provider)
class ProviderAdmin(admin.ModelAdmin):
    """
    Admin panel for provider
    """

    list_display = ("name", "provider_type", "parent_provider", "dept")
    list_filter = ("provider_type", "contact__city")
    actions = ["dept_clear"]
    inlines = [ContactInline]

    @admin.action(description="Clear dept")
    def dept_clear(self, request, queryset: QuerySet):
        """
        Clear dept func
        """
        queryset.update(dept=0.0)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """
    Admin panel for product
    """

    list_display = ("name", "model_product")
    list_filter = ("provider__provider_type", "provider__contact__city")
