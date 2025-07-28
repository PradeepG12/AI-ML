# pandas
import pandas as pd # type: ignore

# df = pd.read_csv("gen_csv.csv")
# df["role"] = [["member", "admin"]]

# matplot
# import matplotlib.pyplot as plt # type: ignore
# data = {
#     "years" : [2000,2010,2020,2030],
#     "lang" : ["python", "js", "java", "python"]
# }
# df = pd.DataFrame(data)
# plt.bar(df["lang"], df["years"])
# plt.title("Lang Growth")
# plt.xlabel("lang")
# plt.ylabel("years")
# plt.ylim(2000,2050)
# plt.show()

# numpy
import numpy as np

a = np.array([1,2,3])
# print(a)
b = np.array([[1,2], [2,2], [3,2]])
# print(b)
c = np.zeros((2,1))
# print(c)
d = np.ones((2,5))
# print(d)
e = np.arange(0,11,2)
# print(e)
f = np.random.rand()*6
# print(f)

arr = np.arange(0,30,5)
# print(arr[arr > 10])
arr2 = arr.reshape((2,3))
# print(arr2.flatten())
arr = np.arange(12).reshape(2,6)
print(arr)
print(arr[:1, :2])

