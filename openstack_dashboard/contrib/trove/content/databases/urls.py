# Copyright 2013 Rackspace Hosting
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

from django.conf.urls import include
from django.conf.urls import patterns
from django.conf.urls import url

from openstack_dashboard.contrib.trove.content.databases.logs \
    import urls as logs_urls
from openstack_dashboard.contrib.trove.content.databases.upgrade \
    import urls as upgrade_urls
from openstack_dashboard.contrib.trove.content.databases import views

BASEINSTANCES = r'^(?P<instance_id>[^/]+)/%s'
INSTANCES = BASEINSTANCES + '$'
BASE_USER = r'^(?P<instance_id>[^/]+)/(?P<user_name>[^/]+)'
USERS = BASE_USER + '/%s$'


urlpatterns = patterns(
    '',
    url(r'^$', views.IndexView.as_view(),
        name='index'),
    url(r'^launch$', views.LaunchInstanceView.as_view(),
        name='launch'),
    url(INSTANCES % '', views.DetailView.as_view(),
        name='detail'),
    url(INSTANCES % 'create_database', views.CreateDatabaseView.as_view(),
        name='create_database'),
    url(INSTANCES % 'resize_volume', views.ResizeVolumeView.as_view(),
        name='resize_volume'),
    url(INSTANCES % 'resize_instance', views.ResizeInstanceView.as_view(),
        name='resize_instance'),
    url(INSTANCES % 'create_user', views.CreateUserView.as_view(),
        name='create_user'),
    url(BASE_USER + '/(?P<user_host>[^/]+)/%s$' % 'edit_user',
        views.EditUserView.as_view(),
        name='edit_user'),
    url(BASE_USER + '/(?P<user_host>[^/]+)/%s$' % 'access_detail',
        views.AccessDetailView.as_view(),
        name='access_detail'),
    url(INSTANCES % 'attach_config', views.AttachConfigurationView.as_view(),
        name='attach_config'),
    url(INSTANCES % 'promote_to_replica_source',
        views.PromoteToReplicaSourceView.as_view(),
        name='promote_to_replica_source'),
    url(INSTANCES % 'manage_root', views.ManageRootView.as_view(),
        name='manage_root'),
    url(BASEINSTANCES % 'logs/', include(logs_urls, namespace='logs')),
    url(BASEINSTANCES % 'upgrade/',
        include(upgrade_urls, namespace='upgrade')),
)
