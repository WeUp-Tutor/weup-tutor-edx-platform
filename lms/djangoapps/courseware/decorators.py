"""
Decorators for courseware views.
"""
import functools

from django.shortcuts import redirect
from opaque_keys.edx.keys import CourseKey
from openedx_filters.learning.filters import CoursewareViewStarted


def courseware_view_hooks(view_func):
    """
    Decorator that calls the CoursewareViewStarted filter before rendering a courseware view.

    If any pipeline step returns a non-None ``redirect_url``, the user is redirected to
    that URL. Otherwise, the original view is rendered normally.

    Usage::

        @courseware_view_hooks
        def my_view(request, course_id, ...):
            ...

    Works with both function-based views and ``method_decorator``-wrapped class-based views.
    The decorator extracts the ``course_id`` or ``course_key`` from the view arguments.
    """
    @functools.wraps(view_func)
    def _wrapper(request_or_self, *args, **kwargs):
        # Support both function views (request as first arg) and method views
        # (self as first arg, request as second arg).
        if hasattr(request_or_self, 'method'):
            # Function-based view: first arg is request
            request = request_or_self
        else:
            # Class-based view via method_decorator: first arg is self, second is request
            request = args[0] if args else kwargs.get('request')

        course_id = kwargs.get('course_id') or (args[0] if args and not hasattr(request_or_self, 'method') else None)
        try:
            course_key = CourseKey.from_string(str(course_id)) if course_id else None
        except Exception:  # pylint: disable=broad-except
            course_key = None

        if course_key is not None:
            redirect_url, _request, _course_key = CoursewareViewStarted.run_filter(
                redirect_url=None,
                request=request,
                course_key=course_key,
            )
            if redirect_url:
                return redirect(redirect_url)

        return view_func(request_or_self, *args, **kwargs)

    return _wrapper
