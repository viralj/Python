import os, django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "veeru.settings")
django.setup()

import datetime, time
from django.db.models import Sum
from cbapp.models import PayOutCreated
from useraccess.models import UsersModel, UserSatoshiCollected, UserSatoshiPayout


class CreatePayOut:
    now = datetime.datetime.now()

    def processCreatePayOut(self):
        """
        First we will try to check if there is payed out created for current month or not
        """
        users = []
        errors = False
        payoutData = None

        try:

            payoutData = PayOutCreated.objects.get(current_month=self.now.month,
                                                   current_year=self.now.year)
        except PayOutCreated.DoesNotExist as e:
            try:
                PayOutCreated.objects.create(current_month=self.now.month,
                                             current_year=self.now.year,
                                             status=False)
            except Exception as e:
                print("1 : " + str(e))
        except Exception as e:
            print("2 : " + str(e))

        """
            Now we will check for status of current month data.
            If it is 0 than its just created.
            If it is 1 than it means there are some pending transactions.
            If it is 2 than it means that every thing is done.
            if it is 9 or higher that there is some error
        """
        if payoutData.status == 0:

            try:
                getAllUsers = UsersModel.objects.filter(active=True)

                if getAllUsers is not None and getAllUsers != []:
                    for x in getAllUsers:
                        users.append(x.id)

                    self.processUsersPayout(users=users)
                else:
                    payoutData.status = 2
                    payoutData.save()

            except Exception as e:
                print("3 : " + str(e))
        elif payoutData.status == 1:
            self.processBTCPayOut()
        elif payoutData.status == 2:
            print("status 2")
        elif payoutData.status >= 9:
            print("status >= 9")

    def processUsersPayout(self, users=[]):
        for x in users:

            """
                We are creating payout for this month for this user
            """
            try:
                a = UserSatoshiPayout.objects.filter(uid=x).order_by('-id')[:1]

                if a != [] and a.__len__() > 0:
                    for z in a:
                        if z.when_time.strftime("%m") !=self.now.month and z.when_time.strftime("%Y") !=self.now.year:
                            self.makePayOut(userID=x)
                else:
                    self.makePayOut(userID=x)
            except Exception as e:
                print("5 : " + str(e))

            time.sleep(1)

        q = PayOutCreated.objects.get(current_month=self.now.month, current_year=self.now.year)
        q.status = 1
        q.save()

    def makePayOut(self, userID):
        user = None
        try:
            singleUserAggregated = UserSatoshiCollected.objects.filter(active=True,uid=userID)\
                .aggregate(total_satoshi=Sum('satoshi'))

            if singleUserAggregated['total_satoshi'] is not None and singleUserAggregated['total_satoshi'] >= 50000:
                UserSatoshiPayout.objects.create(uid=userID, satoshi=singleUserAggregated['total_satoshi'],
                                                 game="btt",status=0,cbapp_id=0)

                singleUser = UserSatoshiCollected.objects.filter(active=True,uid=userID,game="btt")

                for x in singleUser:
                    x.active = False
                    x.save()

        except Exception as e:
            print("4 : " + str(e))

    def processBTCPayOut(self):

        processToPayOut = None

        try:
            processToPayOut = UserSatoshiPayout.objects.filter(status=0)

            if processToPayOut is not None and processToPayOut.__len__() > 0:
                for x in processToPayOut:

                    user = UsersModel.objects.get(id=x.uid, active=True)
                    bitAddr = user.bitaddr
                    amount = int(x.satoshi)*0.00000001
                    month = (x.when_time).strftime("%B")
                    year = (x.when_time).strftime("%Y")
                    description = "Reward from BitTacToe for {}, {}.".format(month, year)



        except Exception as e:
            print("6 : " + str(e))




a = CreatePayOut()
a.process()
