import pyttsx3
import PyPDF2
reader = pyttsx3.init('sapi5')
voices = reader.getProperty('voices')
reader.setProperty('voice', voices[1].id)

text_We_Want_to_Use = open('how_to_become_software_engineer.pdf', 'rb')

# PDF READER;
pdf_text = PyPDF2.PdfFileReader(text_We_Want_to_Use)

# A single page reading.
sheetText = pdf_text.getPage(2)

text = sheetText.extractText()

reader.say(text)

reader.runAndWait()