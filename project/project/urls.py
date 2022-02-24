from django.urls import path, include
from django.contrib import admin
from django.urls import path
# from djoser.views import UserViewSet
from rest_framework.routers import DefaultRouter
from calendars.urls import router as calendarrouter
from accounts.urls import router as accountsrouter

router = DefaultRouter()

router.registry.extend(calendarrouter.registry)
router.registry.extend(accountsrouter.registry)
# router.register('users', UserViewSet, basename="users")


def is_route_selected(url_pattern):
    """Add routes here.."""

    urls = [
        "users/set_username/",
        "users/set_email/",
        "users/reset_email_confirm/",
    ]
    for u in urls:
        match = url_pattern.resolve(u)
        if match:
            return False
    return True


# Filter router URLs removing unwanted ones
selected_user_routes = list(filter(is_route_selected, router.urls))

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('calendars/', include('calendars.urls')),
    path('accounts/', include('accounts.urls')),
]
#  + selected_user_routes
