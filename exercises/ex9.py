def vowel_counter(sentence):
    vowels=['a','e','i','o','u','A','E','I','O','U']
    count=0
    for c in sentence:
         if c in vowels:
            count=count+1
    print(count)


