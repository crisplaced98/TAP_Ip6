from wrapper_hasNext import wrapper_hasNext
class Test:

    def test(c):
        '''lista = ['uno', 'dos', 'tres', 'cuatro', 'tres']
        for value in lista:
            c.append(value)'''

        for elem in c:
            print(elem)
        print('---------------------------------')

    def test2(c):
        for value in c:
            print(value)
        print('---------------------------------')

    def test3(c):
        it = wrapper_hasNext(c)
        while it.hasNext():
            print(it.__next__())
        print('---------------------------------')

    lista = ['uno', 'dos', 'tres', 'cuatro', 'tres']
    c = []
    for value in lista:
        c.append(value)

    test(c)
    test2(c)    #En Python no es ilegal
    test3(c)