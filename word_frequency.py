def word_frequency(sent):
    breaking = "".join([word.lower() for word in sent.split(".")])
    dicts = {}
    word_array = []

    breaking = breaking.split(" ")
    for word in breaking:
        if word.isalpha() and word.startswith(word[0]):
            word_array.append(breaking.count(word))
    for i, j in zip(breaking, word_array):
        if i.isalpha():
            dicts.update({i.lower(): j})

    print(dicts)


sentence = "this is   test sentence. this sentence is a test."
print(word_frequency(sentence))
