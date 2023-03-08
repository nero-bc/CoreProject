from colorfield.fields import ColorField
from dynamic_filenames import FilePattern

from django.contrib.postgres.fields import HStoreField
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

from ...characters.models import CharacterModel
from ...episodes.models import EpisodeModel
from ...producers.models import ProducerModel

from .anime_genre import AnimeGenreModel
from .anime_theme import AnimeThemeModel

cover_upload_pattern = FilePattern(filename_pattern="cover/{uuid:s}{ext}")
banner_upload_pattern = FilePattern(filename_pattern="banner/{uuid:s}{ext}")

# Create your models here.


class AnimeNameSynonymModel(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self) -> str:
        return f"{self.name}"

    class Meta:
        verbose_name = "Anime Synonym"


class AnimeModel(models.Model):
    mal_id = models.IntegerField(unique=True, blank=True, null=True)
    anilist_id = models.IntegerField(unique=True, blank=True, null=True)
    kitsu_id = models.IntegerField(unique=True, blank=True, null=True)

    # These 3 fields can't be null or else search vector will throw an error
    name = models.CharField(
        unique=True,
        null=False,
        max_length=1024,
    )
    name_japanese = models.CharField(
        default="",
        null=False,
        blank=True,
        max_length=1024,
    )
    name_synonyms = models.ManyToManyField(AnimeNameSynonymModel, blank=True)

    source = models.CharField(max_length=128, blank=True, null=True)
    aired_from = models.DateTimeField(blank=True, null=True)
    aired_to = models.DateTimeField(blank=True, null=True)

    # Image fields
    banner = models.ImageField(
        upload_to=banner_upload_pattern,
        default=None,
        blank=True,
        null=True,
    )
    cover = models.ImageField(
        upload_to=cover_upload_pattern,
        default=None,
        blank=True,
        null=True,
    )
    # Image field nearest color
    banner_background_color = ColorField(null=True, blank=True)
    cover_background_color = ColorField(null=True, blank=True)

    synopsis = models.TextField(blank=True, null=True)
    background = models.TextField(blank=True, null=True)
    rating = models.FloatField(
        blank=True,
        null=True,
        validators=[
            MaxValueValidator(5),
            MinValueValidator(0),
        ],
    )

    genres = models.ManyToManyField(AnimeGenreModel, blank=True)
    themes = models.ManyToManyField(AnimeThemeModel, blank=True)
    characters = models.ManyToManyField(CharacterModel, blank=True)
    # Producers and studios are the same
    studios = models.ManyToManyField(ProducerModel, blank=True, related_name="studios")
    producers = models.ManyToManyField(ProducerModel, blank=True, related_name="producers")

    recommendations = models.ManyToManyField("self", blank=True)
    episodes = models.ManyToManyField(EpisodeModel, blank=True)

    # Dict Model field
    theme_openings = HStoreField(
        default=dict,
        null=False,
        blank=True,
    )
    theme_endings = HStoreField(
        default=dict,
        null=False,
        blank=True,
    )

    updated = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.name}"

    class Meta:
        verbose_name = "Anime"
