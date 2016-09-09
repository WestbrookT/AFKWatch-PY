from flask import Flask, render_template, url_for, request
import json
from keras.models import load_model


model = load_model('afknet.h5')

app = Flask(__name__)

def cmp(li):
	if li[0] > li[1]:
		#not cheating
		return 1
	#cheating
	return 0

@app.route('/', methods=['POST'])
def predict():

	data = request.get_json()

	prediction = model.predict(data)

	return cmp(prediction)