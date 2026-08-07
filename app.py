from flask import Flask, render_template, request
import pickle
import os

app = Flask(__name__)

# Optional: Load your ML model if it exists, otherwise just run the app
model_path = 'shopper_tree.pkl'
if os.path.exists(model_path):
    model = pickle.load(open(model_path, 'rb'))
else:
    model = None
    print("Warning: shopper_tree.pkl not found. Predictions won't work until you train the model.")

@app.route('/')
def index():
    # This serves the Landing Page (Get Started)
    return render_template('index.html')

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        # Get form data
        admin_pages = request.form.get('admin_pages')
        duration = request.form.get('duration')
        month = request.form.get('month')
        visitor_type = request.form.get('visitor_type')
        weekend = request.form.get('weekend')

        # TODO: Process data & pass to model
        # prediction = model.predict([[admin_pages, duration, ...]])
        
        # For now, just send a message back to the form page
        return render_template('home.html', prediction="User likely to purchase!")
        
    # If it's a GET request, just show the form
    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True)