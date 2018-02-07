from views import *
from rest_framework import routers
from django.conf.urls import url, include

router = routers.SimpleRouter()

router.register(r'company', CompanyViewSet)
router.register(r'risk', RiskViewSet)
router.register(r'risk-type', RiskTypeEntityViewSet)
router.register(r'risk-type-attribute', RiskTypeAttributeViewSet)


urlpatterns = [
	url(r'v1/', include(router.urls, namespace = 'v1')),
]
