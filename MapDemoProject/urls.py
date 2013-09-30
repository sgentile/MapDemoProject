from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView, RedirectView
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from django.conf import settings
from MapDemo import views

admin.autodiscover()

urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'MapDemoProject.views.home', name='home'),
                       # url(r'^MapDemoProject/', include('MapDemoProject.foo.urls')),
                       # url(r'^$', TemplateView.as_view(template_name="index.html")),

                       # Uncomment the admin/doc line below to enable admin documentation:
                       url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

                       url(r'^notes/', views.NoteList.as_view()),

                       # Uncomment the next line to enable the admin:
                       url(r'^admin/', include(admin.site.urls)),

                       (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),

                       (r'^/?$', RedirectView.as_view(url='/static/index.html')),
)
