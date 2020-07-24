from WiseStudy import app
from flask import render_template, request, redirect, url_for
from datetime import datetime
import numpy as np


class MathTopics:
    
    mult_excs = 2
    div_excs = 2 
    frac_excs = 0 

    topicDic = {
        0: "Multiplication",
        1: "Division",
        2: "Fraction",
    }

    def excSplit():
       return [2, 2, 0] 
    

class curriculumCard:
    """Class for representing a curriculum card."""
    def __init__(self, bg_color, header, title, text, id):
        self.bg_color= bg_color
        self.header = header
        self.title = title
        self.text = text
        self.id = id

    def printCard(self):
        print("bg_color: " + self.bg_color)
        print("header: " + self.header)
        print("title: " + self.title)
        print("text: " + self.text)


#Curriculum card data

cards = []
cards.append(curriculumCard("bg-success", "Mathematics", "Selected excercises","Selected exercises in the mathematics for development of skills in grades 3-5", "math-card"))
cards.append(curriculumCard("bg-primary", "Reading", "Book list", "Book list for nurturing character, curiosity and inspiration.", "reading-card"))


@app.route('/')
@app.route('/home')
def index():
    """Renders the index page."""
    return render_template(
        'index.html',
        title='Home',
        year= datetime.now().year,
        curriculum_deck = cards,
    )

def getTopicId(exc_id):
    excSplit = MathTopics.excSplit()
    categoryIndexer = list(np.cumsum(excSplit))
    exc_idNum = int(exc_id)
    
    if exc_idNum < categoryIndexer[0]:
        return 0
    else:
        for i in range(1, len(categoryIndexer) - 1):
            if exc_idNum >= categoryIndexer[i-1] and exc_idNum < categoryIndexer[i+1]:
                return i

    
def getTopicStr(exc_id):
    topic_id = getTopicId(exc_id)   

    return MathTopics.topicDic.get(topic_id)



@app.route('/math',methods=['GET','POST'])
def mathPage():
    """Renders the math page."""

    if request.method == 'POST':
        
        exc_id = request.form['exc_id']

        topic = getTopicStr(exc_id)

        return redirect(url_for('excercisePage',exc_id=exc_id, topic=topic))

    return render_template(
        'math.html',
        title='Math',
        year=datetime.now().year,
    )

@app.route('/reading')
def readingPage():
    """Renders the reading page."""
    return render_template(
        'reading.html',
        title='Reading List',
        year=datetime.now().year,
    )

@app.route('/math/excercise/<topic>/<int:exc_id>')
def excercisePage(exc_id, topic):
    """Renders the excercise page."""   

    return render_template(
        'excercise.html',
        title='Excercise',
        year=datetime.now().year,
        exc_id = exc_id,
        topic = topic,
    )



