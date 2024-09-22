#12.Write a Python program to convert a list of characters into a string.

#ans:-

my_list = ['K','r','a','s','h','n','i','k','a',' ','p','a','n','j','r','o','l','i','y','a']

char_list = ''
for char in my_list:
    char_list += char
# list1 = ''.join(my_list)
print(char_list)
