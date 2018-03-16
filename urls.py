from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'add_campaign_misp/$', views.add_campaign_misp, name='add_campaign_misp'),
	url(r'^(?P<ctype>.+?)/(?P<cid>.+?)/$', views.get_relationships, name='get_relationships'),
	url(r'send_to_misp/$', views.send_to_misp, name='send_to_misp'),
	]


'''
def register_api(v1_api):
    from misp_service.api import RelationshipsServiceResource
    v1_api.register(RelationshipsServiceResource())
'''
