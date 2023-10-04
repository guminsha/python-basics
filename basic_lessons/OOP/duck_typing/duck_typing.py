# Duck Typing = concept where the class of an object is less important than the methods/attributes
#               class type is not checked if minimum methods/attributes are present
#               "If it walks like a duck, and it quacks like a duck, then it must be a duck."

import duck
import chicken
import person

duck = duck.Duck()
chicken = chicken.Chicken()
person = person.Person()

person.catch(duck)
