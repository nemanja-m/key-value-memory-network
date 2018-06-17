import torchtext


CPU = -1
DATA_PATH = 'data/processed/data.csv'


class Dataset(object):

    def __init__(self, path=DATA_PATH, batch_size=32):
        print('\nLoading dataset')

        self._batch_size = batch_size
        self._device = CPU

        self._field = torchtext.data.Field(tokenize='spacy',
                                           lower=True,
                                           batch_first=True)

        fields = [
            ('query', self._field),
            ('response', self._field),
        ]

        self.data = torchtext.data.TabularDataset(
            path=path,
            format='csv',
            fields=fields
        )

        print(' - Building vocabulary')
        self._field.build_vocab(self.data)
        self.vocab = self._field.vocab

        self.iterator = torchtext.data.BucketIterator(
            self.data,
            batch_size=self._batch_size,
            repeat=False,
            device=self._device
        )

    def process(self, batch, train=True):
        return self._field.process(batch, device=self._device, train=train)

    def numericalize(self, tokens):
        return self._field.numericalize([tokens], device=self._device)
