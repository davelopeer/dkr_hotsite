from django.conf.urls import url
from website import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^form-send/$', views.pay_success, name='pay-success'),
    url(r'^health-form/$', views.health_form, name='health-form'),
]
