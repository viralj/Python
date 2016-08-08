from django.db.models import Sum
from django.http import Http404, JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView

from useraccess.models import UserSatoshiCollected, UsersModel


class UserSatoshiFetch(TemplateView):
    def get(self, request, *args, **kwargs):
        raise Http404

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(UserSatoshiFetch, self).dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        error = False
        msg = 0
        data = None

        email = request.POST.get('email')

        if email is not None:
            try:
                user = UsersModel.objects.get(email=email)

                data = UserSatoshiCollected.objects \
                    .filter(uid=user.id, active=True, won=True) \
                    .aggregate(total=Sum('satoshi'))

                data = data['total']

            except UserSatoshiCollected.DoesNotExist:
                error = True
                msg = 1
            except Exception:
                error = True
                msg = 3

        else:
            error = True
            msg = 2

        return JsonResponse({'error': error, 'msg': msg, 'satoshi': data},
                            content_type='application/json')
