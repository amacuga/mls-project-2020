# Not finished, wasn't sure how to get model.predict() from jupyter to app.py and index.html

# flask for web app.
import flask as fl
# numpy for numerical work.
import numpy as np

# Create a new web app.
app = fl.Flask(__name__)

# Add root route.
@app.route("/")
def home():
  return app.send_static_file('index.html')

# Add prediction.
@app.route('/predict')
def predict():
  # needs to be modified, now it's just generating random value from uniform distibution
  return {"value": np.random.uniform()}