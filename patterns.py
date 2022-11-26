import re

def is_valid_mail(potential_mail):
    return re.match(r"\w+@[\w.]+", potential_mail, re.UNICODE)

