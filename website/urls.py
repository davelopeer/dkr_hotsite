from django.conf.urls import url
from website import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^form-send/$', views.pay_success, name='pay-success'),
    url(r'^health-form/$', views.health_form, name='health-form'),
    url(r'^guest-form/$', views.guest_form, name='guest-form'),
    url(r'^volunteer-form/$', views.volunteer_form, name='volunteer-form'),
    url(r'^cancellation-policy/$', views.cancellation_policy, name='cancellation-policy'),
    url(r'^sponsor/$', views.sponsor, name='sponsor'),
    url(r'^accommodation/$', views.accomodation, name='accomodation'),
    url(r'^sponsored-form/$', views.sponsored_form, name='sponsored-form'),
    url(r'^special-guest-form/$', views.special_guest_form, name='special-guest-form'),
]
