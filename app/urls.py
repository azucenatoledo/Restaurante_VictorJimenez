from django.conf import settings

from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.models import User
from django.conf.urls.static import static
from rest_framework import routers, serializers, viewsets
from . import viewss
from core import views
from django.conf.urls import handler400


# , handler403, handler404, handler500


# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']


# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'productos', viewss.ProductoViewSet)
urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('accounts/', include('allauth.urls')),
                  path('', views.HomeView.as_view(), name='home'),
                  path('contact/', views.ContactView.as_view(), name='contact'),
                  path('cart/', include('cart.urls', namespace='cart')),
                  path('profile/', views.ProfilView.as_view(), name='profile'),
                  # path('api/', include(router.urls)),
                  # path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

handler404 = viewss.Error404View.as_view()
