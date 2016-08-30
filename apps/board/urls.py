from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^add$', views.add, name='add'),  # Render 'new memory' page
    url(r'^add/process$', views.create, name='create'),  # POST
    url(r'^edit$', views.edit_board, name='edit_board'),  # Render 'edit board' page
    url(r'^edit/process$', views.update_board, name='update_board'),  # POST
    url(r'^view/(?P<username>[\w@+.-]+)$', views.view_board, name='view_board'),  # Render 'user board'
    url(r'^view/(?P<username>[\w@+.-]+)/all$', views.view_all, name='view_all'),  # Render 'user memories'
    url(r'^view/(?P<username>[\w@+.-]+)/(?P<memory_id>\d+)$', views.view_memory, name='view_memory'),  # Render 'view memory'

]
