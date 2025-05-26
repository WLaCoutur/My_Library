# email_utils.py
def replace_domain(email, old_domain, new_domain):
    if "@" + old_domain in email:
        index = email.index("@" + old_domain)
        new_email = email[:index] + "@" + new_domain
        return new_email
    return email

def sum_of_integers(n):
    if n < 1:
        return 0
    return n + sum_of_integers(n - 1)