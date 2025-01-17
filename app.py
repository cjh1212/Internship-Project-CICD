from flask import Flask, render_template, request
from transformers import AutoTokenizer, AutoModelForSequenceClassification, Trainer
import pandas as pd
from datasets import load_dataset
from datasets import Dataset

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')
    
@app.route('/result', methods=['POST', 'GET'])
def result():

    
    if request.method == 'POST':
        tokenizer = AutoTokenizer.from_pretrained('tokenization/')
        model = AutoModelForSequenceClassification.from_pretrained("model/")

        def tokenize_function(example):
            return tokenizer(example['title'], truncation=True)
            
        sentence = request.form['sentence']
        dictionary = {'title': [sentence]}
        df = pd.DataFrame(dictionary)
        
        dataset = Dataset.from_pandas(df)
        dataset = dataset.map(tokenize_function)

        trainer = Trainer(model=model, tokenizer=tokenizer)
        prediction = trainer.predict(dataset)
        prediction = prediction[0][0].tolist()

        idx = prediction.index(max(prediction))

        if idx == 0:
            cat = 'Business'
        elif idx == 1:
            cat = 'Sports'
        else:
            cat = 'Technology'
        result = cat
        return render_template("result.html", result = result)
 
if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
