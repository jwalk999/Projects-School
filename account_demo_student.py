"""
Week 13 in-class exercise: Account and GuestAccount.

Run this file as-is first and watch what happens when someone tries to
guess a password on each kind of account. Then see the handout for your
task.
"""


class Account:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.is_locked = False
        self.failed_attempts = 0

    def check_password(self, attempt):
        if self.is_locked:
            return False
        if attempt == self.password:
            self.failed_attempts = 0
            return True
        self.failed_attempts += 1
        if self.failed_attempts >= 3:
            self.is_locked = True
        return False


class GuestAccount(Account):
    """A guest account with its own password check."""

    def check_password(self, attempt):
        return attempt == self.password


def brute_force(account, candidate_passwords):
    """Try a list of candidate passwords against an account, one at a
    time, the way an attacker's script would."""
    for attempt_number, candidate in enumerate(candidate_passwords, start=1):
        if account.check_password(candidate):
            print(f"  Attempt {attempt_number}: '{candidate}' -- SUCCESS. Logged in as {account.username}.")
            return True
        locked_note = " (account is now locked)" if getattr(account, "is_locked", False) else ""
        print(f"  Attempt {attempt_number}: '{candidate}' -- wrong.{locked_note}")
    print("  Ran out of candidate passwords.")
    return False


def main():
    candidates = ["password", "123456", "letmein", "admin", "hunter2", "qwerty"]

    print("=== Trying candidate passwords against a normal Account ===")
    normal = Account("alice", "hunter2")
    brute_force(normal, candidates)
    print(f"Final state: is_locked={normal.is_locked}, failed_attempts={normal.failed_attempts}")

    print()
    print("=== Trying the same candidate passwords against a GuestAccount ===")
    guest = GuestAccount("guest1", "hunter2")
    brute_force(guest, candidates)
    print(f"Final state: is_locked={getattr(guest, 'is_locked', 'N/A -- never set')}")


if __name__ == "__main__":
    main()
