from django.contrib.auth import REDIRECT_FIELD_NAME
from django.contrib.auth.decorators import user_passes_test


def superuser_required(function=None, redirect_field_name=REDIRECT_FIELD_NAME):
    """
     Decorator for views that checks that the logged in user is a superuser,
    redirects to the log-in page if necessary.
    """
    # actual_decorator = user_passes_test(
    #     lambda u: u.is_active and u.userprofile.is_SuperUser,
    #     redirect_field_name=redirect_field_name
    # )
    # if function:
    #     return actual_decorator(function)
    # return actual_decorator
    pass


def test(func):
    def wrapper(request, *args, **kwargs):
        user = request.user
        print(user.is_active, user.userprofile.is_SuperUser)
        return func(request, *args, **kwargs)

    return wrapper


def justuser_required(function=None, redirect_field_name=REDIRECT_FIELD_NAME):
    actual_decorator = user_passes_test(
        lambda u: u.is_active and u.is_Just_User,
        redirect_field_name=redirect_field_name
    )
    if function:
        return actual_decorator(function)
    return actual_decorator


def specificuser_required(function=None, redirect_field_name=REDIRECT_FIELD_NAME):
    actual_decorator = user_passes_test(
        lambda u: u.is_active and u.is_SpecificUser,
        redirect_field_name=redirect_field_name
    )
    if function:
        return actual_decorator(function)
    return actual_decorator
