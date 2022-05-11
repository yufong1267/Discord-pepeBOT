import googletrans
from pprint import pprint

class Get_transResult():
    def get_transResult(self, sentence , dst = 'en'):
        # Initial
        translator = googletrans.Translator()
        results = translator.translate(sentence , dest=dst)

        return results.text
