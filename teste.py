from models.cliente import Cliente
from models.conta import Conta


hideki: Cliente = Cliente('Alexandre Hideki', 'hidekialexandre@gmail.com', '123.456.789-98', '13/05/2002')
adriana: Cliente = Cliente('Adriana Lins', 'adrianalins@gmail.com', '234.567.891-89', '05/03/1989')

# print(hideki)
# print(adriana)

contaa: Conta = Conta(adriana)
contah: Conta = Conta(hideki)

# print(contaa)
# print(contah)

