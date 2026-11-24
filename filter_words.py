with open("data/words_alpha.txt", "r") as file:
    words = file.read().splitlines()

four_letter_words = [word for word in words if len(word) == 4]

with open("data/four_letter_words.txt", "w") as file:
    file.write("\n".join(four_letter_words))

print(f"Found {len(four_letter_words)} four-letter words")