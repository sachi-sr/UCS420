my_dict={
  "name":"Sachi Srivastava",
  "roll no": "1024170398",
  "branch":"COPC",
  "age":21,
  "city":"Patiala"
}
my_dict["location"]=my_dict.pop("city")
print("After renaming city:",my_dict)

my_dict["cgpa"]=8.5
print("After adding CGPA",my_dict)

my_dict["age"]+=1
print("After increasing age:",my_dict)

dict_pop=my_dict.copy()
removed_branch=dict_pop.pop("branch")
print("Using pop():",dict_pop)
print("Removed value:",removed_branch)

dict_del=my_dict.copy()
del dict_del["branch"]
print("Using del:",dict_del)
print("Key-value pairs:")
for key,value in my_dict.items():
  print(f"{key}->{value}")

if "email" in my_dict:
  print("Email:",my_dict["email"])
else:
  print("Email not found in the dictionary.")

friend_dict={
    "name": "Prisha",
    "roll no":"1024150304",
    "branch":"ENC",
    "age":20,
    "city": "Patiala"
  }
merged_dict={**my_dict,**friend_dict}
print("MErged dictionary",merged_dict)

# When both dictionaries have the same key, the value from the
# second dictionary (friend_dict) wins.
string_values = {
    key: value
    for key, value in my_dict.items()
    if isinstance(value, str)
}

print("\nDictionary containing only string values:", string_values)