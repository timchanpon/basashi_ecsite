from django.views import generic
from rest_framework import generics

from .models import Word
from .serializers import WordSerializer

import random


class HomeView(generic.TemplateView):
    template_name = 'home.html'


class WordAPIView(generics.ListAPIView):
    serializer_class = WordSerializer

    def get_queryset(self):
        word_count = self.kwargs['word_count']
        pks = Word.objects.filter(word_count=word_count).values_list('pk', flat=True)
        pks_list = list(pks)

        pk = self.kwargs['pk']
        if not pk == 'null':
            pk = Word.objects.get(pk=pk).pk
            if pk in pks_list:
                pks_list.remove(pk)

        pks_random = random.sample(pks_list, 4)
        queryset = Word.objects.filter(pk__in=pks_random)

        return queryset
