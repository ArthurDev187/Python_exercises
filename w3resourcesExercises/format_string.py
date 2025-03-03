# valor = 70

# print(f'It is very {'expensive' if valor > 50 else 'cheap'}!')

def convert_celcius(faren):
    return (faren - 32) * 5/9

print(f'Valor de F° convertido em C°: {convert_celcius(75):.1f}')