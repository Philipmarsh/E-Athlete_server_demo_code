"""server_v1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""


from django.conf.urls.static import static
from django.contrib import admin

from django.urls import path, include
from rest_framework import routers
from users import views as userviews
from diary import views as diaryviews
from home import views as homeviews

from server_v1 import settings

router = routers.DefaultRouter()
router.register('users', userviews.UserViewSet)
router.register('result', diaryviews.ResultViewSet, basename='Result')
router.register('goal', diaryviews.GoalViewSet, basename='Goal')
router.register('objective', diaryviews.ObjectiveViewSet, basename='Objective')
router.register('fcm-token', userviews.FCMTokenView)
router.register('session', diaryviews.SessionEntryViewSet, basename='SessionEntry')
router.register('general-day', diaryviews.GeneralDayEntryViewSet, basename='GeneralDayEntry')
router.register('competition', diaryviews.CompetitionEntryViewSet, basename='Competition')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('', include('home.urls')),
    path('e-coach/', include('ecoach.urls')),
    path('tinymce/', include('tinymce.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
