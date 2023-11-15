def count_letters(give_me_txt):
    low_txt = give_me_txt.lower()
    dict_with_letters = {}

    for letter in low_txt:

        if letter.isalpha():
            if letter in dict_with_letters:
                dict_with_letters[letter] += 1
            else:
                dict_with_letters[letter] = 1

    return dict_with_letters

def calculate_frequency(dict_with_letters):

    sum_of_letters = sum(dict_with_letters.values())
    enother_dict = {}

    for letter, number in dict_with_letters.items():
        enother_dict[letter] = number / sum_of_letters

    return enother_dict

main_str = """
У лукоморья дуб зелёный;
Златая цепь на дубе том:
И днём и ночью кот учёный
Всё ходит по цепи кругом;
Идёт направо — песнь заводит,
Налево — сказку говорит.
Там чудеса: там леший бродит,
Русалка на ветвях сидит;
Там на неведомых дорожках
Следы невиданных зверей;
Избушка там на курьих ножках
Стоит без окон, без дверей;
Там лес и дол видений полны;
Там о заре прихлынут волны
На брег песчаный и пустой,
И тридцать витязей прекрасных
Чредой из вод выходят ясных,
И с ними дядька их морской;
Там королевич мимоходом
Пленяет грозного царя;
Там в облаках перед народом
Через леса, через моря
Колдун несёт богатыря;
В темнице там царевна тужит,
А бурый волк ей верно служит;
Там ступа с Бабою Ягой
Идёт, бредёт сама собой,
Там царь Кащей над златом чахнет;
Там русский дух… там Русью пахнет!
И там я был, и мёд я пил;
У моря видел дуб зелёный;
Под ним сидел, и кот учёный
Свои мне сказки говорил.
"""

letters_numbers = count_letters(main_str)
letters_frequency = calculate_frequency(letters_numbers)

for letter, frequency in letters_frequency.items():
    print(f"{letter}: {round(frequency,2)}")

# Не понимаю почему round некоторые значения не округляет до двух знаков после запятой
'''
Ответ следующий:
у: 0.03
л: 0.04
к: 0.03
о: 0.08
м: 0.05
р: 0.05
ь: 0.01
я: 0.02
д: 0.05
б: 0.02
з: 0.02
е: 0.07
ё: 0.02
н: 0.06
ы: 0.02
й: 0.03
а: 0.08
т: 0.07
ц: 0.01
п: 0.02
и: 0.06
ч: 0.01
ю: 0.0
в: 0.04
с: 0.04
х: 0.02
г: 0.01
ш: 0.0
ж: 0.01
щ: 0.0
'''
