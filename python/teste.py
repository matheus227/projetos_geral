#livros emprestados

#lista de livros emprestados
livros_emprestados = {
    
}

def emprestimo():
    while True:
        cd = input("Olá, qual livro deseja emprestar? ")
        autor = input('Qual o autor? ')
        print(f'livro {cd} emprestado')
        
        livros_emprestados[f"{cd}"] = f"{autor}"
        continuar = input('deseja continuar? s/n ').lower()  # Não esqueça os parênteses em lower()
        
        if continuar != 's':  # Se não for 's', para o loop
            break

emprestimo()
print(livros_emprestados)
