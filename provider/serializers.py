from rest_framework.serializers import ModelSerializer
from provider.validators import ProviderTypeValidator
from .models import Provider, Contact


class ContactSerializer(ModelSerializer):
    """
    Serializer for contact
    """

    class Meta:
        model = Contact
        fields = [
            "email",
            "country",
            "city",
            "street",
            "home",
        ]


class ProviderSerializer(ModelSerializer):
    """
    Serializer for provider
    """

    contact = ContactSerializer(many=False)

    class Meta:
        model = Provider
        read_only_fields = [
            "dept",
        ]

        fields = [
            "id",
            "name",
            "provider_type",
            "parent_provider",
            "contact",
            "dept",
        ]
        validators = [ProviderTypeValidator]

    def create(self, validated_data):
        """
        Create provider and contact
        """
        contact = validated_data.pop("contact")
        provider = Provider.objects.create(**validated_data)
        Contact.objects.create(**contact, provider=provider)
        return provider

    def update(self, instance, validated_data):
        """
        Update provider and contact except dept
        """
        if "contact" in validated_data:
            contact = validated_data.pop("contact")
            Contact.objects.filter(provider=instance).update(**contact)
        return super().update(instance, validated_data)
