# Simulador da Máquina Norma

## Descrição
Este projeto implementa um **simulador da Máquina Norma**, com o objetivo de estudar máquinas universais, computação e execução de programas passo a passo.  

O simulador permite:
- Criar registradores personalizados pelo usuário.
- Inicializar os registradores com valores definidos.
- Executar programas monolíticos com instruções rotuladas.
- Utilizar **macros** para comparar valores entre registradores (`IGUAL`, `MAIOR`, `MENOR`).
- Acompanhar a execução linha a linha e o estado final dos registradores.

---

## Funcionalidades

1. **Registradores Dinâmicos**  
   - O usuário define a quantidade de registradores, seus nomes e valores iniciais.

2. **Instruções suportadas**  
   - `se zero_X então vá_para <linha1> senão vá_para <linha2>`: verifica se o registrador X é zero e altera o fluxo de execução.  
   - `faça add_X vá_para <linha>`: incrementa o registrador X em 1 e continua para a linha especificada.  
   - `faça sub_X vá_para <linha>`: decrementa o registrador X em 1 (não permitindo valores negativos) e continua para a linha especificada.  
   - `fim`: finaliza a execução do programa.  

3. **Macros Implementadas**  
   - `macro_igual(reg1, reg2)`: verifica se dois registradores são iguais.  
   - `macro_maior(reg1, reg2)`: verifica se o primeiro registrador é maior que o segundo.  
   - `macro_menor(reg1, reg2)`: verifica se o primeiro registrador é menor que o segundo.  
   - **Observação**: todas as macros preservam os valores originais dos registradores após a execução.

4. **Entrada**  
   - Um arquivo de texto (`programa.txt`) contendo as instruções rotuladas.

---

## Exemplo de programa (`programa.txt`)

```text
1: se zero_a então vá_para 5 senão vá_para 2
2: se zero_b então vá_para 5 senão vá_para 3
3: faça sub_a vá_para 4
4: faça sub_b vá_para 1
5: fim
