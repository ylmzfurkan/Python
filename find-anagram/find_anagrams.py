import os

def load_words(file_path):
    with open(file_path, "r") as file:
        words = file.read().splitlines()
    return words

def is_anagram(word1, word2):
    return sorted(word1) == sorted(word2)

def find_anagrams(input_word, words):
    anagrams = [word for word in words if is_anagram(input_word, word)]
    return anagrams

if __name__ == "__main__":
    current_directory = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_directory, "words_alpha.txt")
    words = load_words(file_path)

    while True:
        input_word = input("Bir kelime girin (çıkmak için 'q'): ").strip().lower()
        if input_word == "q":
            break

        anagrams = find_anagrams(input_word, words)
        if anagrams:
            print(f"{input_word} için anagramlar: {', '.join(anagrams)}")
        else:
            print(f"{input_word} için anagram bulunamadı.")
