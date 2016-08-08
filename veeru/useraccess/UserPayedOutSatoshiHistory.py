
import locale
from django.http import Http404, JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView

from cbapp.CheckUserPayOut import CheckUserPayOut
from useraccess.models import UsersModel, UserSatoshiCollected, UserSatoshiPayout


class UserPayedOutSatoshiHistory(TemplateView):
    def get(self, request, *args, **kwargs):
        raise Http404

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(UserPayedOutSatoshiHistory, self).dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        error = False
        msg = 0
        data = None

        email = request.POST.get('email')
        game = request.POST.get('game')
        user = None
        userData = None
        results = None
        locale.setlocale(locale.LC_ALL, 'en_US')

        if email is not None and game is not None:

            try:
                user = UsersModel.objects.get(email=email)
                a = CheckUserPayOut()
                a.startProcess(userID=user.id)

                try:
                    userData = UserSatoshiPayout.objects.filter(uid=user.id, game=game).order_by('-id')

                    if len(userData) > 0:
                        results = [ob.userPayedOutSatoshiAsJSON() for ob in userData]
                        for x in results:
                            x["time"] = x["time"].strftime("%B, %Y")
                            x["satoshi"] = locale.format("%d", x["satoshi"], grouping=True)

                except Exception as e:
                    error = True
                    msg = 1

            except UsersModel.DoesNotExist:
                error = True
                msg = 2

        else:
            error = True
            msg = 3

        return JsonResponse({'error': error, 'msg': msg, 'data': results},
                            content_type='application/json')