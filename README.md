# Simulador da Máquina Norma

## Descrição
Este projeto implementa um simulador da Máquina Norma, com o objetivo de estudar máquinas universais, computação e execução de programas.  

O simulador permite:
- Criar registradores personalizados pelo usuário.
- Inicializar os registradores com valores definidos.
- Executar programas monolíticos com instruções rotuladas.
- Utilizar macros para operações matemáticas.
- Acompanhar a execução linha a linha e o estado final dos registradores.

---

## Funcionalidades
1. **Registradores Dinâmicos**: usuário define quantos registradores, nomes e valores iniciais.  
2. **Instruções suportadas**:
   - `zero_x`: verifica se o registrador x é zero.
   - `add_x`: incrementa o registrador x em 1.
   - `sub_x`: decrementa o registrador x em 1.
   - `vá_para <linha>`: muda o fluxo de execução.  
3. **Macros Implementadas**:
   - `macro_mul x y z`: multiplicação de dois números inteiros.
   - `macro_div x y z`: divisão de dois números inteiros (trata divisão por zero).
   - `macro_primo x y`: identifica se um número é primo.  
4. **Entrada**: arquivo de texto com o programa (`programa.txt`).  

Exemplo de programa (`programa.txt`):

```text
1: se zero_b então vá_para 5 senão vá_para 2
2: faça add_a vá_para 3
3: faça add_a vá_para 4
4: faça sub_b vá_para 1
5: macro_mul a b c
6: macro_div a b d
7: macro_primo a e


=== Início da Computação ===
Linha 1: se zero_b então vá_para 5 senão vá_para 2
Registradores: {'a': 0, 'b': 2, 'c': 0, 'd': 0, 'e': 0}
Linha 2: faça add_a vá_para 3
Registradores: {'a': 0, 'b': 2, 'c': 0, 'd': 0, 'e': 0}
Linha 3: faça add_a vá_para 4
Registradores: {'a': 1, 'b': 2, 'c': 0, 'd': 0, 'e': 0}
...
Linha 7: macro_primo a e
Registradores: {'a': 4, 'b': 0, 'c': 0, 'd': 0, 'e': 0}
=== Fim da Computação ===
Estado final dos registradores: {'a': 4, 'b': 0, 'c': 0, 'd': 0, 'e': 0}
