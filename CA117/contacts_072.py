#!/usr/bin/env python

class Contact(object):
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

    def __str__(self):
        return( "{} {} {}".format(self.name, self.phone, self.email))

class ContactList(object):
    def __init__(self):
        self.d = {}

    def add_contact(self, c):
        self.d[c.name] = c

    def del_contact(self, name):
        if name in self.d:
            del self.d[name]
        else:
            print("Contact list")
            print("-----------")

    def get_contact(self, name):
        try:
            return(self.d[name])
        except KeyError:
            return None

    def __str__(self):
        slist = []
        for k, v in sorted(self.d.items()):
            slist.append('{}'.format(v))
        return '\n'.join(slist)

import sys

def main():
    cl = ContactList()
    for line in sys.stdin:
        [name, phone, email] = line.strip().split()
        c = Contact(name, phone, email)
        cl.add_contact(c)

    c = cl.get_contact('Jimmy')
    print(c)
    c = cl.get_contact('Mary')
    print(c)

    print(cl)
    cl.del_contact('Maggie')
    cl.del_contact('Maggie')

    c = Contact('Sue', '087-6442378', 'sue@eircom.net')
    cl.add_contact(c)
    c = Contact('Fred', '085-8776543', 'fred@yahoo.com')
    cl.add_contact(c)
    print(cl)

if __name__ == '__main__':
    main()
