# Reverse vowels in each word of a sentence
# input: baked brie rules
# output: bekad brei relus


# pointers
class SolutionOne:
    def reverse_sentence_vowels(self, sentence: str) -> str:
        arr = sentence.split()
        words = []

        for word in arr:
            word = self.__reverse_word_vowels(word)
            words.append(word)

        return (" ").join(words)

    def __reverse_word_vowels(self, word: str) -> str:
        vowels_set = {"A", "E", "I", "O", "U", "a", "e", "i", "o", "u"}
        i, j = 0, len(word) - 1
        word = list(word)

        while i < j:
            if word[i] not in vowels_set:
                i += 1
                continue
            if word[j] not in vowels_set:
                j -= 1
                continue

            word[i], word[j] = word[j], word[i]
            i += 1
            j -= 1

        return ("").join(word)


# stack
class SolutionTwo:
    def reverse_sentence_vowels(self, sentence: str) -> str:
        arr = sentence.split()
        words = []

        for word in arr:
            word = self.__reverse_word_vowels(word)
            words.append(word)

        return (" ").join(words)

    def __reverse_word_vowels(self, word: str) -> str:
        vowels_set = {"A", "E", "I", "O", "U", "a", "e", "i", "o", "u"}
        vowels_stack = []
        word = list(word)

        for char in word:
            if char in vowels_set:
                vowels_stack.append(char)

        for i in range(len(word)):
            if word[i] in vowels_set:
                word[i] = vowels_stack.pop()

        return ("").join(word)


print(SolutionOne().reverse_sentence_vowels("baked brie rules"))
print(SolutionTwo().reverse_sentence_vowels("baked brie rules"))
