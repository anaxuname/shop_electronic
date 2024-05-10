from rest_framework import serializers


class ProviderTypeValidator:
    """
    Validator for provider type
    """

    def __init__(self, data):
        provider_type = data.get("provider_type")
        parent_provider = data.get("parent_provider")
        if provider_type == 0 and parent_provider is not None:
            raise serializers.ValidationError(
                "Parent provider can't be provider type 0"
            )
        if provider_type != 0 and parent_provider is None:
            raise serializers.ValidationError(
                "Parent provider is required for provider type not 0"
            )
