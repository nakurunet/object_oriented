#creating fruits class
class Fruits():
        MOST_COMMON_FRUITS = ['banana', 'apple', 'mango', 'tangerine'] #creating a class variable
        def __init__(self,f_type, color, quantity): #creating the parent class constructor
                                                                #defining instance variables
                self.f_type = f_type
                self.color = color
                self.quantity = quantity

                #defining an instance function
        def show_fruit_properties(self):
                print "Type of fruit", self.f_type
                print "Color of fruit", self.color
                print "Quantity of fruit", self.quantity
                
		
class Farm(Fruits): #farm class inherits from Fruits class
	def __init__(self, f_type, color, quantity, soil ):
		Fruits.__init__(self, f_type, color, quantity) #initializing inherited variables 
		self.__soil = soil 
		
	#encapsulation
	def best_soil(self, fruit):
		if Fruits.MOST_COMMON_FRUITS[0] == fruit:
			self.__soil = 'Loam soil for banana'
			print self.__soil
		elif Fruits.MOST_COMMON_FRUITS[1] == fruit:
			self.__soil = 'Sandy Clay soil for apple'
			print self.__soil
		elif Fruits.MOST_COMMON_FRUITS[2] == fruit:
			self.__soil = 'Sandy Loam soil for Mango'
			print self.__soil
		elif Fruits.MOST_COMMON_FRUITS[3] == fruit:
			self.__soil = 'Well drained Loam soil for tangerine'
			print self.__soil
		else:
			print 'Not a common fruit'
