import unittest
import sys
sys.path.append("../src/index.py")
import Dict

class TestDict(unittest.TestCase):
    def setUp(self):
        print('setUp...')

    def tearDown(self):
        print('tearDown...')

    def test_init(self):
        d = Dict(a=1, b='test')
        self.assertEquals(d.a, 1)
        self.assertEquals(d.b, 'test')
        self.assertTrue(isinstance(d, dict))

    def test_key(self):
        d = Dict()
        d['key'] = 'value'
        self.assertEquals(d.key, 'value')

    def test_attr(self):
        d = Dict()
        d.key = 'value'
        self.assertTrue('key' in d)
        self.assertEquals(d['key'], 'value')

    def test_keyerror(self):
        d = Dict()
        with self.assertRaises(KeyError):
            value = d['empty']

    def test_attrerror(self):
        d = Dict()
        with self.assertRaises(AttributeError):
            value = d.empty

    def triangles(n):
            L=[]
            if n==1:
                L.append(1)
            if n==2:
                L.append(1)
                L.append(1)	
            if n>2:
                L.append(1)
                L.append(1)
                LUP=triangles(n-1)
                for i in range(1,n-1):
                    L.insert(i,LUP[i-1]+LUP[i])
            return L
            print(triangles(4))

    def yang(n):
            y=[]
            for i in range(n):
                y.append(triangles(i+1))
            return y
            yy=yang(10)	
            for i in range(10):
                print(yy[i])

    if __name__ == '__main__':
        unittest.main()