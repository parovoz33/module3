def single_root_words(root_word, *other_words):
    root_word = root_word.lower()

    same_words = []

    # Перебираем остальные слова
    for word in other_words:
        lower_word = word.lower()

        if root_word in lower_word or lower_word in root_word:
            same_words.append(word)

    return same_words


result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')

print(result1)  # Ожидаемый вывод: ['richiest', 'orichalcum', 'richies']
print(result2)  # Ожидаемый вывод: ['Able', 'Disable']

