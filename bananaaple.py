import fruits

banana = fruits.Fruits("banana", "Yellow", 6) #creating an instance of Fruits class and assigning values
apple = fruits.Farm("apple","green",5,"Loam")

banana.show_fruit_properties()
print "most common fruits are: ", fruits.Fruits.MOST_COMMON_FRUITS #display class fruit list

print "best soil for apple: ",apple.best_soil("apple")
		
