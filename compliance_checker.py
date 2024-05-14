import os

def check_sudoers():
    with open('/etc/sudoers', 'r') as f:
        lines = f.readlines()
    for line in lines:
        if line.startswith("Defaults") and "requiretty" in line:
            return True
    return False

if __name__ == "__main__":
    if check_sudoers():
        print("Compliance check passed: requiretty is set in sudoers.")
    else:
        print("Compliance check failed: requiretty is not set in sudoers.")
