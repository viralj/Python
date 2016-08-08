from django.conf.urls import url

from useraccess.UserAccountStatus import UserAccountStatus
from useraccess.UserEarnedSatoshiHistory import UserEarnedSatoshiHistory
from useraccess.UserLogin import UserLogin
from useraccess.UserMakeSatoshi import UserMakeSatoshi
from useraccess.UserPayedOutSatoshiHistory import UserPayedOutSatoshiHistory
from useraccess.UserSatoshiFetch import UserSatoshiFetch

urlpatterns = [

    # url(r'^(?P<str_one>[a-z A-Z 0-9]{5,20})/(?P<str_two>[a-z A-Z 0-9]{5,20})$', AdRunner.as_view(), name='Ad Runner'),
    url(r'^UserAuth/Login$', UserLogin.as_view(), name='User Auth Login'),
    url(r'^UserAccountStatus$', UserAccountStatus.as_view(), name='User Account Status'),
    url(r'^UserSatoshiFetch$', UserSatoshiFetch.as_view(), name='User Satoshi Fetch'),
    url(r'^UserEarnedSatoshiHistory', UserEarnedSatoshiHistory.as_view(), name='User Earned Satoshi History'),
    url(r'^UserPayedOutSatoshiHistory', UserPayedOutSatoshiHistory.as_view(), name='User Payed Out Satoshi History'),
    url(r'^UserMakeSatoshi', UserMakeSatoshi.as_view(), name='User Make Satoshi'),


]