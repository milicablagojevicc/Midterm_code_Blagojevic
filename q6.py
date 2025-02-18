name = "Milica"
# name[2] = "L" # this causes an error
modified_name = name[:2] + "L" + name[3:] #BUT we can reate a new string
print(modified_name)
#With the creation of this new string, we can print the desired outcome (MiLica), but it would be impossible to do so by editing the inital string, since they are IMMUTABLE

#Contrastingly, lists ARE mutable
name_list = ["M", "i", "l", "i", "c", "a"]
name_list[2] = "L" # NOW we can modify the output even after the initial setting
print(name_list)
# new output: ['M', 'i', 'L', 'i', 'c', 'a']