import phonenumbers

from sys import argv
from re import findall

def validate(line):

    def validate_name(name):
        name = name.split()
        if len(name) < 2:
            name = findall('[A-ZА-Я][^A-ZА-Я]*', *name)
        name = ' '.join(name)
        return name
        
    def validate_age(age):
        age = int(age)
        if age < 1:
            return ''
        return str(age)
        
    def validate_phone(phone):
        phone = phonenumbers.parse(phone, 'RU')
        phone = phonenumbers.format_number(phone, 1)
        return phone
    
    def validate_email(email):
        email = tuple(filter(lambda x: x, email.split('@')))
        if len(email) < 2:
            return ''
        local, domain = email
        domain = tuple(filter(lambda x: x, domain.split('.')))
        if len(domain) < 2:
            return ''
        domain = '.'.join(domain)
        email = '@'.join((local, domain))
        return email
        
    name, age, phone, email = line.split('|')
    name = validate_name(name)
    age = validate_age(age)
    phone = validate_phone(phone)
    email = validate_email(email)
    
    return '|'.join((name, age, phone, email))

if __name__ == '__main__':
    with open(argv[-1], 'r') as f:
        for line in f:
            print(validate(line))
