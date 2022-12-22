from django.contrib import admin
from .models import demodb
import csv
from django.http import HttpResponse
#from django.contrib.auth.models import User, Group      #If you want to remove default groups


admin.site.site_header = "Rohan Admin"
admin.site.site_title = "Rohan's Admin Portal"
admin.site.index_title = "Welcome to Rohan's Admin Portal"

# admin.site.unregister(User)   #If you want to remove default groups
# admin.site.unregister(Group)  #If you want to remove default groups



# Register your models here.

@admin.register(demodb)
class modelAdmin(admin.ModelAdmin):
    def get_actions(self, request):
        actions = super().get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions

    actions = ["export_as_csv"]

    def export_as_csv(self, request, queryset):
        meta = self.model._meta
        field_names = [field.name for field in meta.fields]

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename={}.csv'.format(meta)
        writer = csv.writer(response)

        writer.writerow(field_names)
        for obj in queryset:
            row = writer.writerow([getattr(obj, field) for field in field_names])

        return response

    export_as_csv.short_description = "Export Selected"

    list_display = (
        "id",
        "name",
        "number"
    )