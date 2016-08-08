from django.http import Http404, JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView

from useraccess.models import UserSatoshiCollected
from useraccess.models import UsersModel


class UserMakeSatoshi(TemplateView):
    def get(self, request, *args, **kwargs):
        raise Http404

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(UserMakeSatoshi, self).dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        error = False
        msg = 0

        email = request.POST.get('email')
        game = request.POST.get('game')
        won = request.POST.get('won').lower() in ("true", "1")
        userAgent = request.META['HTTP_USER_AGENT']

        if email is not None and game is not None and userAgent == "android-veeru":
            try:

                user = UsersModel.objects.get(email=email)

                if user is not None:

                    if won:
                        addSatoshi = UserSatoshiCollected.objects.create(
                            uid=user.id,
                            active=True,
                            won=True,
                            game=game,
                            satoshi=250
                        )
                        try:
                            addSatoshi.save()
                        except Exception:
                            error = True
                            msg = 5

                    else:
                        updateSatoshi = UserSatoshiCollected.objects.filter(uid=user.id,
                                                                            game=game,
                                                                            won=True,
                                                                            active=True).order_by('id')[0:1]

                        try:
                            for x in updateSatoshi:
                                x.active = False
                                x.won = False
                                x.save()
                        except Exception:
                            error = True
                            msg = 6

                else:
                    error = True
                    msg = 4
            except UsersModel.DoesNotExist:
                error = True
                msg = 2
            except Exception:
                error = True
                msg = 3

        else:
            error = True
            msg = 1

        return JsonResponse({'error': error, 'msg': msg, 'email': email, 'game': game, 'agent': userAgent},
                            content_type='application/json')
