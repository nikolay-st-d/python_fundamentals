import random

word = ''
for i in range(10):
    vovels = list('aeiouy')
    consonants = list('bcdfghjklmnpqrstvwxz')
    sr = ['co', 'mo', 'do', 'ta', 'ka', 'ku']
    vovel = random.choice(vovels)
    consonant = random.choice(consonants)
    sr = random.choice(sr)

    word = sr
    word += consonant
    word += vovel
    word += sr

    print(word)
