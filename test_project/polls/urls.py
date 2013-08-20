from django.conf.urls import *
from django.views.generic import (
    DetailView,
    ListView,
)

from models import Poll, Choice


info_dict = {
    'queryset': Poll.objects.all(),
}


urlpatterns = patterns('',
    (r'^$', ListView.as_view(model=Poll)),
    (r'^(?P<pk>\d+)/$', DetailView.as_view(**info_dict), info_dict),
    url(r'^(?P<pk>\d+)/results/$', DetailView.as_view(**info_dict),
        dict(info_dict, template_name='polls/results.html'), 'poll_results'),
    (r'^(?P<poll_id>\d+)/vote/$', 'polls.views.vote'),
)
