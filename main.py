from flask import Flask, redirect, url_for, request, render_template
app = Flask(__name__)

@app.route('/')
def main():
    return render_template('index.html')

if __name__=="__main__":
    app.run('localhost', 5000, debug=True)