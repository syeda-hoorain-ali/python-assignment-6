class A:
    def show(self):
        print('"Call method from class "A"')


class B(A):
    def show(self):
        print('"Call method from class "B"')
        

class C(A):
    def show(self):
        print('"Call method from class "C"')


# class ordering
class D(C, B): 
    pass
    

if __name__ == '__main__':
    obj = D()
    obj.show()
    print(D.mro())
