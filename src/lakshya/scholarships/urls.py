from django.conf.urls import patterns, include, url
from django.views.generic.simple import direct_to_template

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('scholarships.views',
    # Examples:
    url(r'^home$', 'scholarships_home', name='scholarships_home'),
    url(r'^scholars-list(/?)(?P<scholar_id>[0-9]*)$', 'get_scholarships_list', name='innovations_list'),
    url(r'^about-scholarships-project$', direct_to_template, {'template' : 'about_scholarships_project.html'}, name='home'),    
    url(r'^funding-partners', 'funding_partners_list', name='funding-partners'),
)