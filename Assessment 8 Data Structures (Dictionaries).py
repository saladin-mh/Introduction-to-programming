def read_file(file_path):
    with open(file_path, 'r') as file:
        text = file.read()
    return text
def count_word_frequency(text):
    words = text.lower().split()
    wordCount = {}
    for word in words:
        if word in word_count:
            wordCount[word] += 1
        else:
            wordCount[word] = 1
    return wordCount
def print_most_common_words(wordCount):
    sortedWords = sorted(wordCount.items(), key=lambda item: item[1], reverse=True)
    topWords = sortesWords[:5]
    for word, frequency in topWords:
        print("{word}: {frequency}".format)
def main():
    input_file = 'text.txt'
    text = read_file(input_file)
    worsCount = count_word_frequency(text)
    print("Top common words:")
    print_most_common_words(wordCount)
if __name__ == "__main__":
    main()
