# in the_bank.py
class Account(object):
    ID_COUNT = 1
    def __init__(self, name, **kwargs):
        self.__dict__.update(kwargs)
        self.id = self.ID_COUNT
        Account.ID_COUNT += 1
        self.name = name
        if not hasattr(self, 'value'):
            self.value = 0
        if self.value < 0:
            raise AttributeError("Attribute value cannot be negative.")
        if not isinstance(self.name, str):
            raise AttributeError("Attribute name must be a str object.")

    def transfer(self, amount):
        self.value += amount

# in the_bank.py
class Bank(object):
    """The bank"""
    def __init__(self):
        self.accounts = []

    def add(self, new_account) -> bool:
        """ Add new_account in the Bank
        @new_account: Account() new account to append
        @return
        True if success, False if an error occured
        """
        # test if new_account is an Account() instance and if
        # it can be appended to the attribute accounts
        # ... Your code
        try:
            if isinstance(new_account, Account):
                check = self.get_account(new_account.name)
                if not check == None and check.name == new_account.name:
                    print("failed")
                    return False
                
                self.accounts.append(new_account)
                print("Account added")
                return True
            else:
                return False

        except Exception as e:
            print(f"Exception: {e}")
            return False

    
        
    def transfer(self, origin, dest, amount) -> bool:
        """" Perform the fund transfer
        @origin: str(name) of the first account
        @dest:
        str(name) of the destination account
        @amount: float(amount) amount to transfer
        @return
        True if success, False if an error occured
        """
        if not isinstance(origin, str) or not isinstance(dest, str):
            print("Error: origin or dest are not str")
            return False
        if not isinstance(amount, (int, float)) or amount < 0:
            print("Error: amount is not a number or less than 1")
            return False
        sender = self.get_account(origin)
        rec = self.get_account(dest)
        if not sender == None and not rec == None:
            if sender.value < amount:
                print(f"Sender had less than {amount}: transaction failed")
                return False
            rec.transfer(amount)
            return True
        return False

    def fix_account(self, name) -> bool:
        """ 
        YOU WILL HAVE TO MODIFY THE INSTANCES ATTRIBUTES IN ORDER TO FIX THEM.
        fix account associated to name if corrupted
        @name:
        str(name) of the account
        @return True if success, False if an error occured
        """
        if not isinstance(name, str):
            print("Cant fix since name is not a str")
            return False
        fix = self.get_account(name)
        if fix is None:
            print("No account with that name")
            return False
        to_fix = self.is_corrupt(fix)
        if len(to_fix) == 0:
            print("Account not corrupted")
            return True
        else:
            for var in to_fix:
                
        return False
                
    def is_corrupt(self, name):
        """check everything and return corrupted or None when ok"""
        check = self.get_account(name)
        brokenVars = []
        if len(check.__dict__) % 2 == 0:
            brokenVars.append('Uneven')
        for key, val in check.__dict__.items():
            if key.startswith('b'):
                brokenVars.append(key)
            if key == 'name' and not isinstance(val ,str):
                brokenVars.append(key)
            if key == 'id' and not isinstance(val, int):
                brokenVars.append(key)
            if key == 'value' and not isinstance(val, (int, float)):
                brokenVars.append(key)
        return None

    def get_account(self, name):
        for account in self.accounts:
            if account.name == name:
                return account
        return None