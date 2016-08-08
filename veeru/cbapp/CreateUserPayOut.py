import os, django

from cbapp.TransactionBTC import TransactionBTC
from cbapp.models import CBTransferBTC

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "veeru.settings")
django.setup()

import datetime
from django.db.models import Sum
from useraccess.models import UserSatoshiPayout, UserSatoshiCollected, UsersModel


class CreateUserPayOut:
    now = datetime.datetime.now()

    def startProcess(self, userID, game):
        checkUserPayout = None

        try:
            checkUserPayout = UserSatoshiPayout.objects.filter(uid=userID).order_by('-id')[:1]


            for x in checkUserPayout:
                userTimeMonth = x.when_time.strftime("%m")
                userTimeYear = x.when_time.strftime("%Y")

                if userTimeMonth != self.now.month and userTimeYear != self.now.year:
                    self.createUserPayOut(userID=userID, game=game)

            if checkUserPayout.__len__() == 0 or checkUserPayout is None:
                self.createUserPayOut(userID=userID, game=game)

        except Exception as e:
            print("CreateUserPayOut")
            print(e)

    def createUserPayOut(self, userID, game):
        userSatoshiData = None

        try:
            userSatoshiData = UserSatoshiCollected.objects.filter(uid=userID,active=True)\
                .aggregate(total_satoshi=Sum('satoshi'))

            if userSatoshiData['total_satoshi'] is not None and userSatoshiData['total_satoshi'] >= 50000:
                creatPayout = UserSatoshiPayout.objects.create(uid=userID, satoshi=userSatoshiData['total_satoshi'],
                                                 game=game, status=0, cbapp_id=0)

                self.processPayout(userID=userID, payoutID=creatPayout.id, game=game)

                singleUser = UserSatoshiCollected.objects.filter(active=True, uid=userID, game=game)

                for x in singleUser:
                    x.active = False
                    x.save()

        except Exception as e:
            print("CreateUserPayOut")
            print(e)


    def processPayout(self, userID, payoutID, game):
        processToPayOut = None

        try:
            processToPayOut = UserSatoshiPayout.objects.get(status=False, uid=userID, id=payoutID)

            user = UsersModel.objects.get(id=userID, active=True)
            bitAddr = user.bitaddr
            amount = int(processToPayOut.satoshi) * 0.00000001
            month = (processToPayOut.when_time).strftime("%B")
            year = (processToPayOut.when_time).strftime("%Y")
            description = "Reward from BitTacToe for {}, {}.".format(month, year)

            sendbtc = TransactionBTC()

            try:
                x = sendbtc.sendBTCToUser(user_btc_wallet=bitAddr, amount=amount, description=description)

                saveData = CBTransferBTC.objects.create(uid=userID)
                saveData.game = game
                saveData.amount_amount = x['amount']['amount']
                saveData.amount_currency = x['amount']['currency']
                saveData.created_at = x['created_at']
                saveData.description = x['description']
                saveData.details_subtitle = x['details']['subtitle']
                saveData.details_title = x['details']['title']
                saveData.tr_id = x['id']
                saveData.instant_exchange = x['instant_exchange']
                saveData.native_amount_amount = x['native_amount']['amount']
                saveData.native_amount_currency = x['native_amount']['currency']
                saveData.resource = x['resource']
                saveData.resource_path = x['resource_path']
                saveData.status = x['status']
                saveData.to_id = x['to']['id']
                saveData.to_resource = x['to']['resource']
                saveData.to_resource_path = x['to']['resource_path']
                saveData.type = x['type']
                saveData.updated_at = x['updated_at']

                try:
                    saveData.save()

                    processToPayOut.cbapp_id = saveData.id
                    processToPayOut.save()

                except Exception as e:
                    print("CreateUserPayOut")
                    print("saving exception : ")
                    print(e)

            except Exception as e:
                print("CreateUserPayOut")
                print("process exception")
                print(e)

        except Exception as e:
            print("CreateUserPayOut")
            print(e)

