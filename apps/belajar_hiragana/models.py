from django.db import models

import uuid


class Word(models.Model):
    """単語モデル"""

    word = models.CharField(max_length=15, unique=True)

    spell = models.CharField(max_length=60, blank=True, null=True)
    word_count = models.PositiveSmallIntegerField(blank=True, null=True)

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.word
