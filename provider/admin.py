from django.contrib import admin
from provider.models import Provider, Contact
from django.db.models import QuerySet


@admin.register(Provider)
class ProviderAdmin(admin.ModelAdmin):
    list_display = ("name", "provider_type", "parent_provider", "dept")
    list_filter = ("provider_type",)
    actions = ["dept_clear"]

    @admin.action(description="Clear dept")
    def dept_clear(self, request, queryset: QuerySet):
        queryset.update(dept=0.0)


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ("email", "country", "city", "street", "home")
    list_filter = ("city",)
