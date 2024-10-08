# saved as Server.py
# Python Remote Objects (Pyro)
import Pyro4
import os

@Pyro4.expose
class Aluno(object): # Implementacao
    def getDisciplina(self):
        return "Sistemas Distribuidos!"
    
daemon = Pyro4.Daemon(host="192.168.31.253")         # Faz um Pyro daemon
uri2 = daemon.register(Aluno) # Registrar o como um objeto Pyro
ns = Pyro4.locateNS()           # Encontra o nome do server
print(uri2)
ns.register("aluno.ufc.kerb", uri2)    # Registrar o objeto com um nome no servidor de nome
print("Oi. Aluno esta ativo.")
daemon.requestLoop()                 # start the event loop of the server to wait for calls