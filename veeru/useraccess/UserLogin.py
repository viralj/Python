from django.core.validators import validate_email
from django.forms import forms
from django.http import Http404
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView

from useraccess.models import UsersModel


class UserLogin(TemplateView):
    def get(self, request, *args, **kwargs):
        raise Http404

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(UserLogin, self).dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):

        error = False
        msg = "none"
        uid = None

        email = request.POST.get("email")
        medium = request.POST.get("medium")

        if email is not "" and medium is not "":

            try:
                validate_email(email)

                try:

                    user = UsersModel.objects.get(email=email)
                    uid = user.id

                except UsersModel.DoesNotExist:
                    user = UsersModel.objects.create()
                    user.email = email
                    user.medium = medium

                    try:
                        user.save()

                        uid = user.id
                    except Exception as e:
                        error = True
                    msg = 1

            except forms.ValidationError:
                error = True
                msg = 2

        else:
            error = True
            msg = 3

        return JsonResponse({'error': error, 'msg': msg, 'uid': uid})
