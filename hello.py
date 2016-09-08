from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')

def home():
    return render_template('home.html')

@app.route('/about/')
def about():
    return render_template('about.html')

@app.route('/map/')
def map():
    return render_template('map.html')

@app.route('/exec')
def parse(name=None):
    import Parse
    print("done")
    return render_template('tour.html',name=name)


if __name__ == '__main__':
	    # app.run(host='0.0.0.0')
    app.run(debug=True)