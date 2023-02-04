name = "Laura"
print (name)

last_name = "Rodriguez"
print(last_name)

full_name = name +" "+ last_name
print(full_name)

quote = "I'm Laura"
print(quote)

quote2 = 'she said "hello"'
print(quote2)

#Format
template = "Hello, my name is " + name + " and my last name is " + last_name
print('v1', template)

template = "Hello, my name is {} and my last name {}".format(name, last_name)
print('v2', template)

template = f"Hello, my name is {name} and my last name is {last_name}"
print('v3', template)