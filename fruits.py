#creating fruits class
class Fruits():
        MOST_COMMON_FRUITS = ['banana', 'apple', 'mango', 'tangerine'] #creating a class variable
        def __init__(self,f_type, color, quantity): #creating the parent class constructor
                                                                #defining instance variables
                self.f_type = f_type
                self.color = color
                self.quantity = quantity

                #defining an instance function
        def show_fruit_properties(self,fruit):
                
                if Fruits.MOST_COMMON_FRUITS[0] == fruit:
			self.__soil = 'Type of fruit: banana'
			print self.__soil
                        print "Color of fruit: Yellow"
                        print "Quantity of fruit: 100 in a Bunch"
		elif Fruits.MOST_COMMON_FRUITS[1] == fruit:
			self.__soil = 'Type of fruit: apple'
			print self.__soil
                        print "Color of fruit: Green or Red"
                        print "Quantity of fruit: 200 in a Tree"
			
		elif Fruits.MOST_COMMON_FRUITS[2] == fruit:
			self.__soil = 'Type of fruit: mango'
			print self.__soil
                        print "Color of fruit: Green"
                        print "Quantity of fruit: 90 in a Tree"
		elif Fruits.MOST_COMMON_FRUITS[3] == fruit:
			self.__soil = 'Type of fruit: tangerine'
			print self.__soil
                        print "Color of fruit: Orange"
                        print "Quantity of fruit: 120 in a Tree"
		
class Farm(Fruits): #farm class inherits from Fruits class
	def __init__(self, f_type, color, quantity, soil ):
		Fruits.__init__(self, f_type, color, quantity) #initializing inherited variables 
		self.__soil = soil 
		
	#encapsulation
	def best_soil(self, fruit):
		if Fruits.MOST_COMMON_FRUITS[0] == fruit:
			self.__soil = 'Loam soil is best for banana'
			print self.__soil
		elif Fruits.MOST_COMMON_FRUITS[1] == fruit:
			self.__soil = 'Sandy Clay soil is best for apple'
			print self.__soil
		elif Fruits.MOST_COMMON_FRUITS[2] == fruit:
			self.__soil = 'Sandy Loam soil is best for Mango'
			print self.__soil
		elif Fruits.MOST_COMMON_FRUITS[3] == fruit:
			self.__soil = 'Well drained Loam soil is best  for tangerine'
			print self.__soil
		else:
			print 'Not a common fruit'
