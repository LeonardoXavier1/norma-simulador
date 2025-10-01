# ==============================
# Simulador de Máquina Norma Interativo
# ==============================

import sys

# ------------------------------
# Funções para macros monolíticas
# ------------------------------

def macro_mul_monolitico(r1, r2, destino, registradores):
    """Multiplicação: destino = r1 * r2"""
    registradores[destino] = registradores[r1] * registradores[r2]

def macro_div_monolitico(r1, r2, destino, registradores):
    """Divisão inteira: destino = r1 // r2"""
    if registradores[r2] == 0:
        print("Erro: divisão por zero")
        registradores[destino] = 0
    else:
        registradores[destino] = registradores[r1] // registradores[r2]

# ------------------------------
# Função para inicializar registradores
# ------------------------------
def inicializar_registradores():
    registradores = {}
    n = int(input("Quantos registradores deseja criar? "))
    for i in range(n):
        nome = input(f"Nome do registrador {i+1}: ").strip()
        valor = int(input(f"Valor inicial de {nome}: "))
        registradores[nome] = valor
    return registradores

# ------------------------------
# Menu interativo de execução
# ------------------------------
def executar_interativamente(registradores):
    print("\n=== Execução Interativa ===\n")
    while True:
        print(f"\nEstado atual dos registradores: {registradores}")
        print("\nEscolha a operação a executar:")
        print("1: Adicionar 1 a um registrador (add)")
        print("2: Subtrair 1 de um registrador (sub)")
        print("3: Multiplicação (macro_mul)")
        print("4: Divisão (macro_div)")
        print("5: Mostrar registradores")
        print("0: Sair")

        opcao = input("Digite a opção: ").strip()

        if opcao == "0":
            print("Encerrando execução.")
            break

        elif opcao == "1":
            r = input("Registrador que deseja incrementar: ").strip()
            if r in registradores:
                registradores[r] += 1
                print(f"{r} incrementado em 1.")
            else:
                print("Registrador inválido.")

        elif opcao == "2":
            r = input("Registrador que deseja decrementar: ").strip()
            if r in registradores:
                registradores[r] = max(0, registradores[r] - 1)
                print(f"{r} decrementado em 1.")
            else:
                print("Registrador inválido.")

        elif opcao == "3":
            r1 = input("Registrador 1 (multiplicando): ").strip()
            r2 = input("Registrador 2 (multiplicador): ").strip()
            destino = input("Registrador destino: ").strip()
            if r1 in registradores and r2 in registradores and destino in registradores:
                macro_mul_monolitico(r1, r2, destino, registradores)
                print(f"{destino} = {r1} * {r2}")
            else:
                print("Algum registrador inválido.")

        elif opcao == "4":
            r1 = input("Registrador 1 (dividendo): ").strip()
            r2 = input("Registrador 2 (divisor): ").strip()
            destino = input("Registrador destino: ").strip()
            if r1 in registradores and r2 in registradores and destino in registradores:
                macro_div_monolitico(r1, r2, destino, registradores)
                print(f"{destino} = {r1} // {r2}")
            else:
                print("Algum registrador inválido.")

        elif opcao == "5":
            print("Registradores:", registradores)

        else:
            print("Opção inválida. Tente novamente.")

# ------------------------------
# Programa principal
# ------------------------------
def main():
    print("=== Simulador Máquina Norma Interativo ===\n")
    registradores = inicializar_registradores()
    executar_interativamente(registradores)
    print("\n=== Fim da Execução ===")
    print("Estado final dos registradores:", registradores)

if __name__ == "__main__":
    main()
