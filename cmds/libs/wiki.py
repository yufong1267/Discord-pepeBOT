import wikipedia

class wiki():
    def get_summary(self , title):
        try:
            #get wiki summary
            final = wikipedia.summary(title , sentences=1)
        except wikipedia.DisambiguationError as e:
            reg = e.options
            final = 'There are too many options can choose, please type full name. \n'
            for r in reg:
                final += r + '\n'

        
        return final
