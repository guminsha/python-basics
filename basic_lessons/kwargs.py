# **kwargs = parameter that will pack all arguments into a dictionary
#           useful so that function can accept a varying amoung of keywords arguments
#           (args = posicional arguments, kargs = keywords arguments)

def hello(**kwargs):
    # print("Hello " + kwargs['first'] + " " + kwargs['last'])
    print("Hello", end=" ")
    for key, value in kwargs.items():
        print(value, end=" ")


hello(tittle="Sr.", first="Rougert", middle="Alexandre", last="Brian")
