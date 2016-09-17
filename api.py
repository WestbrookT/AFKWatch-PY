from flask import Flask, render_template, url_for, request
import json, numpy
from keras.models import load_model


model = load_model('afknet.h5')

app = Flask(__name__)

def nonlin(x, deriv=False):
	# if(deriv==True):
	#     return x*(1-x)
	# return 1/(1+np.exp(-x))
	return numpy.tanh(x)

def cmp(li):
	if li[0] > li[1]:
		#not cheating
		return 0
	#cheating
	return 1

@app.route('/', methods=['POST'])
def predict():

	data = json.loads(request.form['points'])
	data = numpy.array(data)
	data = nonlin(data)

	prediction = model.predict(data)
	

	out = []
	for i in prediction:
		out.append(cmp(i))

	return json.dumps(out)

if __name__ == '__main__':
	app.run(debug=True)