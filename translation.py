from googletrans import Translator
translator = Translator()

def translate(filename):
    try:
        with open(filename,mode='r+') as file:
            lines = file.readlines()
            lines="".join(lines).splitlines()
            for line in lines:
                translated = translator.translate(line,dest='ja')
                file.write(f'{line} translated = {translated.text}\n')
                print(translated)
    except(FileNotFoundError,IOError) as error:
            print(f'It appears there was an error : {error}')

translate('../folder/test1.txt')
