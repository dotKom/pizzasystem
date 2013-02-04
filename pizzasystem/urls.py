from django.conf.urls import patterns, include, url

urlpatterns = patterns('pizzasystem.views',
    url(r'^$', 'index', name='pizza_index'),
    url(r'^pizzaview', 'pizzaview', name='pizzaview'),
    url(r'^(?P<pizza_id>\d+)/$','edit', name='edit'),
)
