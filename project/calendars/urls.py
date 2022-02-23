from django.urls import path, include
from rest_framework import routers
from . import views

app_name = 'calendars'
router = routers.DefaultRouter()

router.register('api/calendars/admin/calendars', views.CalendarAdminViewSet,
                basename='calendar-admin')
router.register('api/calendars/admin/events', views.EventAdminViewSet,
                basename='event-admin')
router.register('api/calendars/calendar', views.CalendarOwnedViewSet,
                basename='calendar')
router.register('api/calendars/events', views.EventOwnedViewSet, basename='event-owned')
router.register('api/calendars/eventslist', views.EventList, basename='event-list')
router.register('api/calendars/eventslist/monthview', views.EventMonthView,
                basename='event-month-view')
router.register('api/calendars/eventslist/allview', views.EventAllView,
                basename='event-all-view')
router.register('api/calendars/eventslist/currentweek', views.CurrentWeekView)
router.register('api/calendars/eventslist/currentweekall', views.CurrentWeekAllView,
                basename='current-week')

urlpatterns = [
    path('', include(router.urls)),
]
