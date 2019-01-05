from sklearn.metrics import classification_report
import pandas as pd
import re


"""
计算精确率、召回率和F1值，并将其起存储在文件中
"""
def F1toCsv(y_true, y_pred, class_name, filepath):
    string = classification_report(y_true, y_pred, target_names=class_name)
    p = re.compile(r'\n+')
    string = p.split(string)[:-1]
    data = list(map(lambda x : re.sub(r"\s{2,}", "  ", x).strip().split("  "), string))
    data[0].insert(0," ")
    columns, data = data[0], data[1:]
    df = pd.DataFrame(columns=columns,data = index)
    df.to_csv(filepath,index=False)