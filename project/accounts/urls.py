from django.urls import path, include
from djoser.views import UserViewSet
from rest_framework import routers

from . import views

app_name = 'accounts'
router = routers.DefaultRouter()
router.register('accounts/admin/users', views.UserAdminViewSet)
router.register('accounts/users', UserViewSet, basename="users")



def is_route_selected(url_pattern):
    """Add routes here.."""

    urls = [
        # "api/accounts/users/set_email/",
        # "users/set_username/",
        # "api/users/set_email/",
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
    path('', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
]
#  +  selected_user_routes
