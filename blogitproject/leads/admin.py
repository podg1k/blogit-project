from django.contrib import admin
from leads.models import Lead
from django.db import models
from django.http import HttpResponse
import csv

# Register your models here.
class ExportCsvMixin:
    def export_as_csv(self, request, queryset):

        meta = self.model._meta
        field_names = [field.name for field in meta.fields]

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename={}.csv'.format(meta)
        writer = csv.writer(response, delimiter=';')

        writer.writerow(field_names)
        for obj in queryset:
            row = writer.writerow([getattr(obj, field) for field in field_names])

        return response
class LeadFormAdmin(admin.ModelAdmin, ExportCsvMixin):
    actions_on_top = True
    actions_on_bottom = False
    list_display = ('id', 'name', 'subject', 'email', 'message', 'created_at_format', 'is_answered')
    list_display_links = ('subject',)
    list_editable = ('is_answered',)
    list_filter = ('is_answered',)
    ordering = ('is_answered', 'id')
    readonly_fields = ('name', 'subject', 'email', 'message', 'created_at')
    search_fields = ('email', 'name')
    actions = ('export_as_csv',)

    def created_at_format(self, obj):
        beauty_data = obj.created_at.strftime('%d.%m.%y %H:%M:%S')
        return beauty_data

admin.site.register(Lead, LeadFormAdmin)