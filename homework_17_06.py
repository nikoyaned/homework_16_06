# Sentence Program


sentence = str.lower(input('please enter your sentence '))
dir  = {}
ls =sentence.split()
for i in ls:
    dir [i] = ls.count(i)
for i in dir.items() :
    print (i)






# Phone Book Program


new_contact = {}


def add_contact():
  k = str.lower(input())
  j = int (input())
  new_contact[k] = j
  print (new_contact)
  print ("Contact added successfully!")


def  Search_contact():
  contact = str.lower(input())
  if contact in new_contact:
      print (contact,"Number is ",new_contact[contact])
  else:
      print('Contact not found !')


def all_contacts():
  for i in new_contact.items():
    print ("Your Contacts are ")
    print (i)
 

def exit():
  print ('Goodbye')


while True:
    print ("1. Add a new contact")
    print ("2. Search for a contact")
    print ("3. List all contacts")
    print ("4. Exit")
    choose = int (input("Please choose one of  the options "))
    if  choose == 1:
      add_contact()
    if choose == 2:  
      Search_contact()
    if choose == 3:
      all_contacts()
    if choose == 4:
      exit()
      break