import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.model_selection import cross_val_score
from sklearn.metrics import accuracy_score

final = pd.read_csv("final.csv")

label = 's5_final'

X = final[['race_African American', 'race_Hispanic', 'race_Caucasian', 'choice_number', 'play_time',
                'priority_final', 'refusal_final']]
y = final[[f'{label}']]

x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=42)



svc = SVC()
svc.fit(x_train, y_train)

y_pred = svc.predict(x_test)

print(accuracy_score(y_test, y_pred))
