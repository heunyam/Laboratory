import pdfminer
from pdfminer.high_level import extract_text

text = extract_text('2222.pdf')
print(text)