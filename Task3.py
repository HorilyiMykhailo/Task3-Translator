from googletrans import Translator, LANGUAGES

translator = Translator()


def CodeLang(lang):
    lang = lang.strip().lower()

    if lang == "ua":
        lang = "uk"

    if lang in LANGUAGES:
        return LANGUAGES[lang].title()

    for code, name in LANGUAGES.items():
        if name.lower() == lang:
            return code

    return "Помилка: невідома мова"


def LangDetect(txt):
    try:
        return translator.detect(txt)
    except Exception:
        return "Помилка визначення мови"


def TransLate(text, lang):
    try:
        check = lang.strip().lower()

        if check == "ua":
            check = "uk"

        if check in LANGUAGES:
            dest_code = check
        else:
            found = CodeLang(lang)
            if "Помилка" in found:
                return found
            dest_code = found

        result = translator.translate(text, dest=dest_code)
        return result.text
    except Exception:
        return "Помилка перекладу"


txt = input("Введіть текст: ")
lang = input("На яку мову перекласти: ")

print("Введений текст:", txt)
print("Мова тексту:", LangDetect(txt))
print("Переклад:", TransLate(txt, lang))
print("CodeLang(\"En\") =", CodeLang("En"))
print("CodeLang(\"English\") =", CodeLang("English"))