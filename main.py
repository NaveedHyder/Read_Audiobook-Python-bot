import pyttsx3
import PyPDF2
pdfReader = PyPDF2.PdfFileReader(open('file.pdf', 'rb'))

speaker = pyttsx3.init()

for page_num in range(pdfReader.numPages):
    text = pdfReader.getPage(page_num).extractText()
    speaker.say(text)
    speaker.runAndWait()
speaker.stop()

speaker.sav_to_file(text, 'audio.mp3')
speaker.runAndWait()
