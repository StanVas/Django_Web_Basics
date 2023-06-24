from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class Profile(models.Model):
    email = models.EmailField(
        null=False,
        blank=False,
    )

    age = models.PositiveIntegerField(
        validators=(
            MinValueValidator(12),
        ),
        null=False,
        blank=False,
    )

    password = models.CharField(
        max_length=30,
        null=False,
        blank=False,
    )

    first_name = models.CharField(
        verbose_name='Last Name',
        max_length=30,
        null=True,
        blank=True,
    )

    last_name = models.CharField(
        verbose_name='First Name',
        max_length=30,
        null=True,
        blank=True,
    )

    profile_picture = models.URLField(
        verbose_name='Profile Picture',
        null=True,
        blank=True,
    )


class Game(models.Model):
    ACTION = "Action"
    ADVENTURE = "Adventure"
    PUZZLE = "Puzzle"
    STRATEGY = "Strategy"
    SPORTS = "Sports"
    BOARD_CARD_GAME = "Board/Card Game"
    OTHER = "Other"

    CATEGORIES = [
        (ACTION, ACTION),
        (ADVENTURE, ADVENTURE),
        (PUZZLE, PUZZLE),
        (STRATEGY, STRATEGY),
        (SPORTS, SPORTS),
        (BOARD_CARD_GAME, BOARD_CARD_GAME),
        (OTHER, OTHER),
    ]

    title = models.CharField(
        max_length=30,
        unique=True,
        null=False,
        blank=False,
    )

    category = models.CharField(
        max_length=15,
        choices=CATEGORIES,
        null=False,
        blank=False,
    )

    rating = models.FloatField(
        validators=(
            MinValueValidator(0.1),
            MaxValueValidator(5.0),
        ),
        null=False,
        blank=False,
    )

    max_level = models.IntegerField(
        validators=(
            MinValueValidator(1),
        ),
        null=True,
        blank=True,
    )

    image_url = models.URLField(
        verbose_name='Image URL',
        null=False,
        blank=False,
    )

    summary = models.TextField(
        null=True,
        blank=True,
    )
