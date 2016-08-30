from django.conf.urls import url, include
# from django.contrib import admin

urlpatterns = [
    url(r'^', include(apps.login.urls), namespace='login'),
    url(r'^board/', include(apps.board.urls), namespace='board'),
    # url(r'^admin/', admin.site.urls),
]
