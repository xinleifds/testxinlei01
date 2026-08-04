import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
data = pd.read_csv("top250.csv")
print("数据集前5行：\n", data.head())
print("\n数据集形状：", data.shape)
print("\n数据集缺失值情况：\n", data.isna().sum())
print("\n数据集统计描述：\n", data.describe())
data.drop(["Actor", "Gross"], axis=1, inplace=True)
data.dropna(how='all',inplace=True)
cols = list(data.columns.values)
cols.pop(cols.index("Rating"))
data = data[cols+["Rating"]]
data["Release Date"] = pd.to_datetime(data["Release Date"])
le = LabelEncoder()
data["Movie Name"] = le.fit_transform(data["Movie Name"])
data["Director"] = le.fit_transform(data["Director"])
ohe = OneHotEncoder(sparse=False)
movie_types_ohe = ohe.fit_transform(data["Movie Types"].values.reshape(-1,1))
movie_types_ohe_df = pd.DataFrame(movie_types_ohe, columns=["Movie_Type_" + str(int(i)) for i in range(movie_types_ohe.shape[1])])
data = pd.concat([data, movie_types_ohe_df], axis=1)
def min_max_normalize(col):
    return (col - np.min(col)) / (np.max(col) - np.min(col))
data["Movie Duration"] = min_max_normalize(data["Movie Duration"])
data["Release Year"] = data["Release Date"].dt.year
data["Release Month"] = data["Release Date"].dt.month
data.drop(["Release Info", "Release Date"], axis=1, inplace=True)
print("\n数据预处理后的数据集前5行：\n", data.head())
plt.figure(figsize=(8,6))
plt.scatter(data["Movie Duration"], data["Rating"], s=10)
plt.xlabel("Movie Duration")
plt.ylabel("Rating")
plt.title("Rating vs Movie Duration")
plt.show()
X = data.drop('Rating', axis=1)
y = data['Rating']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
gbdt = GradientBoostingRegressor(n_estimators=100, learning_rate=0.1, max_depth=3, random_state=42)
gbdt.fit(X_train, y_train)
y_pred = gbdt.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
print("\n均方误差：", mse)


