from django.db import models
from django.db.models.base import Model
from django.db.models.fields.related import ManyToManyField
from django.template.defaultfilters import slugify

# Create your models here.


class People(models.Model):
    """ Data Model for all the People"""

    people_id = models.IntegerField(primary_key=True)
    people_name = models.CharField(max_length=200)
    people_slug = models.CharField(max_length=220)
    people_gender = models.CharField(max_length=6)
    people_desc = models.TextField(null=True)
    people_profession = models.CharField(max_length=50)
    people_dob = models.DateField(null=True)
    people_img = models.CharField(max_length=400, null=True)

    def __str__(self):
        return self.people_name

    def save(self, *args, **kwargs):
        if not self.people_slug:
            self.people_slug = slugify(self.people_name)

        super(People, self).save(*args, **kwargs)
    
    class Meta:
        
        ordering = ["people_name"]


class Studio(models.Model):
    """Data model for Studios. Might add a column in Future"""

    studio_id = models.CharField(max_length=4, primary_key=True)
    studio_name = models.CharField(max_length=100)
    studio_slug = models.CharField(max_length=120)
    studio_area = models.CharField(max_length=30)
    studio_hq = models.CharField(max_length=120)

    def __str__(self):
        return self.studio_name

    def save(self, *args, **kwargs):
        if not self.studio_slug:
            self.studio_slug = slugify(self.studio_name)

        super(Studio, self).save(*args, **kwargs)


class Movie(models.Model):
    """Data model for the movies"""
    movie_id = models.IntegerField(primary_key=True)
    movie_title = models.CharField(max_length=200)
    movie_slug = models.CharField(max_length=200,null=True)
    movie_year = models.IntegerField(null=True)
    movie_release = models.DateTimeField(null=True)
    movie_imdb = models.CharField(null=True, max_length=10)
    movie_rt = models.CharField(null=True, max_length=10)
    movie_rating = models.CharField(max_length=10,null=True)
    movie_poster = models.CharField(max_length=500,null=True)
    movie_popularity = models.FloatField(null=True)
    movie_awards = models.CharField(max_length=200, null=True)
    movie_desc = models.TextField(null=True)
    movie_director = models.ForeignKey(People, on_delete=models.DO_NOTHING)
    movie_runtime = models.CharField(max_length=12, null=True)
    movie_yt = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.movie_title

    def save(self, *args, **kwargs):
        if not self.movie_slug:
            self.movie_slug = slugify(self.movie_title)

        super(Movie, self).save(*args, **kwargs)

    class Meta:
        ordering = ["movie_title"]


class MovieGenre(models.Model):
    """Data model to store the movie casting"""

    mg_movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    mg_genre = models.CharField(max_length=20)

    def __str__(self):
        return self.mg_movie.movie_title


class MovieCast(models.Model):
    """Data model to store the casting Information"""

    mc_movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    mc_star = models.ForeignKey(People, on_delete=models.DO_NOTHING)
    mc_char = models.CharField(max_length=40,null=True)

    def __str__(self):
        return self.mc_star.people_name


class MovieCredit(models.Model):
    """Movie Credits"""

    mc_movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    mc_people = models.ForeignKey(People, on_delete=models.CASCADE)
    mc_role = models.CharField(max_length=60)

    def __str__(self):
        return self.mc_role+" "+self.mc_movie


class Certificate(models.Model):
    """Certificates for the Movies"""

    certificate_id = models.CharField(max_length=30)
    movie_id = models.ForeignKey(Movie, on_delete=models.CASCADE)
    movie_rating = models.CharField(max_length=3)
    issue_authority = models.CharField(max_length=50)
    approval_date = models.DateField

    def __str__(self):
        return self.movie_rating


class ReleaseData(models.Model):
    """Stores the release Information globally"""

    release_id = models.CharField(max_length=10)
    movie_id = models.ForeignKey(Movie, on_delete=models.CASCADE)
    country = models.CharField(max_length=50)
    release_date = models.DateField()

    def __str__(self):
        return self.release_date
