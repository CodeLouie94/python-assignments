from flask import Flask, render_template  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"
# @app.route('/')
# def hello_world():
#     return 'Hello Flask!'

@app.route('/')
def play():
    return render_template('play.html', num=3, color = "aqua")

@app.route('/play/<int:num>')
def display_boxes(num):
    return render_template("play.html", num=num, color = "aqua")

@app.route('/play/<int:num>/<string:color>')
def display_color_boxes(num, color):
    return render_template('play.html', num=num, color=color)

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.

