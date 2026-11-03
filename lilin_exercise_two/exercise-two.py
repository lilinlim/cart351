from flask import Flask,render_template,request,redirect,url_for
import requests
app = Flask(__name__)


# the default route
@app.route("/")
def index():
      return render_template("index.html")

#*************************************************
#Task-1: GET REQUEST
@app.route("/t1")
def t1():
    return render_template("t1.html",have_results=False)
#*************************************************
@app.route("/getSearchCriteria")
def getSearchCriteria():
    #fill me in :
    result = request.args["searching"]
    url = f"https://images-api.nasa.gov/search?q={result}&media_type=image"
    response = requests.get(url)
    data = response.json()

    description = data['collection']['items'][0]['data'][0]['description']
    
    #replace the empty space to be url encoded
    imgFromNasa = data['collection']['items'][0]['links'][0]['href']
    imgFromNasa = imgFromNasa.replace(' ', '%20')

    return render_template("t1.html",
                            have_results = True,
                            description = description,
                            imgPath = imgFromNasa
                                           
                           )
    pass

#*************************************************
# #Task-2: GET REQUEST
@app.route("/t2")
def t2():
    return render_template("t2.html")
#*************************************************
@app.route("/getSearchCriteriaAdv")
def getSearchCriteriaAdv():
 #fill me in :
    result = request.args["searching"]
    url = f"https://images-api.nasa.gov/search?q={result}&media_type=image"
    response = requests.get(url)
    data = response.json()
    
    #replace the empty space to be url encoded
    imgFromNasa = data['collection']['items'][0]['links'][0]['href']
    imgFromNasa = imgFromNasa.replace(' ', '%20')
    
    description = data['collection']['items'][0]['data'][0]['description']
    return render_template("t2.html",images = encodedImageLinks)
    pass
#*************************************************

#run
app.run(debug=True)