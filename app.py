import requests
from flask import Flask , request , app , jsonify , url_for , render_template 


app = Flask(__name__ , template_folder = 'templates' , static_folder='statics')
## Load the model

API_URL = "https://api-inference.huggingface.co/models/mahmoudNG/distilbert-base-uncased-finetuned-emotion"
headers = {"Authorization": "Bearer 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"}

def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.json()
	


@app.route('/')
def home():
    return render_template('main.html')



@app.route('/predict' , methods = ['POST'])
def predict():
    data=[' '.join(x for x in request.form.values())][0]
    output = query({
	"inputs": data,
        })
    # print(type(output[0]),output[0])
    for i in range(len(output[0])):
        output[0][i]['score'] = format(output[0][i]['score'] , '0.2f')

    if output[0]:
        return render_template("main.html", my_string="you are ",prediction_emotions =output[0])
    else:
        return render_template("main.html", my_string="you are ",prediction_emotions =output)
# prediction_emotions="you emotions are {}".format(output)
if __name__ =='__main__':
    app.run(debug=True)