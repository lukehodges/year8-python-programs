### 04/03/2020
### Luke Hodges
### basic python graph

# importing the graph module
import matplotlib.pyplot as plt

# defining our x and y coordinates
x = [1,2,3]
y = [2,4,7]

# adding the points to the graph
plt.plot(x, y)

# labeling the graph sides and title
plt.xlabel('time taken')
plt.ylabel('price')
plt.title("my first graph")

# exporting the graph
plt.savefig("result.png")
