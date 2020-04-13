from flask import Flask, render_template, request, flash, session, redirect
from flask_bootstrap import Bootstrap
import json
import os
import time
from difflib import get_close_matches

app = Flask(__name__)

app.config['SECRET_KEY'] = os.urandom(24)

data = json.load(open('data.json'))

Bootstrap(app)
@app.route('/', methods=['GET','POST'])
def home():
    if request.method == 'POST':
        form = request.form
        Word = form['inputWord']
        temp = Word
        #Converting to lower case
        Word = Word.lower()
        session['input'] = temp
        if Word in data:
            # print(data[Word])
            i=1
            for word in data[Word]:
                session['Word'] = word

                session['index'] = i
                flash(str(session['index']) +". " + session['Word'])
                i+=1
#            return data[Word]
        elif len(get_close_matches(Word, data.keys())) > 0:
            flash('Did you mean ' + get_close_matches(Word, data.keys())[0] + ' instead?','danger')
        else:
            flash('The word doesn\'t exist. Please check again...!', 'danger')
            # print("No such word")

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True);
