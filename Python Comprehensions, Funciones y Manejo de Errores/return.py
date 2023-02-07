#Return de diferentes variables

def find_volume(length=1,width=1,height=1,depth=1):
    return length*width*depth, height, 'hola'

result, height, text = find_volume(width=5)
print(result)
print(height)
print(text)