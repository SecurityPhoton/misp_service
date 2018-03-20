from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'add_campaign_misp/$', views.add_campaign_misp, name='misp_service-views-add_campaign_misp'),
	url(r'^(?P<ctype>.+?)/(?P<cid>.+?)/$', views.get_relationships, name='misp_service-views-get_relationships'),
	url(r'send_to_misp/$', views.send_to_misp, name='misp_service-views-send_to_misp'),
	]


'''
def register_api(v1_api):
    from misp_service.api import RelationshipsServiceResource
    v1_api.register(RelationshipsServiceResource())
'''
