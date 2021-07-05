from django.shortcuts import render

def error_401(request, exception=None, code=401):
    return getRender(request, code, 'Unauthorized')

def error_403(request,  exception=None, code=403):
    return getRender(request, code, 'Forbidden')

def error_404(request, exception=None, code=404):
    return getRender(request, code, 'Not Found')

def error_419(request,  exception=None, code=419):
    return getRender(request, code, 'Page Expired')

def error_429(request, exception=None, code=429):
    return getRender(request, code, 'Too Many Requests')

def error_500(request,  exception=None, code=500):
    return getRender(request, code, 'Server Error')

def error_503(request, exception=None, code=503):
    return getRender(request, code, 'Service Unavailable')

def getRender(request, code, msg, ex=None):
    return render(request, template_name='layout/error.html', context={"code":code, "msg":msg, "ex":ex}, status=code)
