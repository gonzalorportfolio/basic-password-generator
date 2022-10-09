import random
def string_random():
  count=0
  final_pass = ""
  while count != pass_length:
    ran_num = random.randint(0,(pass_length-1))
    new_pass.append(site_name_letters[ran_num])
    count = count + 1
  for l in new_pass:
   final_pass = final_pass+l
  cap_char = new_pass[random.randint(0, len(new_pass))].upper()
  print(punch[random.randint(0,10 )]+cap_char+final_pass+str(pass_length+random.randint(0,9)))
pass_length = 0
SNL_amount = 0
site_name_letters = []
new_pass = []
punch = ["!", "@", "#", "$", "%", "^", "&", "(", ")", "<", ">"]
print("Random Password Genorator")
site_name = input("\nenter the name of the site that you will like to create a password for: \n")
requirment = input("Is there a minimum number of Characters? Y/N")
if requirment.upper()=="Y":
  min_rec=int(input("what is the minimum character requirment ")) 
  pass_length = min_rec
  for i in site_name:
    site_name_letters.append(i)
    SNL_amount = SNL_amount+1
  while SNL_amount<pass_length:
    apha = ["z","x","b","m"]
    site_name_letters.append(apha[random.randint(0, 3)])  
    SNL_amount=SNL_amount+1
  string_random()
else:
  for i in site_name:
    pass_length= pass_length+1
    site_name_letters.append(i)
  string_random()
