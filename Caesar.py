alphabet_rus_1 = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
alphabet_rus_2 = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
alphabet_eng_1 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
alphabet_eng_2 = 'abcdefghijklmnopqrstuvwxyz'
result = ''

print('Введите на каком языке будет текст (английский или русский): ')
language = str(input())
print('Текст нужно зашифровать или расшифровать?')
action = str(input())
if action == 'зашифровать':
    print('Введите текст для шифрования: ')
    text = list(input())
    print('Введите шаг сдвига: ')
    step = int(input())
    if language == 'русский':
        for letter in text:
            place = alphabet_rus_1.find(letter)
            new_place = place + step
            if new_place > 33:
                new_place = new_place - 33
            if place == -1:
                place = alphabet_rus_2.find(letter)
                if place == -1:
                    result += letter
                else:
                    new_place = place + step
                    if new_place > 33:
                        new_place = new_place - 33
                    result += alphabet_rus_2[new_place]
            elif place != -1:
                result += alphabet_rus_1[new_place]
    elif language == 'английский':
        for letter in text:
            place = alphabet_eng_1.find(letter)
            new_place = place + step
            if new_place > 26:
                new_place = new_place - 26
            if place == -1:
                place = alphabet_eng_2.find(letter)
                if place == -1:
                    result += letter
                else:
                    new_place = place + step
                    if new_place > 26:
                        new_place = new_place - 26
                    result += alphabet_eng_2[new_place]
            elif place != -1:
                result += alphabet_eng_1[new_place]
    else:
        print('К сожалению сообщение на этом языке нельзя зашифровать.')
    print(result)
elif action == 'расшифровать':
    print('Введите текст для расшифрования: ')
    text = list(input())
    print('Введите шаг сдвига: ')
    step = int(input())
    if language == 'русский':
        for letter in text:
            place = alphabet_rus_1.find(letter)
            new_place = place - step
            if new_place > 33:
                new_place = new_place - 33
            if place == -1:
                place = alphabet_rus_2.find(letter)
                if place == -1:
                    result += letter
                else:
                    new_place = place - step
                    if new_place > 33:
                        new_place = new_place - 33
                    result += alphabet_rus_2[new_place]
            elif place != -1:
                result += alphabet_rus_1[new_place]
    elif language == 'английский':
        for letter in text:
            place = alphabet_eng_1.find(letter)
            new_place = place - step
            if new_place > 26:
                new_place = new_place - 26
            if place == -1:
                place = alphabet_eng_2.find(letter)
                if place == -1:
                    result += letter
                else:
                    new_place = place - step
                    if new_place > 26:
                        new_place = new_place - 26
                    result += alphabet_eng_2[new_place]
            elif place != -1:
                result += alphabet_eng_1[new_place]
    else:
        print('К сожалению сообщение на этом языке нельзя расшифровать.')
    print(result)
