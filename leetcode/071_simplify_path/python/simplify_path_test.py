
import unittest
import simplify_path

class TestSimplify_Path(unittest.TestCase):
    def test_simplifyPath(self):
        s = simplify_path.Solution()
        self.assertEqual(s.simplifyPath("/home/"),"/home")
        self.assertEqual(s.simplifyPath("/a/./b/../../c/"), "/c")
        self.assertEqual(s.simplifyPath("/a///./b/../../c/"), "/c")
        self.assertEqual(s.simplifyPath("/.."), "/")
        self.assertEqual(s.simplifyPath("/../a/b/c"), "/a/b/c")                
        
if __name__ == '__main__':
    unittest.main()
