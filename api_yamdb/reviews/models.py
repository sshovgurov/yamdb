from django.db import models
from users.models import User


class Genre(models.Model):
    name = models.CharField(max_length=64)
    slug = models.SlugField(max_length=32, unique=True) 


class Category(models.Model):
    name = models.CharField(max_length=64)
    slug = models.SlugField(max_length=32, unique=True) 


class Title(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField(
        max_length=255,
        blank=True,
    )
    genre = models.ManyToManyField(
        Genre,
        related_name="titles",
    )
    category = models.ForeignKey(
        Category,
        related_name="titles",
        null=True,
        on_delete=models.SET_NULL,
    )


class Review(models.Model):
    title_id = models.ForeignKey(
        Title,
        on_delete=models.CASCADE,
        related_name="reviews"
    )
    score = models.PositiveIntegerField()
    text = models.TextField(max_length=256)
    pub_date = models.DateTimeField(
        auto_now_add=True,
        db_index=True
    )
    author = models.ForeignKey(
        User,
        related_name="reviews",
        on_delete=models.CASCADE,
    )


class Comment(models.Model):
    review_id = models.ForeignKey(
        Review,
        on_delete=models.CASCADE,
        related_name="comments"
    )
    text = models.TextField(max_length=256)
    pub_date = models.DateTimeField(
        auto_now_add=True,
        db_index=True
    )
    author = models.ForeignKey(
        User,
        related_name="comments",
        on_delete=models.CASCADE,
    )
