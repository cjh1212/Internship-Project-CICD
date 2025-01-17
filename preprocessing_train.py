from pathlib import Path
from sklearn.model_selection import train_test_split
from transformers import AutoTokenizer, AutoModelForSequenceClassification
from transformers import Trainer, TrainingArguments, EarlyStoppingCallback
import torch
from datasets import load_dataset
from datasets import load_metric
import numpy as np
import pandas as pd
from datasets import Dataset
from sklearn import preprocessing
import os
os.environ["WANDB_DISABLED"] = "true"

batch_size = 8
warm_up = 200
seed = 12
max_length = 128

df = pd.read_csv('./train_data.csv')
num_labels = len(np.unique(df['label']))
le = preprocessing.LabelEncoder()
df['label'] = le.fit_transform(df['label'])

metric = load_metric("f1")
tokenizer = AutoTokenizer.from_pretrained('bert-base-uncased')
model = AutoModelForSequenceClassification.from_pretrained("bert-base-uncased", num_labels=num_labels)

print("Done loading data and model")

def compute_metrics(eval_pred):
    logits, labels = eval_pred
    predictions = np.argmax(logits, axis=-1)
    return metric.compute(predictions=predictions, references=labels, average="weighted")

def tokenize_function(examples):
    return tokenizer(examples["title"], padding="max_length", truncation=True, max_length=max_length)

train_df, test_df, y_train, y_test = train_test_split(df,
                                                  df['label'],
                                                  stratify=df['label'],
                                                  test_size=0.2,
                                                  random_state=seed)
train_df, dev_df, y_train, y_val = train_test_split(train_df,
                                                  train_df['label'],
                                                  stratify=train_df['label'],
                                                  test_size=0.1,
                                                  random_state=seed)


print("tokenizing data")

train_dataset = Dataset.from_pandas(train_df)
dev_dataset = Dataset.from_pandas(dev_df)
test_dataset = Dataset.from_pandas(test_df)

train_dataset = train_dataset.map(tokenize_function, batched=True)
dev_dataset = dev_dataset.map(tokenize_function, batched=True)
test_dataset = test_dataset.map(tokenize_function, batched=True)


training_args = TrainingArguments(
    output_dir='./results',          
    num_train_epochs=1,              
    per_device_train_batch_size=batch_size,  
    per_device_eval_batch_size=batch_size,   
    warmup_steps=warm_up,                
    weight_decay=0.01,               
    logging_dir='./logs',            
    logging_steps=100,
    # save_strategy="epoch",
    evaluation_strategy="epoch",
    # load_best_model_at_end=True,
    report_to='all'
)

trainer = Trainer(
    model=model,     
    args=training_args,        
    train_dataset=train_dataset,      
    eval_dataset=dev_dataset,
    compute_metrics=compute_metrics,         
)


trainer.train()

results = trainer.evaluate(test_dataset)

message = str(results['eval_f1'])

with open('results.txt', 'w+') as outfile:
  outfile.write(message)
  
trainer.save_model('model')
trainer.save_model('test/model')
