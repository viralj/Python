from django.http import JsonResponse
from django.views.generic import TemplateView
from django.db import connections, OperationalError


class TestConnection(TemplateView):
    def get(self, request, *args, **kwargs):

        msg = 0

        db_conn = connections['default']
        try:
            c = db_conn.cursor()
        except OperationalError:
            error = True
            msg = 1
        except Exception:
            error = True
            msg = 2
        else:
            error = False

        return JsonResponse({"error" : error, "msg" : msg})