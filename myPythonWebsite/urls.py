from django.conf.urls import url
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^add/', views.add, name='add'),
    url(r'^(?P<employee_id>[0-9]+)/$', views.employee_detail, name='employee_detail'),
    url(r'^newForm/',TemplateView.as_view(template_name = 'myPythonWebsite/addAccomodationForm.html'))
]