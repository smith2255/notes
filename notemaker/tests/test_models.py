from .. import models

from django.core.exceptions import ValidationError
from django.db.utils import DatabaseError
from django.test import TestCase
from model_mommy import mommy
from unittest.mock import MagicMock, Mock, patch


class BaseModelTest(TestCase):

    def setUp(self):
        self.user = mommy.make(
            'auth.user'
        )

    def test_base_model_should_not_save(self):
        base_obj = models.BaseModelMixin(
            modified_by=self.user
        )
        with self.assertRaises(Exception):
            base_obj.save()


class NoteModelTest(TestCase):

    def setUp(self):
        self.user = mommy.make(
            'auth.user'
        )

    def test_create_note(self):
        title = "This is a note"
        models.Note.objects.create(
            title=title,
            owner=self.user,
            modified_by=self.user
        )
        note = models.Note.objects.first()
        self.assertEqual(
            note.title,
            title
        )

    def test_create_note_without_a_title(self):
        try:
            models.Note.objects.create(
                owner=self.user,
                modified_by=self.user
            )
        except Exception as e:
            self.assertEqual(
                type(e),
                ValidationError
            )

    def test_create_note_without_a_very_long_title(self):
        title = "This is a really long title with too many characters"

        self.assertTrue(
            len(title) > 25
        )

        try:
            models.Note.objects.create(
                owner=self.user,
                modified_by=self.user
            )
        except Exception as e:
            self.assertEqual(
                type(e),
                ValidationError
            )

    def test_save_method(self):
        note = models.Note(
            title="This is a note",
            owner=self.user,
            modified_by=self.user
        )
        with patch.object(
            models.Note,
            'clean_fields',
            return_value=None
        ) as patch_obj:
            note.save()
        self.assertEqual(
            patch_obj.call_count,
            1
        )
        self.assertEqual(
            models.Note.objects.count(),
            1
        )

    def test_str_method(self):
        note = models.Note.objects.create(
            title="This is a note",
            owner=self.user,
            modified_by=self.user
        )

        self.assertEqual(
            str(note),
            note.title
        )


class BulletModelTest(TestCase):

    def setUp(self):
        self.user = mommy.make(
            'auth.user'
        )
        self.note = mommy.make(
            'notemaker.Note',
            modified_by=self.user,
            owner=self.user
        )

    def test_create_bullet(self):
        bullet = models.Bullet()
        bullet.note = self.note
        bullet.modified_by = self.user
        bullet.bullet = "This is a point"
        bullet.save()

        self.assertEqual(
            models.Bullet.objects.count(),
            1
        )
