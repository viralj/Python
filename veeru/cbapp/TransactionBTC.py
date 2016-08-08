from coinbase.wallet.client import Client

from cbapp import CoinbaseSecrets

# # Get your primary coinbase account
# primary_account = client.get_primary_account()
# address = primary_account.create_address()
#
# # Send coins to the new account from your primary account:
# tx = primary_account.send_money(to="1BLDRcN19R6bt9oiCy7WXkLrtQcNmJCdQo",
#                            amount='0.0001', currency='BTC', description='Testing account again!')


# data = {
#   "amount": {
#     "amount": "-0.00010000",
#     "currency": "BTC"
#   },
#   "created_at": "2016-08-04T22:06:56Z",
#   "description": "Testing account again!",
#   "details": {
#     "subtitle": "to 1BLDRcN19R6bt9oiCy7WXkLrtQcNmJCdQo",
#     "title": "Transferred bitcoin"
#   },
#   "id": "fbc781fe-2f95-5b2f-ae9c-6ab35a3d86df",
#   "instant_exchange": False,
#   "native_amount": {
#     "amount": "-0.05",
#     "currency": "USD"
#   },
#   "resource": "transaction",
#   "resource_path": "/v2/accounts/a101a60c-dd26-5d6f-acd7-cca2498baffe/transactions/fbc781fe-2f95-5b2f-ae9c-6ab35a3d86df",
#   "status": "pending",
#   "to": {
#     "id": "7e037dec-b533-5282-9bf7-86b88edbaadc",
#     "resource": "account",
#     "resource_path": "/v2/accounts/7e037dec-b533-5282-9bf7-86b88edbaadc"
#   },
#   "type": "transfer",
#   "updated_at": "2016-08-04T22:06:57Z"
# }
from cbapp.CoinbaseSecrets import VEERU_ID, API_KEY, API_SECRET, BTC_WALLET_ADDRESS


class TransactionBTC:
    # Setting up coinbase client
    client = Client(API_KEY, API_SECRET)

    # Getting primary account
    primary_account = client.get_primary_account()

    def sendBTCToUser(self, user_btc_wallet, amount, description):
        return self.primary_account.send_money(to=user_btc_wallet,
                                               amount=amount,
                                               currency="BTC",
                                               description=description)

    def getAllTransactions(self):
        return self.client.get_transactions(account_id=VEERU_ID)

    def getSingleTransaction(self, transaction_id):
        return self.primary_account.get_transaction(transaction_id=transaction_id)

