from django.contrib import admin
from .models import BigFootReport

# admin.site.register(BigFootReport)
class BigFootReportAdmin(admin.ModelAdmin):
  list_display = ('report_number', 'report_class', 'county', 'season', 'location_details',
                  'other_witnesses', 'year', 'state', 'observed', 'time_and_conditions',
                  'also_noticed', 'other_stories', 'nearest_town', 'nearest_road',
                  'environment', 'month', 'date', 'a_g_references')
  fields = ['report_number', 'report_class', 'county', 'season', 'location_details',
                  'other_witnesses', 'year', 'state', 'observed', 'time_and_conditions',
                  'also_noticed', 'other_stories', 'nearest_town', 'nearest_road',
                  'environment', 'month', 'date', 'a_g_references']

admin.site.register(BigFootReport, BigFootReportAdmin)

