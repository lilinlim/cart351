from flask import Flask,render_template,request,redirect,url_for, jsonify
import os #os means operating system, related to filepaths, etc
from uploader import convert_image_to_ascii
#NOTE no need for PIL because its in the ASCII files

app = Flask(__name__)

#configuration of file uploads
UPLOAD_FOLDER = 'static/uploads' 
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024 # 16 MB limit

#default route
@app.route('/')
def index():
   return render_template("index.html")

#route to upload image
@app.route('/uploading')
def uploadImage():
    return render_template("upload.html")

#showing convertion
@app.route("/conversionComplete", methods=["POST"])
def conversionComplete():

    uploadedfile = request.files["the_file"]

    filePath = os.path.join(app.config["UPLOAD_FOLDER"], uploadedfile.filename)
    app.logger.info(filePath)

    uploadedfile.save(filePath)
    app.logger.info(uploadedfile.filename)
    
    ascii_art = convert_image_to_ascii(filePath, 80)

    #returns the image
    return jsonify({"imagePath": filePath, "asciiArt": ascii_art})

#always at the end
app.run(debug=True)