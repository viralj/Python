import os, django

from cbapp.TransactionBTC import TransactionBTC

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "veeru.settings")
django.setup()

import datetime
from cbapp.models import CBTransferBTC
from useraccess.models import UserSatoshiPayout


class CheckUserPayOut:
    now = datetime.datetime.now()

    def startProcess(self, userID):
        checkPendingPayOut = None

        try:
            checkPendingPayOut = UserSatoshiPayout.objects.get(uid=userID, status=False)

            if checkPendingPayOut is not None:
                getTransaction = CBTransferBTC.objects.get(id=checkPendingPayOut.cbapp_id)
                self.checkStatusOfTransaction(trID=getTransaction.tr_id,
                                              payoutID=checkPendingPayOut.id,
                                              cbtrID=getTransaction.id)

        except UserSatoshiPayout.DoesNotExist:
            return True
        except Exception as e:
            print("CheckUserPayOut")
            print("Checking exception")
            print(e)


    def checkStatusOfTransaction(self, trID, payoutID, cbtrID):
        x = TransactionBTC()
        z = x.getSingleTransaction(transaction_id=trID)

        if str(z['status']).lower() == 'completed':
            try:
                a = CBTransferBTC.objects.get(id=cbtrID)
                a.status = z['status']
                a.updated_at = z['updated_at']
                a.save()

                b = UserSatoshiPayout.objects.get(id=payoutID)
                b.status = True
                b.save()

            except Exception as e:
                print("CheckUserPayOut")
                print("another exception")
                print(e)
