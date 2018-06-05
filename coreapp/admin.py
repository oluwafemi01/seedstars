from django.contrib import admin
from coreapp.models import stores


class storesAdmin(admin.ModelAdmin):
    class Meta:
        model = stores
admin.site.register(stores,storesAdmin)
               

