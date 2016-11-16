from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def welcome():
	return render_template('welcome.html')

@app.route("/create-form")
def createForm():
   return render_template('create.html')

@app.route("/create-task")
def createTask():
	return

@app.route("/update-task")
def updateTask():
	return

@app.route("/delete-task")
def deleteTask():
	return

@app.route("/get-task")
def getTask():
	return

@app.route("/get-tasks")
def getTasks():
	return

@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8888, debug=True)
