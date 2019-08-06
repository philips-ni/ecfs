
import unittest
import accountsMerge

class TestAccountsmerge(unittest.TestCase):
    def test_accountsMerge(self):
        s = accountsMerge.Solution()
        accounts = [["John", "johnsmith@mail.com", "john00@mail.com"], ["John", "johnnybravo@mail.com"], ["John", "johnsmith@mail.com", "john_newyork@mail.com"], ["Mary", "mary@mail.com"]]
        # merged_accounts = [["John", 'john00@mail.com', 'john_newyork@mail.com', 'johnsmith@mail.com'],  ["John", "johnnybravo@mail.com"], ["Mary", "mary@mail.com"]]
        merged_accounts = s.accountsMerge(accounts)
        print(merged_accounts)

if __name__ == '__main__':
    unittest.main()
