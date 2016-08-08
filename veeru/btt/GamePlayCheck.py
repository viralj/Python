from django.http import Http404, JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView


class GamePlayCheck(TemplateView):
    def get(self, request, *args, **kwargs):
        raise Http404

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(GamePlayCheck, self).dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):

        error = False
        msg = 0
        data = [{'game_id': None}]

        return JsonResponse({'error': error, 'msg': msg, 'data': data},
                            content_type='application/json')