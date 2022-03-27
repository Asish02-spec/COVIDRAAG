from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
  return render_template('main.html')

@app.route('/my-link/')
def my_link():
  from python_lib import method
  return "ok:)"
if __name__ == '__main__':
  app.run(debug=True)