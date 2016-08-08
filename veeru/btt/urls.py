from django.conf.urls import url

from btt.GamePlayCheck import GamePlayCheck
from btt.GameWinner import GameWinner

urlpatterns = [

    # url(r'^(?P<str_one>[a-z A-Z 0-9]{5,20})/(?P<str_two>[a-z A-Z 0-9]{5,20})$', AdRunner.as_view(), name='Ad Runner'),
    url(r'^GamePlayCheck$', GamePlayCheck.as_view(), name='BTT Game Play Check'),
    url(r'^GameWinner$', GameWinner.as_view(), name='BTT Game Winner Status'),


]