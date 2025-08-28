# Ejercicio 1: Inprimir en cursiva la estrofa de la cancion "Bendita tierra" de kime
#Codigo ANSI para activar cursiva (I) y para restablecer el formato (R)
I = "\033[3m"
R = "\033[0m"

#Primera linea en cursiva
print(f"{I}Vivo enamorado de este suelo, {R}")

#Segunda linea en cursiva
print(f"{I}No me canso de tu luna y de tu cielo, {R}")

#Tercera linea en cursiva
print(f"{I}Porque yo elegi aqui sembrar mis sueños{R}")

#Cuarta linea en cursiva
print(f"{I}Porque Dios lleno de magia este pueblo{R}")

#Quinta linea en cursiva (respetando las comillas internas alrededor de la palabra yerba)
print(f"{I}voy desde cipote entre \"la yerba\"{R}")

#Sexta linea en cursiva
print(f"{I}En mi sangre llevo todos tus paisajes{R}")