# Skriv funktionen här!
def palindromish(word, grade):
    # Convert string to list of chars.
    if isinstance(word, str):
        word = list(word)

    # Get half length of the word. Dont care about the
    # middle character if it is uneven, so using floor division.
    half_word = len(word) // 2

    # Check so that grade is below half length, else set it.
    if grade > half_word:
        grade = half_word

    count = 0
    # Iterate over first and last char of the list, comparing them.
    # -abs() gets the negative index of the word to read backwards,
    # but 0 is not a negative index so we need index + 1
    while count < half_word and word[count] == word[-abs(count + 1)]:
        count += 1

    if count == grade:
        return True

    return False


if __name__ == "__main__":
    # Skriv exempel på körningar av funktionen här
    #
    # Exempel:
    # print(palindromish("radar", 2))
    # print(palindromish([1, 2, 3, 2, 1], 3))
    # Lägg till fler exempel som visar hur din funktion fungerar
    print(palindromish("radar", 2))  # True
    print(palindromish("tenet", 5))  # True
    print(palindromish("hallojsan", 10))  # False
    print(palindromish("Tenet", 3))  # False
    print(palindromish([1, 2, 3, 50, 60, 3, 2, 1], 3))  # True
    print(palindromish([1, 2, 3, 50, 60, 3, 2, 1], 4))  # False
