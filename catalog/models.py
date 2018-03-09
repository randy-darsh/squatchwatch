from django.db import models

class BigFootReport(models.Model):
  """
  Model representing a Samsquantch Sighting
  """
  report_number = models.IntegerField(default=0)
  report_class = models.CharField(max_length=200)
  county = models.CharField(max_length=200)
  season = models.CharField(max_length=200)
  location_details = models.TextField(max_length=1000)
  other_witnesses = models.CharField(max_length=200)
  year = models.CharField(max_length=10)
  state = models.CharField(max_length=20)
  observed = models.TextField(max_length=2000)
  time_and_conditions = models.TextField(max_length=1000)
  also_noticed = models.TextField(max_length=1000)
  other_stories = models.TextField(max_length=1000)
  nearest_town = models.CharField(max_length=100)
  nearest_road = models.CharField(max_length=100)
  environment = models.CharField(max_length=500)
  month = models.CharField(max_length=20)
  date = models.CharField(max_length=20)
  a_g_references = models.CharField(max_length=200)

  def get_absolute_url(self):
    """
    Returns the url to acccess a particular BigFootReport instance
    """
    return reverse('bigfootreport-detail', args=[str(self.id)])

  def __str__(self):
    """
    String for representing the Model object.
    """
    return '{0}, {1}'.format(self.report_number, self.report_class, self.county, self.season, 
                             self.location_details, self.other_witnesses, self.year, self.state,
                             self.observed, self.time_and_conditions, self.also_noticed, self.other_stories,
                             self.nearest_town, self.nearest_road, self.environment, self.month, self.date)


