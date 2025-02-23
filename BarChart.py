import matplotlib.pyplot as plt

Continents="Africa","Asia","Europe","North America","Oceania","South America","Soviet Union"
Area=11.7,10.4,1.9,9.4,3.3,6.9,7.9

plt.bar(Continents,Area,color='orange',width=0.5)
plt.xlabel("Continents")
plt.ylabel("Area") 
plt.title("Bar Chart ")
plt.xticks(rotation=65)
plt.grid()
plt.show()
