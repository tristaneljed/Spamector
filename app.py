from flask import Flask, request, render_template, json, redirect, url_for, session, abort, Markup
from engine import SpamDetector
app = Flask(__name__)
app.secret_key = 'F12Zr47j\3yX R~X@H!jmM]Lwf/,?KT'

# Defining the basic route and its corresponding request handler
@app.route("/")
def index():

    return render_template('index.html')

	
# Run the engine
@app.route("/RunEngine", methods=['POST', 'GET'])
def RunEngine():

	clearsession()
	OutputMsg = None
	message = None
	
	if request.form['inputMessage'] !="":
	
		message = request.form['inputMessage']
		spam_detector = SpamDetector()
		OutputMsg = spam_detector.predictMessage(message)
		if OutputMsg == "ham":
			OutputMsg = Markup("<img src='../static/img/ham.png' width='50' height='50'/><br>No worries, your message is fine 😉")
		else:
			OutputMsg = Markup("<img src='../static/img/spam.png' width='50' height='50'/><br>Be careful! your message is a spam!")
		return render_template('index.html', message=message, OutputMsg=OutputMsg)
		
	else:
		return redirect(url_for('index'))
		
# Clear the session 
@app.route('/clear')
def clearsession():
    # Clear the session
    session.clear()
    # Redirect the user to the main page
    return redirect(url_for('index'))
	
# Build the model 
@app.route('/build')
def build_model():
	spam_detector = SpamDetector()
	build_results = spam_detector.saveModel()
	return build_results

# Predict the message via command line
@app.route('/predict/<message>')
def predict_message(message):
	spam_detector = SpamDetector()
	return spam_detector.predictMessage(message)

# Checking if the executed file is the main program and run the app	
if __name__ == "__main__":
	app.debug=True
	app.run()