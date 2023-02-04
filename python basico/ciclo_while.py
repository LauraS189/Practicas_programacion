#WHILE

counter = 0
'''
while counter < 20:
    counter += 1
    print(counter)
    
    if counter == 15:
        break
    print(counter)
'''

while counter < 20:
    counter += 1
    if counter < 15:
        continue
    print(counter)