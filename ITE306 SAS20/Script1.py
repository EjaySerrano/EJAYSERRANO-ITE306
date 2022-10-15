from flask import*
app = flask (_name_)

@app.route('/')
def message():
	return render_template('message.html')
if __name__ == '_main_':
    app.run(debug = True)