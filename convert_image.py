# import the following libraries
# will convert the image to text string
import pytesseract	

# adds image processing capabilities
from PIL import Image	

#translates into the mentioned language
from googletrans import Translator	

# Import the required module for text
# to speech conversion
from gtts import gTTS

# This module is imported so that we can
# play the converted audio
import os

# opening an image from the source path
img = Image.open('steve.jpg')	

# describes image format in the output
print(img)						

# path where the tesseract module is installed (Needed on Windows)
# pytesseract.pytesseract.tesseract_cmd = '/Users/abogutalan/opt/anaconda3/lib/python3.8/site-packages/pytesseract/pytesseract.py'

# converts the image to result and saves it into result variable
result = pytesseract.image_to_string(img)
# write text in a text file and save it to source path
with open('original_text.txt',mode ='w') as file:	
	
				file.write(result)
				print(result)

# Language in which you want to convert
language = 'tr'

p = Translator()					
# translates the text into german language
k = p.translate(result,dest=language)	
# print(k)

# write translated text to a file
with open('translated_text.txt',mode ='w') as file:	
	
				file.write(k.text)
				print(k.text)



# Passing the text and language to the engine,
# here we have marked slow=False. Which tells
# the module that the converted audio should
# have a high speed
myobj = gTTS(text=k.text, lang=language, slow=False)

audio_file = "audio.mp3"

# Saving the converted audio in a mp3 file named
# welcome
myobj.save(audio_file)

# Playing the converted file
os.system("mpg321 " + audio_file)
