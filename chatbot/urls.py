from django.urls import re_path, include
from django.contrib import admin

from django.views.generic.base import TemplateView

urlpatterns = [
    re_path(r'^admin/', admin.site.urls),
    re_path(r'^$', TemplateView.as_view(template_name="index.html")),
    re_path(r'^sms/', include('sms.urls')),
    re_path(r'^orders/', include('orders.urls')),
]