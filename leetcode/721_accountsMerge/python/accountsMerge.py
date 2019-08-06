import collections
class Solution:
    def accountsMerge(self, accounts):
        res = []
        cache = collections.defaultdict(list)
        visited = set()
        for i, acc in enumerate(accounts):
            for email in acc[1:]:
                # find the intersection, same email showing in multiple account
                cache[email].append(i)
        print(cache)
        def dfs(idx, sub_res):
            if idx in visited:
                return
            visited.add(idx)
            for email in accounts[idx][1:]:
                sub_res.add(email)
                for records in cache[email]:
                    # collect each account mapping to this intersection
                    dfs(records, sub_res)
            return
        for idx, acc in enumerate(accounts):
            tmp_res = set()
            dfs(idx, tmp_res)
            if tmp_res:
                res.append([acc[0]] + sorted(list(tmp_res)))
        return res
    
class Solution2(object):
    def accountsMerge(self, accounts):
        merged_accounts = []
        for account in accounts:
            idx = self.findByAccountName(merged_accounts, account[0])
            if idx != -1  and self.commonEmailFound(account, merged_accounts[idx]):
                merged_accounts[idx] = self.merge(merged_accounts[idx], account)
            else:
                merged_accounts.append(account)
        return merged_accounts
                                                    
    def findByAccountName(self, merged_accounts, account_name):
        for idx in range(len(merged_accounts)):
            if merged_accounts[idx][0] == account_name:
                return idx
        return -1

    def merge(self, target_account, account):
        target_emails = target_account[1:]
        account_emails = account[1:]
        target_emails.extend([el for el in account_emails if el not in target_emails])
        merged_account = [account[0]] + sorted(target_emails)
        return merged_account

    def commonEmailFound(self, account, target_account):
        target_emails = target_account[1:]
        account_emails = account[1:]
        common_emails = [el for el in target_emails if el in account_emails]
        if len(common_emails) > 0:
            return True
        else:
            return False
        
