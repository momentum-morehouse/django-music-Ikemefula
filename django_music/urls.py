"""django_music URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URlpatterns:  path('', views.home, name='home')
Class-based viewsL to u
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.urls import include, path
from tracctracc import views as tracctracc_views


# Each template is a separate file that consists of HTML along with some extra template syntax for variables, loops, and other control flow
urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('registration.backends.simple.urls')),
    path('', tracctracc_views.list_albums, name='list_albums'),
    path('tracctracc/add/', tracctracc_views.add_album, name='add_album'),
    path('tracctracc/<int:pk>/edit/', tracctracc_views.edit_album, name='edit_album'),
    ]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),

        # For django versions before 2.0:
        # url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
