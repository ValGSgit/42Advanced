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
        # add only checks the type of new_account and that no account
        # already stored shares the same name (no corruption check here).
        if not isinstance(new_account, Account):
            return False
        if self.get_account(new_account.name) is not None:
            return False
        self.accounts.append(new_account)
        return True

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
            return False
        if not isinstance(amount, (int, float)) or isinstance(amount, bool):
            return False
        if amount < 0:
            return False
        sender = self.get_account(origin)
        receiver = self.get_account(dest)
        if sender is None or receiver is None:
            return False
        # both accounts must be valid (not corrupted) before any movement
        if self.is_corrupt(sender) or self.is_corrupt(receiver):
            return False
        # a transfer to the same account is valid but moves no funds
        if sender is receiver:
            return True
        if sender.value < amount:
            return False
        sender.transfer(-amount)
        receiver.transfer(amount)
        return True

    def fix_account(self, name) -> bool:
        """
        YOU WILL HAVE TO MODIFY THE INSTANCES ATTRIBUTES IN ORDER TO FIX THEM.
        fix account associated to name if corrupted
        @name:
        str(name) of the account
        @return True if success, False if an error occured
        """
        if not isinstance(name, str):
            return False
        account = self.get_account(name)
        if account is None:
            return False
        if not self.is_corrupt(account):
            return True
        # 1. drop every attribute whose name starts with 'b'
        for key in list(account.__dict__):
            if key.startswith('b'):
                delattr(account, key)
        # 2. guarantee a location attribute (zip/addr) exists
        if not any(k.startswith('zip') or k.startswith('addr')
                   for k in account.__dict__):
            account.addr = ''
        # 3. fix the parity last: a valid account has an odd attr count
        if len(account.__dict__) % 2 == 0:
            account.fixed = True
        return not self.is_corrupt(account)

    def is_corrupt(self, account) -> list:
        """Return the list of corruption issues (empty list == valid)."""
        attrs = account.__dict__
        issues = []
        # even number of attributes
        if len(attrs) % 2 == 0:
            issues.append('even number of attributes')
        # an attribute starting with 'b'
        for key in attrs:
            if key.startswith('b'):
                issues.append(f"attribute '{key}' starts with b")
        # no attribute starting with zip or addr
        if not any(k.startswith('zip') or k.startswith('addr') for k in attrs):
            issues.append('no zip/addr attribute')
        # name, id and value must be present
        for required in ('name', 'id', 'value'):
            if required not in attrs:
                issues.append(f"missing '{required}' attribute")
        # type checks
        if 'name' in attrs and not isinstance(attrs['name'], str):
            issues.append('name is not a str')
        if 'id' in attrs and not isinstance(attrs['id'], int):
            issues.append('id is not an int')
        if 'value' in attrs and not isinstance(attrs['value'], (int, float)):
            issues.append('value is not an int or float')
        return issues

    def get_account(self, name):
        for account in self.accounts:
            if account.name == name:
                return account
        return None