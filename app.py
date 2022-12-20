# import pyrebase
from flask_cors import CORS
from flask import Flask, render_template
app = Flask(__name__)
CORS(app)

# config = {
#   "apiKey": "AIzaSyCs5zm4bUJsGX-pXYRbpQPqLNANrH_3Ie8",
#   "authDomain": "resume-screening-b8567.firebaseapp.com",
#   "databaseURL": "https://resume-screening-b8567-default-rtdb.firebaseio.com",
#   "projectId": "resume-screening-b8567",
#   "storageBucket": "resume-screening-b8567.appspot.com",
#   "messagingSenderId": "134972310230",
#   "appId": "1:134972310230:web:936cda3b0031c154433f77",
#   "measurementId": "G-NRF8TL7ZJR"
# }

# firebase = pyrebase.initialize_app(config)

# db = firebase.database()

@app.route("/")
def home():
    return render_template('login.html')

@app.route("/index")
def index():
    return render_template('index.html')

@app.route("/index_rec")
def index_rec():
    return render_template('index_rec.html')

@app.route("/layout_rec")
def layout_rec():
    return render_template('layout_rec.html')

@app.route("/Portfoliojs")
def Portfoliojs():
    return render_template('Portfoliojs.html')

@app.route("/Profile_rec")
def Profile_rec():
    return render_template('Profile_rec.html')

@app.route("/Post")
def Post():
    return render_template('Post.html')

@app.route("/contact")
def contact():
    return render_template('contact.html')

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/about_rec")
def about_rec():
    return render_template('about_rec.html')


@app.route("/login")
def login():
    return render_template('login.html')

@app.route("/log_rec")
def log_rec():
    return render_template('log_rec.html')


@app.route("/job-list")
def job_list():
    return render_template('job-list.html')

@app.route("/job-detail")
def job_detail():
    return render_template('job-detail.html')

@app.route("/status")
def status():
    return render_template('status.html')

@app.route("/Show_candidates")
def Show_candidates():
    return render_template('Show_candidates.html')

@app.route("/Seeker_profile")
def Seeker_profile():
    return render_template('Seeker_profile.html')

@app.route("/contact_rec")
def Contact_rec():
    return render_template('contact_rec.html')

if __name__=="__main__":
    app.run(debug=True)
    
