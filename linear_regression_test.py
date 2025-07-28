from sklearn.linear_model import LinearRegression
import pandas as pd
import matplotlib.pyplot as plt

data = {
    "studied": [1,2,3,4,5],
    "marks": [40,50,60,70,80]
}
df = pd.DataFrame(data)
X, y = df[["studied"]], df["marks"]
model = LinearRegression()
model.fit(X, y)

predicted = model.predict([[6]])
print(predicted)
plt.scatter(X, y, color="blue", label="Actual Data")
plt.plot(X, model.predict(X), color="red", label="Regression Line")
plt.xlabel("Hours Studied")
plt.ylabel("Marks Obtained")
plt.title("Linear Regression: Study Hours vs Marks")
plt.legend()
plt.grid(True)
plt.show()