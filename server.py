from flask import Flask, render_template, request, redirect, session
import random
import datetime
import time

app = Flask(__name__,)
app.secret_key = '\xb8?\xff\xd4\x1a\xdf\x11\xeaiP2[\x8cs\x1d\x17\x9d\xc5\xcf\x7f\xbb\xf0P\xd3'

def randomNum(start, end):
    num = random.randrange(start, end)
    return num
def winLose():
    chance = random.randrange(0,2)
    if chance == 1:
        return True
    else:
        return False

def addActivity(num, gainlost, location):
    timestamp = datetime.datetime.now().strftime("%A, %B %d, %Y - %I:%M %p")
    if location =='farm':
        session['activity'].append(['gain', 'Earned {} gold from the {}. ({})' .format(num, location, timestamp)])
    elif location =='cave':
        session['activity'].append(['gain', 'Earned {} gold from the {}. ({})' .format(num, location, timestamp)])
    elif location =='house':
        session['activity'].append(['gain', 'Earned {} gold from the {}. ({})' .format(num, location, timestamp)])
    elif location =='casino':
        if gainlost =='gain':
            session['activity'].append(['gain', 'Earned {} gold from the {}. ({})' .format(num, location, timestamp)])
        elif gainlost =='lost':
            session['activity'].append(['lost','Lost {} gold from the {}... Ouch!! ({})' .format(num, location, timestamp)])
        else:
            print "Error"
    else:
        print "Error"


@app.route('/')
def index():
    if session['total'] == None:
        session['total'] = 0
    if session['activity'] == None:
        session['activity'] = []
    return render_template('index.html', total=session['total'], activities=session['activity'])

@app.route('/process_money', methods=['POST'])
def gold():
    hiddenInput = request.form['hidden']
    if hiddenInput == 'farm':
        farmGold = randomNum(10, 21)
        session['total'] += farmGold
        addActivity(farmGold, 'gain', 'farm')
    elif hiddenInput == 'cave':
        caveGold = randomNum(5,11)
        session['total'] += caveGold
        addActivity(caveGold, 'gain', 'cave')
    elif hiddenInput == 'house':
        houseGold = randomNum(2,6)
        session['total'] += houseGold
        addActivity(houseGold, 'gain', 'house')
    elif hiddenInput == 'casino':
        casinoGold = randomNum(0,51)
        chance = winLose()
        if chance == True:
            session['total'] += casinoGold
            addActivity(casinoGold, 'gain', 'casino')
        elif chance == False:
            session['total'] -= casinoGold
            addActivity(casinoGold, 'lost', 'casino')
    else:
        print "Error"

    return redirect('/')

@app.route('/reset', methods=['POST'])
def reset():
    session['total'] = 0
    session['activity'] = []

    return redirect('/')

app.run(debug=True)
