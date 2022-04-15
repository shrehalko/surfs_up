
# Import dependency
from flask import Flask

# create a new Flask instance
app = Flask(__name__)

# Create Flask Routes. We need to define the starting point, 
# also known as the root. To do this, we'll use the function below.
@app.route('/')
def hello_world():
    return 'Hello world'

@app.route('/')
def Hi():
    return 'Hi Shreha'