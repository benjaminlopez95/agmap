<<<<<<< HEAD
from django.conf.urls import url
from plots.views import CreateNewPlotView, PlotView

urlpatterns = [
    url(r'^create/$', CreateNewPlotView.as_view(), name='plots'),
    url(r'^create-map/$', PlotView.as_view(), name='plotview'),
]
=======
from django.conf.urls import url
from plots.views import CreateNewPlotView, PlotView

urlpatterns = [
    url(r'^create/$', CreateNewPlotView.as_view(), name='plots'),
    url(r'^create-map/$', PlotView.as_view(), name='plotview'),
]
>>>>>>> e854a0e1d078f16e921a24a3e201c203befc9c4a
