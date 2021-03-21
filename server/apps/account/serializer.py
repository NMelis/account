from django.db.models import F
from rest_framework import routers, serializers

from server.apps.account.models import Account


class AccountStatusSerializer(serializers.ModelSerializer):
    balance = serializers.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        model = Account
        fields = ('uuid', 'status', 'name', 'balance', 'hold')


class AccountAddSerializer(serializers.Serializer):
    balance = serializers.DecimalField(required=True, write_only=True, max_digits=10, decimal_places=2)
    finish_balance = serializers.SerializerMethodField(read_only=True)
    past_balance = serializers.SerializerMethodField(read_only=True)
    added_amount = serializers.SerializerMethodField(read_only=True)

    def get_added_amount(self, value):
        return self.validated_data['balance']

    def get_past_balance(self, value):
        return self.instance.balance-self.validated_data['balance']

    def get_finish_balance(self, value):
        return self.instance.balance+self.validated_data['balance']

    def create(self, validated_data):
        raise NotImplemented()

    def update(self, instance, validated_data):
        instance.balance = F('balance') + validated_data['balance']
        instance.save(update_fields=['balance'])
        instance.refresh_from_db()
        return instance

    class Meta:
        model = Account
        fields = ('balance', 'past_balance', 'added_amount', 'finish_balance')


class AccountSubstractSerializer(serializers.Serializer):
    substraction = serializers.DecimalField(required=True, write_only=True, max_digits=10, decimal_places=2)
    balance = serializers.DecimalField(read_only=True, max_digits=10, decimal_places=2)
    hold = serializers.DecimalField(read_only=True, max_digits=10, decimal_places=2)

    def validate(self, data):
        result = self.instance.balance - self.instance.hold - data['substraction']
        if result < 0:
            raise serializers.ValidationError({'substraction': 'Insufficient funds'})
        return data

    def update(self, instance, validated_data):
        instance.hold = F('hold') + validated_data['substraction']
        instance.save(update_fields=['hold'])
        instance.refresh_from_db()
        return instance

    def create(self, validated_data):
        raise serializers.ValidationError('Create does not support')

    class Meta:
        model = Account
        fields = ('substraction', 'balance', 'hold')
