import uuid

from . import validators

from dirtyfields import DirtyFieldsMixin
from django.db import models
from django.contrib.auth.models import User


class BaseModelMixin(models.Model, DirtyFieldsMixin):
    time_created = models.DateTimeField(auto_now_add=True)
    time_edited = models.DateTimeField(auto_now=True)
    modified_by = models.ForeignKey(User)
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )

    class Meta:
        abstract = True


class Note(BaseModelMixin):
    title = models.CharField(
        validators=[validators.min_length_three],
        blank=False,
        max_length=25
    )
    owner = models.ForeignKey(
        User,
        related_name='note_owner'
    )

    def __str__(self):
        return '{0}'.format(self.title)

    def save(self, *args, **kwargs):
        self.clean_fields()
        super(Note, self).save(*args, **kwargs)


class Bullet(BaseModelMixin):
    bullet = models.TextField(max_length=200)
    note = models.ForeignKey(Note)

    def __str__(self):
        return '{0}: {1}'.format(self.note, self.bullet)
