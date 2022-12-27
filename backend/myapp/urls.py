
from xml.dom.minidom import Document
from django.contrib import admin
from django.urls import path,re_path,include

from django.conf  import settings
from django.conf.urls.static import static
from django.views.generic.base import TemplateView
from django.views.static import serve

urlpatterns = [
    path('admin/', admin.site.urls),
    # directed to our api
    re_path(r'^api/',include('api.urls')),

    # directed to react build file [ALWAYS MENTIONS r'^$' as reg. exp. otherwise images will not load]
    # if image doesnot load recheck this regex and use another
    re_path(r'^$', TemplateView.as_view(template_name='index.html'), name='home'),
    
    # these are the react router paths that will work for refreshed pages
    # path('singlepage/<int:id>/' , TemplateView.as_view(template_name='index.html')),
    # path('sectionpage/<int:id>/' , TemplateView.as_view(template_name='index.html')),
    # path('featuredsinglepage/' , TemplateView.as_view(template_name='index.html')),
    # path('podcastpage/' , TemplateView.as_view(template_name='index.html')),
]


# tellingn django, where the media files are located
urlpatterns += [
        re_path(r'^media/(?P<path>.*)$', serve, {
            'document_root': settings.MEDIA_ROOT,
        }),
    ]

# telling django django/ whitenoise, where static files are located
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

