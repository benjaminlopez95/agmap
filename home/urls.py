<<<<<<< HEAD
from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from home.views import HomeView
from django.views.generic import TemplateView

from .models import FieldPlot


urlpatterns = [
    url(r'^$', HomeView.as_view(), name='home'),
]
=======
from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from home.views import HomeView
from django.views.generic import TemplateView

from .models import FieldPlot


urlpatterns = [
    url(r'^$', HomeView.as_view(), name='home'),
]
>>>>>>> e854a0e1d078f16e921a24a3e201c203befc9c4a
