import numpy as np

def pertinencia_triangulo(x, a, b, c):
    """
    Função de pertinência triangular.
    """
    if x <= a or x >= c:
        return 0
    elif a < x < b:
        return (x - a) / (b - a)
    elif b <= x < c:
        return (c - x) / (c - b)
    return 0

# Funções de pertinência para comida
def comida_ruim(x):
    return pertinencia_triangulo(x, 0, 0, 5)

def comida_media(x):
    return pertinencia_triangulo(x, 0, 5, 10)

def comida_boa(x):
    return pertinencia_triangulo(x, 5, 10, 10)

# Funções de pertinência para serviço
def servico_ruim(x):
    return pertinencia_triangulo(x, 0, 0, 5)

def servico_medio(x):
    return pertinencia_triangulo(x, 0, 5, 10)

def servico_bom(x):
    return pertinencia_triangulo(x, 5, 10, 10)

def calcular_gorjeta_nebulosa(nota_comida, nota_servico):
    # Mapear as notas para os valores de pertinência
    comida_ruim_val = comida_ruim(nota_comida)
    comida_media_val = comida_media(nota_comida)
    comida_boa_val = comida_boa(nota_comida)
    
    servico_ruim_val = servico_ruim(nota_servico)
    servico_medio_val = servico_medio(nota_servico)
    servico_bom_val = servico_bom(nota_servico)
    
    # Aplicar as regras da lógica nebulosa
    gorjeta_pequena = min(comida_ruim_val, servico_ruim_val)  # Gorjeta pequena
    gorjeta_media = min(comida_media_val, servico_medio_val)  # Gorjeta média
    gorjeta_grande = min(comida_boa_val, servico_bom_val)     # Gorjeta grande
    
    # Combinação dos resultados
    gorjeta_ativada = (gorjeta_pequena * 5) + (gorjeta_media * 10) + (gorjeta_grande * 15)
    soma_ativacao = gorjeta_pequena + gorjeta_media + gorjeta_grande
    
    # Evitar divisão por zero
    if soma_ativacao == 0:
        return 0
    
    # Cálculo final da gorjeta
    gorjeta = gorjeta_ativada / soma_ativacao
    return gorjeta

# Solicitar notas do usuário
while True:
    nota_comida = int(input("Digite a nota para a comida (0 a 10): "))
    nota_servico = int(input("Digite a nota para o serviço (0 a 10): "))

    # Calcular a gorjeta usando lógica nebulosa
    gorjeta = calcular_gorjeta_nebulosa(nota_comida, nota_servico)

    # Exibir a gorjeta sugerida
    print(f"A gorjeta sugerida é: {gorjeta:.2f}")
