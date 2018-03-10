from django.shortcuts import render
from django.views import generic
from .models import BigFootReport

def index(request):
  return render( request, 'index.html' )

class BigFootReportListView(generic.ListView):
  model = BigFootReport

class BigFootReportDetailView(generic.DetailView):
  model = BigFootReport

  def get_context_data(self, **kwargs):
        context = super(BigFootReportListView, self).get_context_data(**kwargs)
        # Create any data and add it to the context
        context['some_data'] = 'This is just some data'
        return context
