import codecs
encoded = codecs.open('fixtures.json', 'r', 'utf-8').read().encode(
            'ascii', 'backslashreplace')
open('fixtures-encoded.txt', 'w').write(encoded)