import unittest
import math
from occurences import *

class findOccurencesTests(unittest.TestCase):
    def test0(self):
        self.assertEqual(findOccurences('','a'),0)
    def test1(self):
        self.assertEqual(findOccurences('hello','a'),0)
    def test3(self):
        self.assertEqual(findOccurences('a','a'),1)
    def test4(self):
        self.assertEqual(findOccurences('hello','e'),1)
    def test5(self):
        self.assertEqual(findOccurences('hello','l'),2)

class isPrimeTests(unittest.TestCase):
    def test0(self):
        self.assertTrue(isPrime(2))
    def test1(self):
        self.assertTrue(isPrime(3))
    def test2(self):
        self.assertFalse(isPrime(4))
    def test3(self):
        self.assertFalse(isPrime(6)) 
    def test4(self):
        self.assertFalse(isPrime(15))
    def test5(self):
        self.assertTrue(isPrime(31))
    def test6(self):
        self.assertTrue(isPrime(100000007))

class isDivisibleTests(unittest.TestCase):
    def test0(self):
        self.assertTrue(isDivisible(4,2))

class palindromeTests(unittest.TestCase):
    def test0(self):
        self.assertFalse(palindrome("abc"))
    def test1(self):
        self.assertTrue(palindrome("a"))
    def test2(self):
        self.assertTrue(palindrome('madamimadam'))
    def test3(self):
        self.assertTrue(palindrome(""))

class biggestOddTests(unittest.TestCase):
    def test0(self):
        self.assertTrue(perfectCube(0))
    def test1(self):
        self.assertTrue(perfectCube(1))
    def test3(self):
        self.assertFalse(perfectCube(2))  
    def test4(self):
        self.assertTrue(perfectCube(8))
    def test5(self):
        self.assertTrue(perfectCube(-125)) 

class perfectCubeTests(unittest.TestCase):
    def test0(self):
        self.assertEqual(biggestOdd([]),0)
    def test1(self):
        self.assertEqual(biggestOdd([1,2,3,4]),3)
    def test3(self):
        self.assertEqual(biggestOdd([4,2,0,8]),0)  
    def test4(self):
        self.assertEqual(biggestOdd([1]),1)
    def test5(self):
        self.assertEqual(biggestOdd([1,2,3,4,5,6,7,8,9]),9)
    def test6(self):
        self.assertEqual(biggestOdd([-1,1]),1)

class biggestBuriedTests(unittest.TestCase):
    def test0(self):
        self.assertEqual(biggestBuried('abcd51kkk3kk19ghi'),51)
    def test1(self):
        self.assertEqual(biggestBuried('kkk32abce@@-33bb14zzz'),33)
    def test3(self):
        self.assertEqual(biggestBuried('this15isast22ring-55'),55)  
    def test4(self):
        self.assertEqual(biggestBuried('uguyfytdtyr'),0)
    def test5(self):
        self.assertEqual(biggestBuried('diunsdiuncdjnv'),0)

class binaryTests(unittest.TestCase):
    def test0(self):
        self.assertEqual(binary(0),'0')
    def test1(self):
        self.assertEqual(binary(11),'1011')

if __name__ == '__main__':
    unittest.main()