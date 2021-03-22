from pathlib import Path

def parse_policy(policy):
    arity_char = policy.split()
    arity_list = arity_char[0].split("-",1)
    return {"min": int(arity_list[0]), "max": int(arity_list[1])}, arity_char[1]

def validate_password_by_policy(pwd_policy_str):
    pwd_policy = pwd_policy_str.split(":", 1)
    policy = pwd_policy[0]
    pwd = pwd_policy[1]
    arity, char = parse_policy(policy)
    occurrences = pwd.count(char)
    return arity["min"] <= occurrences <= arity["max"]

def count_valid_passwords(filename):
    file = open(filename, 'r')
    passwords = file.readlines()
    counter = 0
    for pwd in passwords:
        if validate_password_by_policy(pwd):
            counter += 1
    return counter
