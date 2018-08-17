from django.conf.urls import url
from .views import HelloApiView

urlpatterns = [
    url(r'^hello/', HelloApiView.as_view(), name='apiview_example'),
]
