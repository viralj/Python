from django.db.models import Sum
from django.http import Http404, JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView

from cbapp.CreateUserPayOut import CreateUserPayOut
from useraccess.models import UsersModel, UserSatoshiCollected
from useraccess.validate_bitaddr import check_bc


class UserAccountStatus(TemplateView):
    def get(self, request, *args, **kwargs):
        raise Http404

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(UserAccountStatus, self).dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        error = False
        msg = 0
        data = None

        email = request.POST.get('email')
        wallet = request.POST.get('wallet')

        if wallet is None:
            try:
                userData = UsersModel.objects.get(email=email)

                try:
                    a = CreateUserPayOut()
                    a.startProcess(userID=userData.id, game="btt")
                except Exception as e:
                    return True

                data = {'bit': userData.bitaddr, 'uid': userData.id}

            except UsersModel.DoesNotExist:
                error = True
                msg = 1

        elif wallet is not None and not check_bc(wallet):
            error = True
            msg = 3

        else:
            update = UsersModel.objects.get(email=email)
            update.bitaddr = wallet
            try:
                update.save()
                data = {'bit': update.bitaddr, 'uid': update.id}

            except Exception as e:
                print(e)
                error = True
                msg = 2

        return JsonResponse({'error': error, 'msg': msg, 'data': data},
                            content_type='application/json')
