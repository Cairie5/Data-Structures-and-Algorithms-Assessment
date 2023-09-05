def word_frequency(sent):
    # Remove punctuation (periods) and convert all words to lowercase
    breaking = "".join([word.lower() for word in sent.split(".")])
    
    # Initialize an empty dictionary to store word frequencies
    dicts = {}
    
    # Initialize an empty list to store word frequencies in the same order as they appear
    word_array = []

    # Split the sentence into words based on spaces
    breaking = breaking.split(" ")
    
    # Loop through the words in the 'breaking' list
    for word in breaking:
        # Check if the word is alphabetical and starts with its first letter
        if word.isalpha() and word.startswith(word[0]):
            # Count the frequency of the current word in the 'breaking' list and append it to 'word_array'
            word_array.append(breaking.count(word))
    
    # Create a dictionary where keys are unique words and values are their frequencies
    for i, j in zip(breaking, word_array):
        if i.isalpha():
            dicts.update({i.lower(): j})

    # Print the resulting dictionary
    print(dicts)

# Example sentence
sentence = "this is   test sentence. this sentence is a test."
print(word_frequency(sentence))
