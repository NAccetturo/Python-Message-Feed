from django.conf.urls import url
from . import views
                    
urlpatterns = [
    url(r'^$', views.index),
    url(r'^create_user$', views.create_new_user),
    url(r'^reset$', views.reset),
    url(r'^sign_in_user$', views.validate_login),
    url(r'^success$', views.success),
    url(r'^create_message$', views.create_new_message),
    url(r'^create_comment$', views.create_new_comment),
#     url(r'^shows/new$', views.create_show_page),
#     url(r'^shows/add_show$', views.add_show),
#     url(r'^shows/(?P<id>[0-9]+)$', views.read_show),
#     url(r'^shows/(?P<id>[0-9]+)/edit$', views.edit_show),
#     url(r'^edit_show/(?P<id>[0-9]+)$', views.add_edit_show),
#     url(r'^shows/(?P<id>[0-9]+)/delete$', views.delete_show),
]
# (?P<num>[0-9]+)
# {% for x in shows %}
# {% for y in messages %}
# {% endfor %}
# {% if session.id = message_owner.id %}
# {% endif %}