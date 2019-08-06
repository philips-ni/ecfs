
import unittest
import mystack

class TestMystack(unittest.TestCase):
    def test_MyStack(self):
        s = mystack.MyStack()
        s.push(1)
        s.push(2)
        self.assertEqual(s.top(), 2)
        self.assertEqual(s.pop(), 2)
        self.assertEqual(s.empty(), False)        
if __name__ == '__main__':
    unittest.main()
