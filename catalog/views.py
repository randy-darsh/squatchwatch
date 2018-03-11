from django.shortcuts import render
from django.views import generic
from .models import BigFootReport

def index(request):
  return render( request, 'index.html' )

class BigFootReportListView(generic.ListView):
  model = BigFootReport
  paginate_by = 30

class BigFootReportDetailView(generic.DetailView):
  model = BigFootReport

class BigFootReportCreate(generic.CreateView):
  model = BigFootReport
  fields = "__all__"