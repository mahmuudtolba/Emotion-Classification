import requests
from flask import Flask , request , app , jsonify , url_for , render_template 


app = Flask(__name__ , template_folder = 'templates' , static_folder='statics')
## Load the model

API_URL = "https://api-inference.huggingface.co/models/mahmoudNG/distilbert-base-uncased-finetuned-emotion"
headers = {"Authorization": "Bearer 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"}

def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.json()
	
output = query({
	"inputs": "I like you. I love you",
})


@app.route('/')
def home():
    return render_template('main.html')



@app.route('/predict' , methods = ['POST'])
def predict():
    data=[' '.join(x for x in request.form.values())][0]
    output = query({
	"inputs": data,
        })
    return render_template("main.html",prediction_emotions="you emotions are {}".format(output[0]))

if __name__ =='__main__':
    app.run(debug=True)