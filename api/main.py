#author: Agee Aondo
#Year: 2023
#import all the required modules



from flask import Flask, jsonify,request
from datetime import datetime, timezone
import os

#the two lines below are used only in development
#from dotenv import load_dotenv
#load_dotenv()

#create the flask app instance
app = Flask(__name__)
app.json.sort_keys = False

#set the secret key
app.secret_key = os.getenv("SECRET_KEY")

#get environment variables
slack_ = os.getenv("SLACK_NAME")
repo = os.getenv("REPO")
file = os.getenv("FILE")
track_ = os.getenv("TRACK")


@app.route('/')
def index():
    return '''<h1>This is 2023 HNGx stage 1 project</h1><br> <p>Created by Agee Aondo @dyagee github repo </p>'''

@app.route("/api/v1", methods=["GET"])
def retrieve():
    if request.method == "POST":
        return "<h1>Out of Bound</1>",400
    else:
        qdata = request.args
        name = qdata.get('slack_name')
        trck = qdata.get('track')
       
        if name is not None and trck is not None:
            if name == slack_ and trck == track_:
                now = datetime.now()
                wkday = now.strftime("%A")
                dt = datetime.now(timezone.utc)
                utc_time = datetime.strftime(dt, "%Y-%m-%dT%H:%M:%S")
                data = {
                "slack_name": slack_,
                "current_day": wkday,
                "utc_time": utc_time + dt.tzname(),
                "track": track_,
                "github_file_url": repo,
                "github_repo_url": file,
                "status_code": 200
                }
                return jsonify(data)
            else:
                return "Fatal error; Wrong Credentials"
        else:
            return "Error; missing a vital credential"

if __name__ == "__main__":
    app.run(debug=True)