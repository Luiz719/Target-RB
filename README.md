
# Desafio de Programação

Este repositório contém soluções para as questões apresentadas em um processo seletivo de programação.

## Questões

### 1. Verificação de número na sequência de Fibonacci

**Enunciado**:  
Escreva um programa que calcule a sequência de Fibonacci e retorne se um número informado pertence ou não à sequência.

[Ver código da questão 1](questão1.py)

---

### 2. Verificar ocorrência de letra 'a'

**Enunciado**:  
Escreva um programa que verifique, em uma string, a existência da letra ‘a’, seja maiúscula ou minúscula, além de informar a quantidade de vezes em que ela ocorre.

[Ver código da questão 2](questão2.py)

---


### 3. Qual será o valor da variável `SOMA` ao final do processamento?

**Enunciado**:  
Dado o seguinte trecho de código:
```c
int INDICE = 12, SOMA = 0, K = 1;
Enquanto K < INDICE faça { 
    K = K + 1; 
    SOMA = SOMA + K; 
}
Imprimir(SOMA);
```
Qual será o valor de `SOMA` ao final?

**Resposta**:  
Dado que:
```
SOMA = 2 + 3 + 4 + ... + 12 
```
Pela Soma dos 12 termos da PA, tem-se que:
$$ SOMA =  \frac{(2+12) \cdot 11}{2} = 77 $$ 
Logo, o valor final de `SOMA` será **77**.

A versão em código também pode ser encontrada em: [Código da questão 3](questão3.py)

---

### 4. Complete o próximo elemento nas sequências

**Enunciado**:  
Complete o próximo elemento nas seguintes sequências:

**a) 1, 3, 5, 7, ___**

- **Lógica**: Sequência de números ímpares.
- **Próximo elemento**: 9

---

**b) 2, 4, 8, 16, 32, 64, ____**

- **Lógica**: Cada número é o dobro do anterior (potências de 2).
- **Próximo elemento**: 128

---

**c) 0, 1, 4, 9, 16, 25, 36, ____**

- **Lógica**: Sequência de quadrados perfeitos (0², 1², 2², 3²...).
- **Próximo elemento**: 49 (7²)

---

**d) 4, 16, 36, 64, ____**

- **Lógica**: Sequência de quadrados perfeitos de números pares (2², 4², 6²...).
- **Próximo elemento**: 100 (10²)

---

**e) 1, 1, 2, 3, 5, 8, ____**

- **Lógica**: Sequência de Fibonacci (soma dos dois números anteriores).
- **Próximo elemento**: 13

---

**f) 2, 10, 12, 16, 17, 18, 19, ____**

- **Lógica**: Todos os números da sequência começam com a letra "D" quando escritos por extenso em português.
- **Próximo elemento**: 200 (duzentos)

---


### 5. Interruptores e lâmpadas

**Enunciado**:  
Você está em uma sala com três interruptores, cada um conectado a uma lâmpada em salas diferentes. Você não pode ver as lâmpadas da sala em que está, mas pode ligar e desligar os interruptores quantas vezes quiser. Seu objetivo é descobrir qual interruptor controla qual lâmpada. Como você faria para descobrir, usando apenas duas idas até uma das salas das lâmpadas, qual interruptor controla cada lâmpada?  

**Resposta**:  

1. Ligaria o primeiro interruptor e o deixaria ligado por alguns minutos.
2. Desligaria o primeiro interruptor e ligaria o segundo.
3. Iria imediatamente para uma das salas:
   - Se a lâmpada estiver acesa, o segundo interruptor controla esta lâmpada.
   - Se a lâmpada estiver apagada, mas quente, o primeiro interruptor controla esta lâmpada.
   - Se a lâmpada estiver apagada e fria, o terceiro interruptor controla esta lâmpada.
4. Agora iria para uma outra sala:
   - De forma análoga à anterior e baseado no que foi observado na primeira sala, pode-se determinar qual interruptor controla a lâmpada desta sala.
5. Por eliminação, torna-se claro qual interruptor controla a lâmpada da sala restante.

Com isso, é possível descobrir qual interruptor controla cada lâmpada duas idas até uma das salas das lâmpadas.

---

## Tecnologias Utilizadas

- **Linguagem**: Python
