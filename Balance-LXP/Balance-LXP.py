import os
from web3 import Web3
import json
from colorama import Fore, Style

# Определяем путь к текущей директории
current_directory = os.path.dirname(os.path.abspath(__file__))

# Инициализация Web3
web3 = Web3(Web3.HTTPProvider('https://linea.decubate.com'))

# Загрузка ABI из файла
abi_file_path = os.path.join(current_directory, 'contract_abi.json')
with open(abi_file_path, 'r') as file:
    contract_abi = json.load(file)

# Адрес контракта
contract_address = '0xd83af4fbd77f3ab65c3b1dc4b38d7e67aecf599a'

# Загрузка адресов кошельков из файла
wallet_addresses = []
wallets_file_path = os.path.join(current_directory, 'wallets.txt')
with open(wallets_file_path, 'r') as wallet_file:
    for line in wallet_file:
        wallet_addresses.append(line.strip())

contract_address = web3.to_checksum_address('0xd83af4fbd77f3ab65c3b1dc4b38d7e67aecf599a')


# Создание объекта контракта
contract = web3.eth.contract(address=contract_address, abi=contract_abi)

total_balance = 0

# Получение баланса для каждого кошелька
for index, wallet_address in enumerate(wallet_addresses, start=1):
    # Получение баланса
    balance = contract.functions.balanceOf(wallet_address).call()
    balance_eth = round(web3.from_wei(balance, 'ether'))
    total_balance += balance_eth
    
    # Вывод баланса в эфирах с суффиксом "LXP"
    print(f'{Fore.GREEN}Кошелёк {index}: {wallet_address}')
    print(f'Баланс: {balance_eth} LXP{Style.RESET_ALL}')
    print('-' * 20)

# Вывод итоговой суммы баланса со всех кошельков
print('-' * 20)
print(f'{Fore.YELLOW}Итоговая сумма баланса со всех кошельков: {total_balance} LXP{Style.RESET_ALL}')
