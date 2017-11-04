from sklearn import tree
features = [[19, 0, 0], [6, 1, 1], [22, 0, 0], [8, 2, 1], [10, 0, 0], [5, 3, 0], [8, 4, 0], [10, 2, 0], [8, 0, 1], [5, 4, 0], [15, 3, 1], [10, 1, 0], [8, 5, 0], [6, 5, 0]]
labels = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0]
clf = tree.DecisionTreeClassifier()
clf = clf.fit(features, labels)
print (clf.predict([[3 ,1 ,1 ]]))

# labels
# 0 = food
# 1 = block

# features = [weight, color, texture]