<<<<<<< HEAD
from django import forms

from leaflet.forms.widgets import LeafletWidget


class WeatherStationForm(forms.ModelForm):

    class Meta:
        model = WeatherStation
        fields = ('name', 'geom')
        widgets = {'geom': LeafletWidget()}
=======
from django import forms

from leaflet.forms.widgets import LeafletWidget


class WeatherStationForm(forms.ModelForm):

    class Meta:
        model = WeatherStation
        fields = ('name', 'geom')
        widgets = {'geom': LeafletWidget()}
>>>>>>> e854a0e1d078f16e921a24a3e201c203befc9c4a
