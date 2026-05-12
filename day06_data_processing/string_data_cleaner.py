"""Adding docstring to the file string_data_cleaner.py
This file contains functions to clean and manipulate string data.
These functions can be used for various purposes such as formatting names, extracting email domains, counting words in a sentence, replacing sensitive words, checking log levels, summarizing sentences, masking email addresses, checking for palindromes, extracting initials from full names, and formatting phone numbers.
Each function is designed to handle specific string manipulation tasks and can be easily integrated into larger applications or used for data cleaning and preprocessing tasks.
"""


def clean_name(name):
    name = name.strip().title()
    return name


def email_domain(email):
    if "@" in email:
        return email.split("@")[1]
    return "Invalid email"


def count_words(sentence):
    return len(sentence.split())


def replace_sensitive_word(text, bad_word):
    # return text.replace(bad_word, "****", 1) the third param denotes how many occurances should be replaced, if third param is omitted it will replace all occurances
    return text.replace(bad_word, "****")


def check_log_level(log_line):
    if log_line.startswith("INFO"):
        return "INFO"
    elif log_line.startswith("ERROR"):
        return "ERROR"
    elif log_line.startswith("DEBUG"):
        return "DEBUG"
    else:
        return "NONE"


def summarize_sentence(sentence):
    if len(sentence) < 20:
        return sentence
    return sentence[0:20] + "..."


def mask_email(email):
    if "@" not in email:
        return "Invalid email"
    email = email.split("@")
    email = email[0].replace(email[0][1:], "*" * len(email[0][1:])) + "@" + email[1]
    return email


def is_palindrome(text):
    text = text.lower().replace(" ", "")
    if text == text[::-1]:
        return True
    else:
        return False


def extract_initials(full_name):
    names = full_name.split()
    inital = ""
    for name in names:
        inital += name[0]
    return inital.upper()


def format_phone_number(phone_number):
    if len(phone_number) != 10:
        return "Invalid Phone number"
    return phone_number[0:3] + "-" + phone_number[3:6] + "-" + phone_number[6:]


print(clean_name("  Manasa  "))
print(email_domain("test@gmail.com"))
print(count_words("Count the words in my sentence"))
print(replace_sensitive_word("This is a bad word, don't use any bad words", "bad"))
print(mask_email("manasuejshfkkagmail.com"))
print(
    summarize_sentence(
        "This is the summary of the whole sentence that I have provided here"
    )
)
print(check_log_level("INFO: this method is inside extract log level"))

print(is_palindrome("madam"))
print(is_palindrome("hello"))
print(extract_initials("Manasa chandra Shekar"))
print(format_phone_number("6253767654"))
