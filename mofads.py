from flask import Flask
from ruamel.yaml import YAML 
import random

#variables
app = Flask(__name__)
yaml = YAML()

with open("mofdata.yaml") as f:
    data = yaml.load(f.read())


#endpoints
@app.route("/")
def test():
    return "<p>It's Alive!</p>"


@app.route("/data")
def get_data():
    return data


@app.route("/random")
def get_random():
    out = random.choice(list(data))
    return out



#run
if __name__ == "__main__":
    app.run(debug=True)
