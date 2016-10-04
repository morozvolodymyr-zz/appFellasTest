from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic import TemplateView

from appFellas.list_image import get_images
from appFellas.views import UploadImageView, AuthorizationView, GetImagesView, LogOutView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', TemplateView.as_view(template_name='index.html')),
    url(r'^new_image$', UploadImageView.as_view()),
    url(r'^new_image_handler$', UploadImageView.as_view()),
    url(r'^authorization$', AuthorizationView.as_view()),
    url(r'^authorization_handler$', AuthorizationView.as_view()),
    url(r'^images$', get_images),
    url(r'^get_images$', GetImagesView.as_view()),
    url(r'^log_out$', LogOutView.as_view()),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
