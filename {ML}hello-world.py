from sklearn import tree

### fetures and labels are variables
### fetures are the imput to the classifyer
### labels are the output to the classifyer

### you can change all the variable types to ints instead of strings.

#fetures = [[140, "smooth"], [130, "smooth"], [150, "bumpy"], [170, "bumpy"]]
features = [[180, 0], [54, 1], [148, 0],[32, 1],[36, 1]]

#labels = ["apple", "apple", "orange", "orange"]
labels = [0, 1, 0, 1, 1]

### next we are going to train the classifier, the classifier for this example 
### will be a Decision Tree classifier, a classifyer could be thought of as a box
### of rules and there are many different types of classifiers, but the imput and output
### types are always the same.

clf = tree.DecisionTreeClassifier()
### this classifier is an empty box of rules so we will need to train it with a learning 
### algorithem, at the moment it knows nothing about apples and oranges.

clf = clf.fit(features, labels)
### in scikit the training algorithm is included in the classifier object and its called
### fit or(find patterns in data).

### now we have a trainded classifier and we can pass in some input data using fetures of our new fruit
print (clf.predict([[173 , 0]]))

### after running the program the computer said [1] for orange.