from django.contrib import admin
from mukofotlar.models import Prize

class PrizeAdmin(admin.ModelAdmin):
    list_display = ('id','name','category')
    search_fields = ('name',)
admin.site.register(Prize,PrizeAdmin)

