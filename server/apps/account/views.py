from rest_framework import viewsets, mixins
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from server.apps.account.models import Account
from server.apps.account.serializer import AccountAddSerializer, AccountStatusSerializer, AccountSubstractSerializer


class AddBalanceAPI(mixins.UpdateModelMixin, GenericViewSet):
    """Пополнение баланса"""
    queryset = Account.objects.filter(status=Account.Status.OPEN).all()
    serializer_class = AccountAddSerializer
    http_method_names = ['put']
    lookup_field = 'uuid'

    def update(self, request, *args, **kwargs):
        response = super(AddBalanceAPI, self).update(request, *args, **kwargs)
        instance = self.get_object()
        return Response({
            'status': 200,
            'result': True,
            'addition': AccountStatusSerializer(instance).data,
            'description': {
                **response.data,
                'method': 'add balance to account'
            },
        })


class StatusBalanceAPI(mixins.RetrieveModelMixin, GenericViewSet):
    """Статус баланса"""
    queryset = Account.objects.all()
    serializer_class = AccountStatusSerializer
    lookup_field = 'uuid'

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        return Response({
            'status': 200,
            'result': True,
            'addition': AccountStatusSerializer(instance).data,
            'description': {
                'method': 'get status'
            },
        })


class SubtractBalanceAPI(mixins.UpdateModelMixin, GenericViewSet):
    """Остаток по балансу, открыт счет или закрыт"""
    queryset = Account.objects.filter(status=Account.Status.OPEN).all()
    serializer_class = AccountSubstractSerializer
    http_method_names = ['put']
    lookup_field = 'uuid'

    def update(self, request, *args, **kwargs):
        super(SubtractBalanceAPI, self).update(request, *args, **kwargs)
        instance = self.get_object()
        return Response({
            'status': 200,
            'result': True,
            'addition': AccountStatusSerializer(instance).data,
            'description': {
                'method': 'subtracted balance from account'
            },
        })


class AccountsAPI(mixins.ListModelMixin, GenericViewSet):
    """Получение всех счетов"""
    queryset = Account.objects.all()
    serializer_class = AccountStatusSerializer
    http_method_names = ['get']


class ServiceAPI(viewsets.ViewSet):
    """Работоспособность сервиса"""

    @action(detail=False, url_path='ping')
    def ping(self, request):
        return Response({'status': 'pong'})
