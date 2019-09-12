import os

from odf.opendocument import load
from odf.opendocument import OpenDocumentText
from odf.style import Style, TextProperties, ParagraphProperties
from odf.text import H, P, Span

# Carregar documento na memoria
doc = load('label.odt')

# Styles
s = doc.styles
h1style = Style(name="Heading 1", family="paragraph")
h1style.addElement(TextProperties(attributes={'fontsize':"14pt",'fontweight':"bold"}))
h1style.addElement(ParagraphProperties(attributes={"textalign": "center"}))
s.addElement(h1style)

# An automatic style
boldstyle = Style(name="Bold", family="text")
boldprop = TextProperties(fontweight="bold")
boldstyle.addElement(boldprop)
doc.automaticstyles.addElement(boldstyle)

# Text
h=H(outlinelevel=1, stylename=h1style, text="Dalton Francisco Tofoli") # Substituir por nome recebido do servidor
doc.text.addElement(h)
doc.save('label_print.odt')

# Imprimir arquivo via terminal e deletar arquivo
#os.system('lowriter -p label.odt')
#os.system('rm label_print.odt')