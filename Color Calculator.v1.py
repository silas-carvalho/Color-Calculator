def realizar_soma(valor1, valor2):
    return valor1 + valor2

def realizar_subtracao(valor1, valor2):
    return valor1 - valor2

def realizar_multiplicacao(valor1, valor2):
    return valor1 * valor2

def realizar_divisao(valor1, valor2):
    return valor1 / valor2 if valor2 != 0 else "Erro: Divisão por zero não é permitida."

def exibir_menu():
    from colorama import Fore, Style

    print(Fore.CYAN + "\nEscolha a operação que deseja realizar:\n" + Style.RESET_ALL)
    print(Fore.YELLOW + "1 - Soma" + Style.RESET_ALL)
    print(Fore.YELLOW + "2 - Subtração" + Style.RESET_ALL)
    print(Fore.YELLOW + "3 - Multiplicação" + Style.RESET_ALL)
    print(Fore.YELLOW + "4 - Divisão" + Style.RESET_ALL)

def main():
    from colorama import Fore, Style

    while True:
        exibir_menu()
        escolha = input(Fore.GREEN + "\nDigite o número correspondente à operação (ou 'sair' para encerrar): " + Style.RESET_ALL)

        if escolha.lower() == 'sair':
            print(Fore.BLUE + "\nCalculadora encerrada. Até logo!" + Style.RESET_ALL)
            break

        if escolha not in ['1', '2', '3', '4']:
            print(Fore.RED + "\nOpção inválida! Tente novamente." + Style.RESET_ALL)
            continue

        try:
            numero1 = float(input(Fore.GREEN + "\nDigite o primeiro número: " + Style.RESET_ALL))
            numero2 = float(input(Fore.GREEN + "Digite o segundo número: " + Style.RESET_ALL))
        except ValueError:
            print(Fore.RED + "\nErro: Apenas números são permitidos. Tente novamente." + Style.RESET_ALL)
            continue

        if escolha == '1':
            print(Fore.MAGENTA + f"\nResultado: {numero1} + {numero2} = {realizar_soma(numero1, numero2)}" + Style.RESET_ALL)
        elif escolha == '2':
            print(Fore.MAGENTA + f"\nResultado: {numero1} - {numero2} = {realizar_subtracao(numero1, numero2)}" + Style.RESET_ALL)
        elif escolha == '3':
            print(Fore.MAGENTA + f"\nResultado: {numero1} * {numero2} = {realizar_multiplicacao(numero1, numero2)}" + Style.RESET_ALL)
        elif escolha == '4':
            resultado = realizar_divisao(numero1, numero2)
            print(Fore.MAGENTA + (f"\nResultado: {resultado}" if isinstance(resultado, str) else f"\nResultado: {numero1} / {numero2} = {resultado}") + Style.RESET_ALL)

if __name__ == "__main__":
    from colorama import init
    init(autoreset=True)
    main()