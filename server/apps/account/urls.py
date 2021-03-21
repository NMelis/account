from rest_framework import routers

from server.apps.account.views import ServiceAPI, AddBalanceAPI, StatusBalanceAPI, SubtractBalanceAPI, AccountsAPI

router = routers.DefaultRouter()
router.register('', ServiceAPI, basename='service')
router.register('add', AddBalanceAPI, basename='add')
router.register('status', StatusBalanceAPI, basename='status')
router.register('subtract', SubtractBalanceAPI, basename='subtract')
router.register('accounts', AccountsAPI, basename='accounts')

urlpatterns = router.urls
