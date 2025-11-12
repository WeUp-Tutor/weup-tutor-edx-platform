from django.http import JsonResponse

def wul_apps_dummyview(request):
    """
    Dummy view for testing Django routing in Open edX LMS.
    URL: /wul_apps/
    """
    return JsonResponse({
        "status": "ok",
        "message": "Custom Fork Works",
        "user": request.user.username if request.user.is_authenticated else "anonymous"
    })
