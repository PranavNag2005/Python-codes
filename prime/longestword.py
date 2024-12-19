def find_longest_word(sentence):
    words=sentence.split()
    l_word=" "
    for word in words:
        if len(word)>len(l_word):
            l_word=word
    return l_word,len(l_word)
sentence=input()
word,length=find_longest_word(sentence)
print(f"the longest word is{word} and length is{length}")