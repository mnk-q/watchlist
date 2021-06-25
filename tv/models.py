from django.db import models
from movie.models import People
# Create your models here.
class TVShow(models.Model):
    tv_id = models.AutoField(primary_key=True)
    tv_name = models.CharField(max_length=200)
    tv_slug = models.CharField(max_length=220, null=True, unique=True)
    tv_year = models.CharField(max_length=20)
    tv_season = models.IntegerField(null=True)
    tv_rating = models.CharField(max_length=12, null=True)
    tv_imdb = models.CharField(max_length=9, null=True)
    tv_rt = models.CharField(max_length=9, null=True)
    tv_awards = models.CharField(max_length=100, null=True)
    tv_creator = models.ForeignKey(People, on_delete=models.DO_NOTHING, null=True)
    tv_desc = models.TextField(null=True)
    tv_poster = models.CharField(max_length=400)

    def __str__(self) -> str:
        return self.tv_name


class TVEpisode(models.Model):
    tve_tv = models.ForeignKey(TVShow, on_delete=models.CASCADE)
    season = models.IntegerField()
    episode = models.IntegerField()
    epi_air_date = models.DateField(null=True)
    epi_desc = models.TextField()
    epi_rating = models.CharField(max_length=3, null=True)
    runtime = models.CharField(max_length=15)

    def __str__(self) -> str:
        return self.tve_tv+" S"+str(self.season)+"E"+str(self.episode)

class TVGenre(models.Model):
    tvg_tv = models.ForeignKey(TVShow, on_delete=models.CASCADE)
    tvg_genre = models.CharField(max_length=16)

    def __str__(self) -> str:
        return self.tvg_tv+" "+self.tvg_genre


class Network(models.Model):
    """ Very Similiar to studio model in movie app, but this is a little different."""

    network_id = models.AutoField(primary_key=True)
    network_name = models.CharField(max_length=50)
    network_url = models.CharField(max_length=60)
    network_logo = models.CharField(max_length=200)
    network_plan = models.CharField(max_length=100, null=True)

    def __str__(self) -> str:
        return self.network_name

class Streaming(models.Model):
    """ This and Network class will be common for Movie and App. And Also, Awards will be a seperate App."""
    streaming_network = models.ForeignKey(Network, on_delete=models.CASCADE)
    streaming_tv = models.ForeignKey(TVShow, on_delete=models.CASCADE)
    streaming_notes = models.CharField(max_length=100, null=True)

    def __str__(self) -> str:
        return self.streaming_network+" "+str(self.streaming_tv)

class TVCast(models.Model):
    """Stores Casting Information"""

    tvc_tv = models.ForeignKey(TVShow, on_delete=models.CASCADE)
    tvc_people = models.ForeignKey(People, on_delete=models.DO_NOTHING)
    tvc_char = models.CharField(max_length=25, null=True)

    def __str__(self):
        return self.tvc_people+" "+self.tvc_tv


