# coding: utf-8

from django.core.urlresolvers import reverse


def reverse_absolute_uri(request, name, kwargs=None):
    return request.build_absolute_uri(reverse(name, kwargs=kwargs))


def get_remote_addr(request):
    """
    Return remote address from 'HTTP_X_REAL_IP' header or 'REMOTE_ADDR'.
    :param request:
    :return:
    """
    return request.META.get('HTTP_X_REAL_IP', request.META.get('REMOTE_ADDR'))
