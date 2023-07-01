def string_inside(str,word):
    lenght=len(str)
    loc=lenght//2
    return str[:loc] + word + str[loc:]
print(string_inside('[[]]','python'))    

print(string_inside('[[]]','php'))   