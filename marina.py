favoritos = []
receita = (input("receita: "))
quer = (input("você deseja adicionar esta receita aos favoritos? "))

if quer == "sim":
    favoritos.append(receita)
    print("A receita foi adicionada aos favoritos.")
else:
    print("A receita não foi adicionada aos favoritos.")

ver_favoritos = (input("você deseja ver seus favoritos? "))
if ver_favoritos == "sim":
    print(favoritos)