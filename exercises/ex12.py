def word_histogram (sentence):
    word= sentence.split()
    dic= {}
    count=0
    for w in word:
        c=count+1
        if c>1:
            dic[w]= count
    print (dic)

word_histogram("three three three two two one")
