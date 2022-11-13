from flask import Flask,render_template,request,session, url_for,redirect
from flask_session import Session

app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def index():
    pass
    return render_template('basketball_court.html')


@app.route('/canteen',methods=['GET','POST'])
def canteen():
    pass
    return render_template('canteen.html')

@app.route('/civil_dept',methods=['GET','POST'])
def civil_dept():
    pass
    return render_template('civil.html')

@app.route('/ct_dept',methods=['GET','POST'])
def ct_dept():
    pass
    return render_template('ct.html')

@app.route('/ece_dept',methods=['GET','POST'])
def ece_dept():
    pass
    return render_template('ece.html')

@app.route('/mech_dept',methods=['GET','POST'])
def mech_dept():
    pass
    return render_template('mech.html')

@app.route('/PET_dept',methods=['GET','POST'])
def PET_dept():
    pass
    return render_template('PET_GYM.html')

@app.route('/Playground',methods=['GET','POST'])
def Playground():
    pass
    return render_template('Playground.html')

@app.route('/RO_Plants',methods=['GET','POST'])
def RO_Plants():
    pass
    return render_template('RO_Plants.html')

@app.route('/Robotics',methods=['GET','POST'])
def Robotics():
    pass
    return render_template('Robotics.html')

@app.route('/Tennikoit',methods=['GET','POST'])
def Tennikoit():
    pass
    return render_template('Tennikoit.html')


app.run(host="0.0.0.0",port=5000)
