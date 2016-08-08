import datetime
from django.db import models

"""
    This class is user's basic model where user's details are stored
"""


class UsersModel(models.Model):
    bitaddr = models.CharField(max_length=250)
    email = models.EmailField(max_length=250, null=False, default="fake@email.com")
    medium = models.CharField(max_length=10)
    active = models.BooleanField(default=True)
    joined = models.DateTimeField(auto_now_add=True)


"""
    This is user's satoshi model where we will store user's collected satoshi
"""


class UserSatoshiCollected(models.Model):
    uid = models.IntegerField()
    satoshi = models.IntegerField()
    game = models.CharField(max_length=10)
    when_time = models.DateTimeField(auto_now_add=True)
    won = models.BooleanField(default=True)
    active = models.BooleanField(default=True)

    def userEarnedSatoshiAsJSON(self):
        return dict(
            satoshi=self.satoshi,
            won=self.won,
            time=datetime.datetime.strptime(self.when_time.isoformat()[:19], "%Y-%m-%dT%H:%M:%S"),
            active=self.active)

    def userWonSatoshiAsJSON(self):
        return dict(
            id=self.id,
        )


"""
    This class is to manage user's payout satoshi requests
"""


class UserSatoshiPayout(models.Model):
    uid = models.IntegerField()
    cbapp_id = models.IntegerField()
    satoshi = models.IntegerField()
    game = models.CharField(max_length=10)
    when_time = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=False)

    def userPayedOutSatoshiAsJSON(self):
        return dict(
            satoshi=self.satoshi,
            status=self.status,
            time=datetime.datetime.strptime(self.when_time.isoformat()[:19], "%Y-%m-%dT%H:%M:%S"),
            )
