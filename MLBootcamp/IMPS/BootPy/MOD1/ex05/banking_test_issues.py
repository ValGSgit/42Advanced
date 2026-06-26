from the_bank import Account, Bank

if __name__ == "__main__":
    bank = Bank()

    # A healthy account: odd attr count, has zip, valid name/id/value, no 'b' attr
    valid = Account(
        'William John',
        zip='100-064',
        value=6460.0,
        ref='58ba2b9954cd278eda8a84147ca73c87',
        info=None,
        other='vice president',
    )

    # An account built valid, then tampered with so it hits several
    # corruption criteria at once (this is what the bank guards against):
    #   - 'bref' attribute starts with 'b'
    #   - no zip/addr attribute
    #   - value is a str (wrong type)
    corrupt = Account(
        'Smith Jane',
        bref='1044618427ff2782f0bbece0abd05f31',
        value=1000.0,
    )
    # tamper with the instance after creation
    corrupt.value = 'one thousand'

    bank.add(valid)
    bank.add(corrupt)

    for account in bank.accounts:
        issues = bank.is_corrupt(account)
        print(f"--- {account.name} (id={account.id}) ---")
        print(f"attributes: {sorted(account.__dict__)}")
        if not issues:
            print("status   : OK (not corrupted)")
        else:
            print(f"status   : CORRUPTED ({len(issues)} issue(s))")
            for issue in issues:
                print(f"  - {issue}")
        print()

    # Show that fix_account clears the issues it can repair
    print("=== running fix_account('Smith Jane') ===")
    fixed = bank.fix_account('Smith Jane')
    smith = bank.get_account('Smith Jane')
    print(f"fix_account returned: {fixed}")
    print(f"attributes now      : {sorted(smith.__dict__)}")
    print(f"remaining issues    : {bank.is_corrupt(smith)}")
