from flask import Flask, render_templates

app=Flask(__name__)

@app.route('/')
def home():
    return render_templates("home.html")

@app.route('/about/')
def about():
    return render_templates("about.html")

if __name__=="__main__":
    app.run(debug=True)
