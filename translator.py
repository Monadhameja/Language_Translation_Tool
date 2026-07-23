from deep_translator import GoogleTranslator

class Translator:

    def __init__(self):
        pass

    def translate(self, text, source, target):
        try:
            translated = GoogleTranslator(
                source=source,
                target=target
            ).translate(text)

            return translated

        except Exception as e:
            return f"Error: {e}"