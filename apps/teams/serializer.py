from rest_framework import serializers
from .models import Translators_Team


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Translators_Team
        exclude = ['team_member']


class TeamRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Translators_Team
        fields = ["team_member"]

    def update(self, instance, validated_data):
        instance.team_member = validated_data.get('team_member', instance.team_member)
        instance.requester = self.context['requester']  # Устанавливаем пользователя
        instance.save()
        return instance