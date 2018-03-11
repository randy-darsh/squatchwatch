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

import tablib
from import_export import resources
from core.models import BigFootReport
bigfootreport = resources.modelresource_factory(model=BigFootReport)()
dataset = tablib.Dataset(['', 'New Report'], headers=['id', 'report_number', 'report_class', 'county', 'season', 'location_details',
                                                      'other_witnesses', 'year', 'state', 'observed', 'time_and_conditions',
                                                      'also_noticed', 'other_stories', 'nearest_town', 'nearest_road',
                                                      'environment', 'month', 'date', 'a_g_references'])
result = bigfootreport_resource.import_data(dataset, dry_run=True)
print result.has_errors()
result = bigfootreport_resource.import_data(dataset, dry_run=False)

class BigFootReportResource(resources.ModelResource):

  class Meta:
    model = BigFootReport

