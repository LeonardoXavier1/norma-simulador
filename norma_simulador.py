import re
import os
import copy

class SimuladorNorma:
    def __init__(self):
        self.registradores = {}
        self.pc = 1
        self.programa = {}
        self.log_execucao = []
        self.carregar_programa()

    def carregar_programa(self, arquivo="programa.txt"):
        """Carrega programa monolítico fixo"""
        if not os.path.exists(arquivo):
            print(f"Arquivo {arquivo} não encontrado! Crie um programa.txt válido.")
            return False

        self.programa = {}
        with open(arquivo, "r", encoding="utf-8") as f:
            for linha in f:
                linha = linha.strip()
                if not linha or linha.startswith('#'):
                    continue
                if ':' in linha:
                    rotulo, instrucao = linha.split(":", 1)
                    self.programa[int(rotulo.strip())] = instrucao.strip()
        print(f"Programa carregado com {len(self.programa)} instruções")
        return True

    def configurar_registradores(self):
        """Permite ao usuário configurar quantidade e valores dos registradores"""
        print("\n=== CONFIGURAÇÃO DOS REGISTRADORES ===")
        while True:
            try:
                qtd = int(input("Quantos registradores deseja usar? (mínimo 2): "))
                if qtd >= 2:
                    break
                print("Mínimo de 2 registradores necessários!")
            except ValueError:
                print("Digite um número válido!")

        nomes = []
        for i in range(qtd):
            nome = input(f"Nome do registrador {i+1} (ex: a, b, c): ").strip().lower()
            while not nome or nome in nomes:
                if not nome:
                    nome = input("Nome não pode ser vazio: ").strip().lower()
                else:
                    nome = input("Nome já usado, escolha outro: ").strip().lower()
            nomes.append(nome)

        self.registradores = {}
        for nome in nomes:
            while True:
                try:
                    valor = int(input(f"Valor inicial para registrador '{nome}': "))
                    self.registradores[nome] = valor
                    break
                except ValueError:
                    print("Digite um número inteiro válido!")

        print(f"\nRegistradores configurados: {self.registradores}")
        return True

    def executar_instrucao(self, instrucao):
        """Executa uma única instrução e retorna próximo PC"""
        self.log_execucao.append(f"[PC={self.pc}] {instrucao} | Registradores: {self.registradores}")
        print(f"[PC={self.pc}] {instrucao} | Registradores: {self.registradores}")

        if instrucao.strip() == "fim":
            return -1 

        # Teste de zero
        if instrucao.startswith("se zero_"):
            match = re.match(r'se zero_(\w+) então vá_para (\d+) senão vá_para (\d+)', instrucao)
            if match:
                reg, dest_zero, dest_nao_zero = match.groups()
                if reg in self.registradores:
                    if self.registradores[reg] == 0:
                        return int(dest_zero)
                    else:
                        return int(dest_nao_zero)

        # Operação add
        elif instrucao.startswith("faça add_"):
            match = re.match(r'faça add_(\w+) vá_para (\d+)', instrucao)
            if match:
                reg, destino = match.groups()
                if reg in self.registradores:
                    self.registradores[reg] += 1
                    return int(destino)

        # Operação sub
        elif instrucao.startswith("faça sub_"):
            match = re.match(r'faça sub_(\w+) vá_para (\d+)', instrucao)
            if match:
                reg, destino = match.groups()
                if reg in self.registradores:
                    if self.registradores[reg] > 0:
                        self.registradores[reg] -= 1
                    return int(destino)

        print(f"Instrução desconhecida: {instrucao}")
        return -1

    def executar_programa(self, programa=None):
        """Executa o programa monolítico completo"""
        if programa is None:
            programa = self.programa
        if not programa:
            print("Nenhum programa carregado!")
            return False

        print("\n=== EXECUÇÃO DO PROGRAMA ===")
        self.pc = 1
        self.log_execucao = []
        passos = 0

        while self.pc != -1 and passos < 1000:
            if self.pc not in programa:
                print(f"Erro: Instrução {self.pc} não encontrada!")
                break

            instrucao = programa[self.pc]
            proximo_pc = self.executar_instrucao(instrucao)
            if proximo_pc == -1:
                break

            self.pc = proximo_pc
            passos += 1

        if passos >= 1000:
            print("AVISO: Programa atingiu limite de passos (possível loop infinito)")

        print(f"\n=== RESULTADO FINAL ===")
        print(f"Registradores finais: {self.registradores}")
        print(f"Total de passos executados: {passos}")
        return True

    def macro_igual(self, reg1, reg2):
        """Macro para testar igualdade entre dois registradores"""
        print(f"\n=== MACRO IGUAL: {reg1} == {reg2}? ===")
        if reg1 not in self.registradores or reg2 not in self.registradores:
            print("Registradores não encontrados!")
            return False

        estado_original = copy.deepcopy(self.registradores)

        # Cria uma cópia do programa substituindo a->reg1 e b->reg2
        programa_temp = {}
        for k, instr in self.programa.items():
            instr_temp = instr.replace("a", reg1).replace("b", reg2)
            programa_temp[k] = instr_temp

        self.executar_programa(programa_temp)

        resultado = (self.registradores[reg1] == 0 and self.registradores[reg2] == 0)
        print(f"Resultado: {resultado}")

        self.registradores = estado_original
        return resultado

    def macro_maior(self, reg1, reg2):
        """Macro para testar se reg1 > reg2"""
        print(f"\n=== MACRO MAIOR: {reg1} > {reg2}? ===")
        if reg1 not in self.registradores or reg2 not in self.registradores:
            print("Registradores não encontrados!")
            return False

        estado_original = copy.deepcopy(self.registradores)
        a = self.registradores[reg1]
        b = self.registradores[reg2]

        while a > 0 and b > 0:
            a -= 1
            b -= 1

        resultado = (a > 0)
        print(f"Resultado: {resultado}")

        self.registradores = estado_original
        return resultado

    def macro_menor(self, reg1, reg2):
        """Macro para testar se reg1 < reg2"""
        print(f"\n=== MACRO MENOR: {reg1} < {reg2}? ===")
        if reg1 not in self.registradores or reg2 not in self.registradores:
            print("Registradores não encontrados!")
            return False

        estado_original = copy.deepcopy(self.registradores)
        a = self.registradores[reg1]
        b = self.registradores[reg2]

        while a > 0 and b > 0:
            a -= 1
            b -= 1

        resultado = (b > 0)
        print(f"Resultado: {resultado}")

        self.registradores = estado_original
        return resultado

    def menu_principal(self):
        """Menu interativo principal"""
        while True:
            print("\n" + "="*50)
            print("    SIMULADOR DA MÁQUINA NORMA")
            print("="*50)
            print("1. Configurar registradores")
            print("2. Executar programa")
            print("3. Testar macro IGUAL")
            print("4. Testar macro MAIOR")
            print("5. Testar macro MENOR")
            print("6. Mostrar estado atual")
            print("7. Sair")
            print("-"*50)

            try:
                opcao = int(input("Escolha uma opção: "))
            except ValueError:
                print("Opção inválida!")
                continue

            if opcao == 1:
                self.configurar_registradores()
            elif opcao == 2:
                if not self.registradores:
                    print("Configure os registradores primeiro!")
                    continue
                self.executar_programa()
            elif opcao in [3,4,5]:
                if not self.registradores:
                    print("Configure os registradores primeiro!")
                    continue
                regs = list(self.registradores.keys())
                if len(regs) >= 2:
                    print(f"Registradores disponíveis: {regs}")
                    reg1 = input("Primeiro registrador: ").strip()
                    reg2 = input("Segundo registrador: ").strip()
                    if reg1 in self.registradores and reg2 in self.registradores:
                        if opcao == 3:
                            self.macro_igual(reg1, reg2)
                        elif opcao == 4:
                            self.macro_maior(reg1, reg2)
                        elif opcao == 5:
                            self.macro_menor(reg1, reg2)
                    else:
                        print("Registradores inválidos!")
                else:
                    print("Precisa de pelo menos 2 registradores!")
            elif opcao == 6:
                print(f"\nEstado atual:")
                print(f"Registradores: {self.registradores}")
                print(f"PC: {self.pc}")
                print(f"Instruções carregadas: {len(self.programa)}")
            elif opcao == 7:
                print("Encerrando simulador...")
                break
            else:
                print("Opção inválida!")

def main():
    print("Bem-vindo ao Simulador da Máquina Norma!")
    simulador = SimuladorNorma()
    simulador.menu_principal()

if __name__ == "__main__":
    main()
