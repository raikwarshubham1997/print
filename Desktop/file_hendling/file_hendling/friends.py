file = open('F:\', 'r')
            
content = file.read()

file.close()
print(content)

# for writting a file

user_input = input("Enter your name: ")
my_file = open("F:\", 'w')

content = my_file.write(user_input)

my_file.close()
