import uuid

from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from server.apps.account.models import Account


class Command(BaseCommand):
    help = 'Create init accounts'

    DATA = [
        {
            'uuid': '26c940a1-7228-4ea2-a3bc-e6460b172040',
            'name': 'Петров Иван Сергеевич',
            'balance': 1700,
            'hold': 300,
            'status': Account.Status.OPEN,
        },
        {
            'uuid': '7badc8f8-65bc-449a-8cde-855234ac63e1',
            'name': 'Kazitsky Jason',
            'balance': 200,
            'hold': 200,
            'status': Account.Status.OPEN,
        },
        {
            'uuid': '5597cc3d-c948-48a0-b711-393edf20d9c0',
            'name': 'Пархоменко Антон Александрович',
            'balance': 10,
            'hold': 300,
            'status': Account.Status.OPEN,
        },
        {
            'uuid': '867f0924-a917-4711-939b-90b179a96392',
            'name': 'Петечкин Петр Измаилович',
            'balance': 1000000,
            'hold': 1,
            'status': Account.Status.CLOSE,
        },
    ]

    def handle(self, *args, **options):
        if not User.objects.filter(username='admin').exists():
            User.objects.create_superuser('admin', 'admin@noreplay.com', 'admin')
        for account in self.DATA:
            Account.objects.get_or_create(uuid=uuid.UUID(account['uuid']), defaults={
                'name': account['name'],
                'balance': account['balance'],
                'hold': account['hold'],
                'status': account['status'],
            })
