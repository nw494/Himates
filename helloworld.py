from flask import Flask

# Create a Flask web application
app = Flask(__name__)

# Define a route for the root URL ("/") that displays "Hello, World!"
@app.route("/")
def hello_world():
    return "Hello, World!"

# Run the web app on a local development server
if __name__ == "__main__":
    app.run(debug=True)

    #hi