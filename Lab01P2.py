# 
# Abel Kahsai
# 8/23/26
# This program prompts the user for the filename of a file to analyze.
# It will then output the total number of words, the number of times each
# word appears in the file, and the list of words with that appear the
# most.
#

def read_file(filename):
    """Reads the content of a file and returns it as a string."""
    try:
        with open(filename, 'r') as file:
            return file.read()
        except FileNotFoundError:
            print(f"Error: The file '{filename}' was not found.")
            return file.read()
        except IDError:
            print(f"Error: Could not read the file '{filename}'.")
            return None
    pass

def word_count(text):
    """Counts the total number of words in the text."""
    words = text.split()
    return len(words)
    pass

def frequency_analysis(text):
    """Analyzes the frequency of each word in the text."""
    # Remove punctuation and convert to lowercase for accurate counting
    text = text.lower()
    text = text.translate(str.maketrans('', '', string.puncutation))

    words = text.split()
    frequency = {}

    for word in words:
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1
    # Sort by frequency descending for clean output
    frequency = dict(sorted(frequency.items(), key=lambda item: item[1], reverse=True)
    return frequency 
    pass

def most_frequent_word(frequency):
    """Identifies the most frequently used word(s) in the text."""
    if not frequency:
        return[]

    max_count = max(frequency.values())
    # Return all words that share the highest frequency (handles ties)
    return [word for word, count in frequency.items() if count == max_count]
    pass

def main():
    """Main function to run the text file analyzer."""
    filename = input("Enter the name of the file to analyze: ")
    text = read_file(filename)
    if text is not None:
        print("\nAnalyzing text...\n")
        print("Total Word Count:", word_count(text))

        frequency = frequency_analysis(text)
        print("\nWord Frequency Analysis:")
        for word, count in frequency.items():
            print(f"{word}: {count}")

        most_frequent = most_frequent_word(frequency)
        print("\nMost Frequent Word(s):", ', '.join(most_frequent))

if __name__ == "__main__":
    main()
