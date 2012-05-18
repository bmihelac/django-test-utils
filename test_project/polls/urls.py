from django.conf.urls.defaults import *
from django.views.generic.list import ListView

from models import Poll, Choice


info_dict = {
    'queryset': Poll.objects.all(),
}


urlpatterns = patterns('',
    (r'^$', ListView.as_view(model=Poll)),
    (r'^(?P<object_id>\d+)/$', 'django.views.generic.list_detail.object_detail', info_dict),
    url(r'^(?P<object_id>\d+)/results/$', 'django.views.generic.list_detail.object_detail', dict(info_dict, template_name='polls/results.html'), 'poll_results'),
    (r'^(?P<poll_id>\d+)/vote/$', 'polls.views.vote'),
)
