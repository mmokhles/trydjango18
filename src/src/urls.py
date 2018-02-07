from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin

from newsletter import views as newsletter_views
from trydjango181 import views as trydjango181_views

urlpatterns = [
    # Examples:
    url(r'^$', newsletter_views.home, name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^contact/$', newsletter_views.contact, name='contact'),
    url(r'^ahsdlasd/$', trydjango181_views.about, name='about'),
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/', include('registration.backends.default.urls')),

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
