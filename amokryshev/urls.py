from django.contrib import admin
from django.urls import path, include
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from mainsite import views
from amokryshev import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('summernote/', include('django_summernote.urls'))
]

urlpatterns += i18n_patterns(
    path('', views.index, name='index'),
    path('articles/<str:article_id>/', views.article, name='article')
)

#if settings.DEBUG:
#    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler400 = 'mainsite.views.error_400'
handler403 = 'mainsite.views.error_403'
handler404 = 'mainsite.views.error_404'
handler500 = 'mainsite.views.error_500'
handler503 = 'mainsite.views.error_503'
