<<<<<<< HEAD
from django.contrib import admin
from plots.models import Plot

class PlotsAdmin(admin.ModelAdmin):
    list_display = ('user', 'name', 'wet_date', 'grower')

admin.site.register(Plot)
=======
from django.contrib import admin
from plots.models import Plot

class PlotsAdmin(admin.ModelAdmin):
    list_display = ('user', 'name', 'wet_date', 'grower')

admin.site.register(Plot)
>>>>>>> e854a0e1d078f16e921a24a3e201c203befc9c4a
