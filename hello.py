from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/exec')
def hello2():
    import Hello2
    print("done")
    return render_template('home.html')

@app.route('/about/')
def about():
    return render_template('about.html')

@app.route('/map/')
def map():
    return render_template('map.html')

if __name__ == '__main__':
	# app.run(host='0.0.0.0')
    app.run(debug=True)