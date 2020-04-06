from flask import Flask, render_template,request
import requests,urllib.parse

app=Flask(__name__)

@app.route('/',methods=['GET','POST'])
def home():
    if(request.method=='POST'):
        state=request.form['search']
        main_api='https://api.covid19india.org/v2/state_district_wise.json'
        json_data=requests.get(main_api).json()
        return render_template('state.html',json_data=json_data,state=state)
    main_api='https://api.rootnet.in/covid19-in/unofficial/covid19india.org/statewise'
    json_data=requests.get(main_api).json()
    json_data=json_data['data']['statewise']
    return render_template('home.html',json_data=json_data)
@app.route('/helpful_links')
def precautions():
    return render_template('helpful_links.html')
@app.route('/helpline')
def helpline():
    return render_template('helpline.html')

@app.route('/state/<string:state>')
def state(state):
    main_api='https://api.covid19india.org/v2/state_district_wise.json'
    json_data=requests.get(main_api).json()
    return render_template('state.html',json_data=json_data,state=state)

@app.route('/dashboard')
def dashboard():
    return render_template('map.html')
if(__name__=='__main__'):
    app.run(debug=True)