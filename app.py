import os
from flask import Flask, request, render_template
import numpy as np
import pandas as pd
from sklearn import metrics 
import warnings
import pickle
warnings.filterwarnings('ignore')
from feature import FeatureExtraction

# Load the model
try:
    file = open("model1.pkl","rb")
    gbc = pickle.load(file)
    file.close()
except Exception as e:
    print(f"Error loading model: {e}")
    gbc = None

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        try:
            url = request.form["url"]
            
            # Basic URL validation
            if not url.startswith(('http://', 'https://')):
                url = 'http://' + url
            
            obj = FeatureExtraction(url)
            x = np.array(obj.getFeaturesList()).reshape(1,30) 

            if gbc is not None:
                y_pred = gbc.predict(x)[0]
                y_pro_phishing = gbc.predict_proba(x)[0,0]
                y_pro_non_phishing = gbc.predict_proba(x)[0,1]
                
                return render_template('index.html', xx=round(y_pro_non_phishing,2), url=url)
            else:
                return render_template('index.html', xx=-1, error="Model not loaded")
                
        except Exception as e:
            print(f"Error processing request: {e}")
            return render_template('index.html', xx=-1, error="Error processing URL")
    
    return render_template("index.html", xx=-1)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)
