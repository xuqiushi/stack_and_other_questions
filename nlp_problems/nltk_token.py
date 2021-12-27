# plot 25 most common words, with stop word stripped out
if __name__ == "__main__":
    from nltk.tokenize import sent_tokenize

    words = ["a", "b", "c", ",", "c", ".", "d"]
    text = str(" ".join(words))
    tokenized_text = sent_tokenize(text)
    # print(tokenized_text)
    from nltk.tokenize import word_tokenize

    tokenized_word = word_tokenize(text)
    # print(tokenized_word)
    from nltk.probability import FreqDist

    fdist = FreqDist(tokenized_word)
    # print(fdist)
    # Frequency Distribution Plot: most commonly occurring words
    import matplotlib.pyplot as plt

    fdist.plot(25, cumulative=False)
    plt.show()
