
class Poly():

    __coefs = []
    __order = 0

    def __init__(self, x0, *terms):
        self.__coefs = [x0] + [term for term in terms]
        self.__order = len(terms)

    def evaluate(self, x):
        return sum([self.__coefs[i]*x**i for i in range(len(self.__coefs))])
    
    def display(self):
        poly_as_string = ""
        for i in range(self.__order+1):
            if i > 1 and self.__coefs[i] > 0:
                poly_as_string += "+{}x^{}".format(self.__coefs[i], i)
            elif self.__coefs[i] < 0:
                poly_as_string += "{}x^{}".format(self.__coefs[i], i)
            elif i == 0:
                poly_as_string += "{}".format(self.__coefs[i])
            else:
                poly_as_string += "+{}x".format(self.__coefs[i])
            print(poly_as_string)

        print(poly_as_string)

    def get_order(self):
        return self.__order
    
    def get_coefs(self):
        return self.__coefs

    def __add__(self, other):
        
        max_order = max(self.__order, other.get_order())
        order_diff = self.__order - other.get_order()

        new_coefs = [0]*(max_order + 1)
        if order_diff > 0:
            adj_coefs = other.get_coefs() + [0]*order_diff
            new_coefs = [self.__coefs[i] + adj_coefs[i] for i in range(len(max_order))]
        else:
            adj_coefs = self.__coefs + [0]*order_diff
            new_coefs = [other.get_coefs()[i] + adj_coefs[i] for i in range(len(max_order))]

        return Poly(*new_coefs[0])


poly1 = Poly(1, 1)
poly2 = Poly(0, 2)
poly1.display()
# poly3 = poly1 + poly2
# print(poly2.evaluate(-2))