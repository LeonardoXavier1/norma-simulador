# ==============================
# Simulador de Máquina Norma
# ==============================

import sys

# ------------------------------
# Funções para macros
# ------------------------------
def macro_multiplicacao(registradores, r1, r2, destino):
    registradores[destino] = registradores[r1] * registradores[r2]

def macro_divisao(registradores, r1, r2, destino):
    if registradores[r2] == 0:
        print("Erro: divisão por zero")
        registradores[destino] = 0
    else:
        registradores[destino] = registradores[r1] // registradores[r2]

def macro_primo(registradores, r, destino):
    n = registradores[r]
    if n < 2:
        registradores[destino] = 0
        return
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            registradores[destino] = 0
            return
    registradores[destino] = 1

# ------------------------------
# Função para carregar programa
# ------------------------------
def carregar_programa(nome_arquivo):
    programa = {}
    try:
        with open(nome_arquivo, "r") as f:
            for linha in f:
                linha = linha.strip()
                if not linha:
                    continue
                if ":" not in linha:
                    continue
                rotulo, instrucao = linha.split(":", 1)
                programa[int(rotulo.strip())] = instrucao.strip()
        return programa
    except FileNotFoundError:
        print("Arquivo não encontrado.")
        sys.exit(1)

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
# Função principal do simulador
# ------------------------------
def executar_programa(programa, registradores):
    linha_atual = 1
    print("\n=== Início da Computação ===\n")
    while linha_atual in programa:
        instrucao = programa[linha_atual]
        print(f"Linha {linha_atual}: {instrucao}")
        print(f"Registradores: {registradores}")

        if instrucao.startswith("se zero_"):
            # Teste zero_x
            partes = instrucao.split()
            reg = partes[1].split("_")[1]
            rotulo_verdadeiro = int(partes[4])
            rotulo_falso = int(partes[-1])
            if registradores.get(reg, 0) == 0:
                linha_atual = rotulo_verdadeiro
            else:
                linha_atual = rotulo_falso

        elif instrucao.startswith("faça add_"):
            reg = instrucao.split()[1].split("_")[1]
            registradores[reg] += 1
            linha_atual = int(instrucao.split()[-1])

        elif instrucao.startswith("faça sub_"):
            reg = instrucao.split()[1].split("_")[1]
            registradores[reg] -= 1
            linha_atual = int(instrucao.split()[-1])

        elif instrucao.startswith("macro_mul"):
            _, r1, r2, destino = instrucao.split()
            macro_multiplicacao(registradores, r1, r2, destino)
            linha_atual += 1

        elif instrucao.startswith("macro_div"):
            _, r1, r2, destino = instrucao.split()
            macro_divisao(registradores, r1, r2, destino)
            linha_atual += 1

        elif instrucao.startswith("macro_primo"):
            _, r, destino = instrucao.split()
            macro_primo(registradores, r, destino)
            linha_atual += 1

        else:
            print("Instrução inválida:", instrucao)
            break

    print("\n=== Fim da Computação ===\n")
    print("Estado final dos registradores:", registradores)

# ------------------------------
# Programa principal
# ------------------------------
def main():
    print("=== Simulador Máquina Norma ===\n")
    registradores = inicializar_registradores()
    arquivo = input("Informe o nome do arquivo do programa: ")
    programa = carregar_programa(arquivo)
    executar_programa(programa, registradores)

if __name__ == "__main__":
    main()
