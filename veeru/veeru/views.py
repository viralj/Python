from django.http import HttpResponseNotFound, HttpResponseForbidden
from django.shortcuts import render_to_response


def error403(request, reason=""):
    return HttpResponseForbidden(render_to_response("404.html"))


def error404(request, reason=""):
    return HttpResponseNotFound(render_to_response("404.html"))
