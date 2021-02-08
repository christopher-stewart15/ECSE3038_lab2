from flask import Flask, request, jsonify
import datetime

app = Flask(__name__)
date = datetime.datetime.now()
Test_Num = 0


profile_DB = {
    "sucess": True,
    "data": {
        "last_updated": "2/3/2021, 8:48:51 PM",
        "username": "coolname",
        "role": "Engineer",
        "color": "#3478ff"
    }
}

tank_DB = []

#routes 
@app.route("/")
def home():
    return "Welcome to the home page!"

@app.route("/profile", methods=["GET", "POST", "PATCH"])
def profile():
    if request.method == "POST":
       
        profile_DB["data"]["last_updated"] = (dte.strftime("%c"))
        profile_DB["data"]["username"] = (request.json["username"])
        profile_DB["data"]["role"] = (request.json["role"])
        profile_DB["data"]["color"] = (request.json["color"])
       
        return jsonify(profile_DB)
   
    elif request.method == "PATCH":
        
        profile_DB["data"]["last_updated"] = (dte.strftime("%c"))
        
        x = request.json
        attributes = x.keys()
        
        for attribute in attributes:
            profile_DB["data"][attribute] = x[attribute]
  
        return jsonify(profile_DB)

    else:
        
        return jsonify(profile_DB)

# Routes for tanks
@app.route("/data", methods=["GET", "POST"])
def Tank_data():
    if request.method == "POST":
        global Test_Num
        Test_Num += 1   
        
        posts = {}
       
        posts["id"] = Test_Num
        posts["location"] = (request.json["location"])
        posts["lat"] = (request.json["lat"])
        posts["long"] = (request.json["long"])
        posts["percentage_full"] = (request.json["percentage_full"])

        tank_DB.append(posts)

        return jsonify(tank_DB)

    else:
        
        return jsonify(tank_DB)

@app.route("/data/<int:tankID>", methods=["PATCH", "DELETE"])
def update(tankID):
     if request.method == "PATCH":
        
        for index in tank_DB:
            if index["id"] == tankID:
                    x = request.json
                    attributes = x.keys()
        
                    for attribute in attributes:
                        index[attribute] = x[attribute]
        
        return jsonify(tank_DB) 

     elif request.method == "DELETE":
        # /DELETE
        for index in tank_DB:
            if index["id"] == tankID:
                tank_DB.remove(index)

        return jsonify(tank_DB)

     else:
         # /GET
        return jsonify(tank_DB)

# Main
if __name__ == '__main__':
   app.run(debug = True)