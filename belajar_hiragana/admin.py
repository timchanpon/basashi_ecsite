from django.contrib import admin

from .models import Word
from .chars_dict import hiragana


class WordAdmin(admin.ModelAdmin):

    def save_model(self, request, obj, form, change):
        word = obj.word

        # spell
        spell = ''
        for char in word:
            if char in hiragana:
                spell += hiragana[char] + '-'
            else:
                spell = 'ERROR_'
                break
        spell = spell[:-1]

        # word_count
        word_count = len(word)

        obj.spell = spell
        obj.word_count = word_count
        obj.save()


admin.site.register(Word, WordAdmin)
