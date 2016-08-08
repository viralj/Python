from datetime import datetime

from django.http import Http404, JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView

from useraccess.models import UserSatoshiCollected


class GameWinner(TemplateView):
    def get(self, request, *args, **kwargs):
        # raise Http404
        error = False
        msg = 0
        data = None

        uid = request.GET.get("uaid")
        won = request.GET.get("won").lower() in ("true", "1")
        userSatoshi = None
        results = None

        if uid is not None and won is not None:

            if not won:
                try:

                    userSatoshi = UserSatoshiCollected.objects.filter(uid=uid, satoshi=500, active=True).order_by('id')[
                                  :1]
                    results = [ob.userWonSatoshiAsJSON() for ob in userSatoshi]

                except Exception:
                    error = True
                    msg = 2

                if results is None or results == []:
                    try:

                        userSatoshi = UserSatoshiCollected.objects.filter(uid=uid, satoshi=250, active=True).order_by(
                            'id')[:2]
                        results = [ob.userWonSatoshiAsJSON() for ob in userSatoshi]

                    except Exception:
                        error = True
                        msg = 3

                if results is not None or results != []:
                    for x in userSatoshi:
                        x.won = False
                        x.active = False
                        x.save()


            else:
                try:
                    UserSatoshiCollected.objects.create(uid=uid, satoshi=500, game="btt", won=True, active=True).save()
                except Exception as e:
                    print("error")
                    print(e)
                    error = True
                    msg = 4

        else:
            error = True
            msg = 1

        return JsonResponse({'error': error, 'msg': msg},
                            content_type='application/json')

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(GameWinner, self).dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        # raise Http404
        error = False
        msg = 0
        data = None

        uid = request.POST.get("uaid")
        won = request.POST.get("won").lower() in ("true", "1")
        userSatoshi = None
        results = None

        if uid is not None and won is not None:

            if not won:
                try:

                    userSatoshi = UserSatoshiCollected.objects.filter(uid=uid, satoshi=500, active=True).order_by('id')[
                                  :1]
                    results = [ob.userWonSatoshiAsJSON() for ob in userSatoshi]

                except Exception:
                    error = True
                    msg = 2

                if results is None or results == []:
                    try:

                        userSatoshi = UserSatoshiCollected.objects.filter(uid=uid, satoshi=250, active=True).order_by(
                            'id')[:2]
                        results = [ob.userWonSatoshiAsJSON() for ob in userSatoshi]

                    except Exception:
                        error = True
                        msg = 3

                if results is not None or results != []:
                    for x in userSatoshi:
                        x.won = False
                        x.active = False
                        x.when_time = datetime.now()
                        x.save()


            else:
                try:
                    UserSatoshiCollected.objects.create(uid=uid, satoshi=500, game="btt", won=True, active=True).save()
                except Exception as e:
                    print("error")
                    print(e)
                    error = True
                    msg = 4

        else:
            error = True
            msg = 1

        return JsonResponse({'error': error, 'msg': msg},
                            content_type='application/json')