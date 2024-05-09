from rest_framework.serializers import ModelSerializer
from .models import Provider, Contact


class ContactSerializer(ModelSerializer):
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
    contact = ContactSerializer(many=False)

    class Meta:
        model = Provider
        fields = [
            "id",
            "name",
            "provider_type",
            "parent_provider",
            "contact",
            "dept",
        ]

    def create(self, validated_data):
        contact = validated_data.pop("contact")
        provider = Provider.objects.create(**validated_data)
        Contact.objects.create(**contact, provider=provider)
        return provider

    def update(self, instance, validated_data):
        contact = validated_data.pop("contact")
        Contact.objects.filter(provider=instance).update(**contact)
        return super().update(instance, validated_data)
