import datetime
print("gerenciamento de cancelas para um shopping")
VALOR_ENTRADA = float(input("Digite o valor base de entrada (R$): "))
VALOR_HORA = float(input("Digite o valor da hora adicional (R$): "))

veiculos_no_patio = {} 

def sinalizar(mensagem):
    """Simula a sinalização de entrada/saída (Irradiador de Informação) [Turno 1]"""
    print(f"\n[SINALIZAÇÃO]: {mensagem}")

def registrar_entrada():
    """Implementa o Passo 1: Elicitação de informações e estímulos [Turno 19]"""
    sinalizar("Veículo detectado na cancela de ENTRADA.")
    
    try:
        placa = input("Informe a placa do veículo: ").upper()
        tem_tag = input("Possui TAG de acesso livre? (S/N): ").upper() == 'S'
        
        if tem_tag:
            sinalizar(f"TAG Identificada. Acesso LIBERADO para placa {placa}.")
            veiculos_no_patio[placa] = {"entrada": datetime.datetime.now(), "tipo": "TAG"}
        else:
            print("Pressione o botão para emitir o ticket...")
            input("[BOTÃO PRESSIONADO]")
            sinalizar(f"Ticket emitido. Acesso LIBERADO para placa {placa}.")
            veiculos_no_patio[placa] = {"entrada": datetime.datetime.now(), "tipo": "TICKET"}
            
    except Exception as e:

        print(f"ERRO AO PROCESSAR ENTRADA: {e}. Por favor, acione o suporte.")

def registrar_saida():
    """Implementa os Passos 2 e 3: Processamento de Transação e Saída [1242, Turno 19]"""
    sinalizar("Veículo detectado na cancela de SAÍDA.")
    placa = input("Informe a placa para saída: ").upper()
    
    if placa in veiculos_no_patio:
        dados = veiculos_no_patio.pop(placa)
        hora_entrada = dados["entrada"]
        hora_saida = datetime.datetime.now()
    
        permanencia = (hora_saida - hora_entrada).total_seconds() / 3600 + 2 
        
        valor_total = VALOR_ENTRADA + (int(permanencia) * VALOR_HORA)
        
        print(f"Tempo de permanência: {permanencia:.2f} horas.")
        
        if dados["tipo"] == "TAG":
            sinalizar(f"Saída via TAG. Valor de R${valor_total:.2f} gerado na fatura.")
        else:
            print(f"Valor a pagar: R${valor_total:.2f}")
            input("Aguardando pagamento... [PAGO]")
            print("Recolha o ticket na saída.")
            
        sinalizar("Cancela aberta. Boa viagem!")
    else:
    
        print("ALERTA: Placa não registrada. Verifique com a administração.")

while True:
    print("\n1- Entrada | 2- Saída | 3- Relatório (Sair)")
    opcao = input("Escolha a operação: ")
    
    if opcao == '1':
        registrar_entrada()
    elif opcao == '2':
        registrar_saida()
    elif opcao == '3':
        print(f"Encerrando... Veículos ainda no pátio: {len(veiculos_no_patio)}")
        break
