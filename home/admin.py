<<<<<<< HEAD
from leaflet.admin import LeafletGeoAdmin
from django.contrib import admin

from . import models as fields_models


admin.site.register(fields_models.FieldPlot, LeafletGeoAdmin)
=======
from leaflet.admin import LeafletGeoAdmin
from django.contrib import admin

from . import models as fields_models


admin.site.register(fields_models.FieldPlot, LeafletGeoAdmin)
>>>>>>> e854a0e1d078f16e921a24a3e201c203befc9c4a
