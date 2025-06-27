import json
from datetime import datetime

ARQUIVO =   "eventos.json"

def carregar_eventos():
    """Função para ler e carregar eventos armazenados em um arquivo JSON"""
    try:
        with open(ARQUIVO, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def salvar_eventos(eventos):
    """Função para salvar os eventos em disco"""
    with open(ARQUIVO, "w") as f:
        json.dump(eventos, f, indent=4)

def cadastrar_evento():
    """Função para cadastrar eventos"""
    nome = input('Nome do evento: ')
    data = input('Data (YYY-MM-DD): ')
    hora = input('Hora (HH:MM): ')
    tipo = input('Tipo (prova, lembrete, trabalho): ')

    # Validar data e hora
    try:
        datetime.strptime(data, "%Y-%m-%d")
        datetime.strptime(hora, "%H:%M") 
    except ValueError:
        print('Data ou hora inválida!')
        return None

    return{
        "nome": nome,
        "data": data,
        "hora": hora,
        "tipo": tipo,
    }      

def listar_eventos(eventos):
    """Função para exibir todos os eventos cadastrados"""
    if not eventos:
        print('Nenhum evento cadastrado.')
        return
    print('\nEventos cadastrados:')
    for i, e in enumerate(eventos):
        print(f"{i+1}. {e['nome']} - {e['data']} {e['hora']} - {e['tipo']}")


def main():
    eventos = carregar_eventos()

    while True:
        print("\n1. Cadastrar evento.")
        print("2. Listar eventos")
        print("3. Sair")
        escolha = input('Escolha uma opção: ')

        if escolha == 1:
             evento = cadastrar_evento()
             if evento:
                 eventos.append(evento)
                 salvar_eventos(eventos)
                 print("Evento cadastrado com sucesso!")
        elif escolha == 2:
            listar_eventos(eventos)
        elif escolha == 3:
            print('Saindo...')
            break
        else:
            print('Opção invalida, tente novamente.')


if __name__ == "__main__":
    main()