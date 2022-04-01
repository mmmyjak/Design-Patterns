class JakisError(Exception):
    pass


class Adaptee:
    def pierwiastki(self,a,b,c):
        delta = b * b - 4 * a * c

        if delta == 0:
            sqrt_delta = delta ** (1/2)
            return (-b) / 2 * a
        elif delta < 0:
            return None
        else:
            sqrt_delta = delta ** (1/2)
            return (((-b - sqrt_delta) / (2 * a)),((-b + sqrt_delta) / (2 * a)))
    
    def printPierwiastki(self,result):
        if result == None:
            print("Równanie nie ma pierwiastków.")
        elif isinstance(result, float):
            print(f"x = {result}")
        else:
            print(f"x1 = {result[0]}, x2 = {result[1]}")


class Adapter:
    def __init__(self, adaptee: Adaptee):
        self.adaptee = adaptee
    
    def pierwiastkiAdapter(self, rownanie):
        digits = "0123456789"
        digits_op = "0123456789-+"
        a,b,c="","",""
        counter,counter2=0,len(rownanie)-1
        try:
            # get a
            if rownanie[0] == "x": a = 1
            elif rownanie[0] in digits_op:
                a += rownanie[0]
                counter = 1
                while rownanie[counter] in digits:
                    a += rownanie[counter]
                    counter+=1
            else: raise JakisError

            #get c
            if rownanie[len(rownanie)-1] == "x": c = 0
            elif rownanie[len(rownanie)-1] in digits:
                c = rownanie[len(rownanie)-1] + c
                counter2 = len(rownanie) - 2
                while rownanie[counter2] in digits_op:
                    c = rownanie[counter2] + c
                    counter2-=1
                    if rownanie[counter2+1] in "+-":
                        break
                if rownanie[counter2] == "^": c = 0
            else: raise JakisError

            #get b
            for i in range(counter, counter2):
                if rownanie[i] in "-+":
                    counter = i
                    while counter < counter2 and rownanie[counter] in digits_op:
                        b += rownanie[counter]
                        counter +=1
            if b == "": b = 0
            elif b == "+": b = 1
            elif b == "-": b =-1
            if "^2" not in rownanie:
                raise JakisError
        except JakisError:
            print("Źle podany parametr")
        except IndexError:
            print("Podaj parametr")
        else:
            self.adaptee.printPierwiastki(self.adaptee.pierwiastki(float(a),float(b),float(c)))
            

if __name__ == "__main__":
    adaptee = Adaptee()
    adapter = Adapter(adaptee)
    adapter.pierwiastkiAdapter("33x^2+5x-6")
    adapter.pierwiastkiAdapter("x^2+1")
    adapter.pierwiastkiAdapter("x^2")
    adapter.pierwiastkiAdapter("3x^2+6")