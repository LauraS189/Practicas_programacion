def message_creator(text):
    articulo = ('computadora', 'celular', 'cable')
    if text == articulo[0]:
        return 'Con mi computadora puedo programar usando Python'
    elif text == articulo[1]:
        return 'En mi celular puedo aprender usando la app de Platzi'
    elif text == articulo[2]:
        return '¡Hay un cable en mi bota!'

text = 'computadora'
response = message_creator(text)
print(response)