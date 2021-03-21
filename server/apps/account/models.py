from uuid import uuid4
from django.db import models
from django.utils.translation import gettext_lazy as _


class Account(models.Model):
    class Status(models.TextChoices):
        OPEN = 'ON', _('Открыт')
        CLOSE = 'OFF', _('Закрыт')
    uuid = models.UUIDField(_('Уникальный номер абонента'), default=uuid4)
    name = models.CharField(_('ФИО абонента'), max_length=255)
    balance = models.DecimalField(_('текущий баланс на счете'), max_digits=10, decimal_places=2)
    hold = models.DecimalField(_('холды на счете'), max_digits=10, decimal_places=2)
    status = models.CharField(_('Статус'), max_length=3, choices=Status.choices, default=Status.OPEN)

    class Meta:
        verbose_name = _('Счет')
        verbose_name_plural = _('Счета')

    def __str__(self):
        return f'{self.name}. №: {self.uuid}'
