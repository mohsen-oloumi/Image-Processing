import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
with open("sig.TXT") as f:
    content = f.readlines()
x_list= []
y_list = []
for i in range (1,int (content[0])+1):
    line = content[i].strip().split()
    x = int (line[0])
    y = int (line[1])
    x_list.append(x)
    y_list.append(y)


arr = []
for i in range (len (x_list)):
    arr.append((x_list[i],y_list[i]))
plt.plot(x_list, y_list)
plt.show()
x_list= []
y_list = []
pca = PCA(n_components=2)
pca_img = pca.fit_transform (arr)
for i in pca_img:
    x_list.append(i[0])
    y_list.append(i[1])
plt.plot(x_list,y_list)
plt.show()