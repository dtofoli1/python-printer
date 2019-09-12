
import sys
import os

import flask
import requests
from odf.opendocument import load
from odf.opendocument import OpenDocumentText
from odf.style import Style, TextProperties, ParagraphProperties
from odf.text import H, P, Span

app = flask.Flask(__name__)

@app.route('/print', methods=[ 'POST' ])
def print_badge():

    form = flask.request.json
    required_attribute = [ 'name' ]

    for attr in required_attribute:
        if attr not in form:
            return flask.jsonify({
                'message': 'attribute {} required'.format(attr)
            }), 400

    # Carrega documento na memoria
    doc = load('label.odt')

    # Styles
    s = doc.styles
    h1style = Style(name="Heading 1", family="paragraph")
    h1style.addElement(TextProperties(attributes={'fontsize':"12pt",'fontweight':"bold"}))
    h1style.addElement(ParagraphProperties(attributes={"textalign": "center", "verticalalign": "center"}))
    s.addElement(h1style)

    # An automatic style
    boldstyle = Style(name="Bold", family="text")
    boldprop = TextProperties(fontweight="bold")
    boldstyle.addElement(boldprop)
    doc.automaticstyles.addElement(boldstyle)

    # Text
    h=H(outlinelevel=1, stylename=h1style, text=form['name']) # Substituir por nome recebido do servidor
    doc.text.addElement(h)
    doc.save('label_print.odt')

    # Imprimir arquivo via terminal e deletar arquivo
    #os.system('lowriter -p label_print.odt')
    #os.system('rm label_print.odt')

    return flask.jsonify({
        'message': 'printing done'
    }), 200


if __name__ == "__main__":
    
    root_module = os.path.abspath(os.path.curdir)
    sys.path.append(root_module)

    os.environ['FLASK_APP'] = 'ex_7.py'
    os.environ['FLASK_ENV'] = 'development'

    app.run(host='0.0.0.0')