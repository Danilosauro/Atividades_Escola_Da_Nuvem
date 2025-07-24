'''Crie um programa que converta temperaturas entre Celsius, Fahrenheit e Kelvin. 
O usuário deve informar a temperatura, a unidade de origem e a unidade para qual deseja converter.'''


temp = float(input("Digite a temperatura: "))
origem = input("Unidade de origem (celsius, fahrenheit, kelvin): ").lower()
destino = input("Unidade de destino (celsius, fahrenheit, kelvin): ").lower()

if origem == destino:
    resultado = temp

elif origem == "celsius" and destino == "fahrenheit":
    resultado = temp * 9 / 5 + 32

elif origem == "celsius" and destino == "kelvin":
    resultado = temp + 273.15

elif origem == "fahrenheit" and destino == "celsius":
    resultado = (temp - 32) * 5 / 9

elif origem == "fahrenheit" and destino == "kelvin":
    resultado = (temp - 32) * 5 / 9 + 273.15

elif origem == "kelvin" and destino == "celsius":
    resultado = temp - 273.15

elif origem == "kelvin" and destino == "fahrenheit":
    resultado = (temp - 273.15) * 9 / 5 + 32

else:
    print("Unidade inválida. Use celsius, fahrenheit ou kelvin.")
    resultado = None


if resultado is not None:
    print(f"\n{temp} {origem.capitalize()} = {resultado:.2f} {destino.capitalize()}")

