import datetime

veiculos_estacionados = {}
historico_saidas = []

def calcular_valor(tempo_permanencia_minutos):
    return round((tempo_permanencia_minutos / 60) * 10, 2)


def registrar_entrada():
    print("\n--- Sistema de Entrada ---")
    placa = input("Digite a placa do veículo: ").upper()
    tem_tag = input("O veículo possui TAG de acesso? (S/N): ").upper() == 'S'
    
    if tem_tag:
        print("TAG detectada. Acesso liberado automaticamente.")
        tipo_acesso = "TAG"
    else:
        print("Pressione o botão para emitir o ticket...")
        input("[Pressione Enter]")
        print("Ticket emitido. Acesso liberado.")
        tipo_acesso = "Ticket"

    veiculos_estacionados[placa] = {
        "entrada": datetime.datetime.now(),
        "tipo": tipo_acesso
    }

def registrar_saida():
    print("\n--- Sistema de Saída ---")
    placa = input("Digite a placa para saída: ").upper()
    
    if placa not in veiculos_estacionados:
        print("Erro: Placa não encontrada no sistema!")
        return

    dados = veiculos_estacionados.pop(placa)
    hora_saida = datetime.datetime.now()
    duracao = hora_saida - dados["entrada"]
    minutos = duracao.total_seconds() / 60
    valor = calcular_valor(minutos)

    print(f"Tempo de permanência: {int(minutos)} minutos.")
    
    if dados["tipo"] == "TAG":
        print(f"Valor de R$ {valor} será gerado na fatura da sua TAG.")
    else:
        print(f"Valor a pagar: R$ {valor}")
        input("Pague o ticket e insira na máquina de saída... [Enter]")
        print("Obrigado, volte sempre!")

    historico_saidas.append({"placa": placa, "valor": valor, "permanencia": minutos})

def gerar_relatorio():
    print("\n--- Relatório Diário ---")
    total_faturado = sum(item['valor'] for item in historico_saidas)
    print(f"Total de veículos que saíram: {len(historico_saidas)}")
    print(f"Faturamento total: R$ {total_faturado}")
    print(f"Veículos ainda no pátio: {list(veiculos_estacionados.keys())}")

try:
    registrar_entrada() 
    registrar_saida()  
    gerar_relatorio()
except Exception as e:
    print(f"Ocorreu um erro inesperado no sistema: {e}")
