from celery import shared_task
from django.db.models import F
from server.apps.account.models import Account


@shared_task
def refresh_holds_account():
    """Вычет суммы холда из баланса абонента с последующим очищением холда"""
    Account.objects.filter(hold__gte=0).update(
        balance=F('balance')-F('hold'),
        hold=0
    )
