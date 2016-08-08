import hashlib
import codecs
from django.shortcuts import render
from django.views.generic import TemplateView

from veeru.settings import BASE_DIR


class AboutBTTGame(TemplateView):
    def get(self, request, *args, **kwargs):
        file = codecs.open(BASE_DIR+"/views/btt_tc.html", 'r').read()
        x = hashlib.sha224(str(file).encode('utf-8')).hexdigest()

        return render(request, 'AboutBTTGame.html', {'sha_sum': str(x)})