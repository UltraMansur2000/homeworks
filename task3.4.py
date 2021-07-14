dictionary = {}


def thesaurus_adv(*args):
    for name in args:
        name_letter = name[0]
        surname_letter = name.split()[-1][0]
        if dictionary.get(surname_letter) is None:
            dictionary[surname_letter] = {name_letter: [name]}
        elif dictionary[surname_letter].get(name_letter) is None:
            dictionary[surname_letter].update({name_letter: [name]})
        else:
            dictionary[surname_letter][name_letter].append(name)


thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева")
print(dictionary)
