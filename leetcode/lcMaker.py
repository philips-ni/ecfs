import os
import sys

def createTargetDir(dir_name):
    cmd = "mkdir -p %s" % (dir_name)
    os.system(cmd)
    print "Dir %s created" % dir_name    

def createSolution(target_dir, problem_name, func_name):
    pkg_name = "_".join(problem_name.split("_")[1:])
    src_file_name = "%s.py" % pkg_name
    test_file_name = "%s_test.py" % pkg_name
    src_file_path = "%s/%s" % (target_dir, src_file_name)
    src_content_template = """
class Solution(object):
    def %s(self):
        pass
"""
    src_content = src_content_template % (func_name)
    with open(src_file_path, "w") as f: 
        f.write(src_content)
    print "File %s created" % src_file_path
    
    test_file_path = "%s/%s" % (target_dir, test_file_name)
    content_template = """
import unittest
import %s

class Test%s(unittest.TestCase):
    def test_%s(self):
        s = %s.Solution()
        self.assertEqual(s.%s(), )
if __name__ == '__main__':
    unittest.main()
"""
    test_content = content_template % (pkg_name, pkg_name.title(), func_name, pkg_name, func_name)
    with open(test_file_path, "w") as f: 
        f.write(test_content)
    print "File %s created" % test_file_path        
        
    
def main(argv):
    if len(argv) != 3:
        usage(argv[0])
    else:
        problem_name = argv[1]
        func_name = argv[2]
        current_dir = os.getcwd()
        target_dir = "%s/%s/python" % (current_dir, problem_name)
        createTargetDir(target_dir)
        createSolution(target_dir, problem_name, func_name)
        

def usage(cmd_name):
    print """
Usage: python %s <problem_name> <fun_name>
""" % (cmd_name)

if __name__ == '__main__':
    sys.exit(main(sys.argv))
