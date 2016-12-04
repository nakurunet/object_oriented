import fruits

inst1 = fruits.Fruits("fruit", "color", 0)
print ""
print "most common fruits are: ", inst1.MOST_COMMON_FRUITS #display class variable fruit list
print ""
a = inst1.MOST_COMMON_FRUITS [0]
b = inst1.MOST_COMMON_FRUITS [1] 
c = inst1.MOST_COMMON_FRUITS [2] 
d = inst1.MOST_COMMON_FRUITS [3] 

def common_fruits(fruit_type=str(raw_input("Enter a common fruit name:  "))):
    if fruit_type == a or fruit_type == b or fruit_type == c or fruit_type == d:
        banana = fruits.Fruits("fruit", "color", 0)
        default = fruits.Fruits("fruit", "color", 0) #creating an instance of Fruits class and assigning values
        f = fruits.Farm(fruit_type,"green",5,"Loam")
        banana.show_fruit_properties(fruit_type)
        print "best soil for "+fruit_type+": ",f.best_soil(fruit_type)
    else:
        print fruit_type + " is NOT a Common Fruit!!"

common_fruits()
		
