from rest_framework import generics

from .models import Word
from .serializers import WordSerializer

import random


class WordAPIView(generics.ListAPIView):
    serializer_class = WordSerializer

    def get_queryset(self):
        pks = Word.objects.filter(word_count=5).values_list('pk', flat=True)
        pks_list = list(pks)
        pks_random = random.sample(pks_list, 4)

        pk = self.kwargs['pk']
        if not pk == 'null':
            pk = Word.objects.get(pk=pk).pk
            while pk in pks_random:
                pks_random = random.sample(pks_list, 4)

        queryset = Word.objects.filter(pk__in=pks_random)

        return queryset
