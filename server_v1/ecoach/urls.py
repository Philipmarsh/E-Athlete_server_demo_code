from django.conf.urls.static import static
from django.urls import path, include
from rest_framework import routers

from .views import ECoachUserAPIView, OrganizationDetailAPIView, OrganizationAPIView, TeamDetailAPIView, TeamAPIView, \
    TeamMemberAPIView

router = routers.DefaultRouter()
router.register('users', ECoachUserAPIView)

urlpatterns = [
    path('api/', include(router.urls)),
    path('users', ECoachUserAPIView),
    path('organization/', OrganizationAPIView.as_view()),
    path('organization/<slug:name>/', OrganizationDetailAPIView.as_view()),
    path('team/', TeamAPIView.as_view()),
    path('team/<slug:name>/', TeamDetailAPIView.as_view()),
    path('individual/<uuid:id>/', TeamMemberAPIView.as_view()),
]