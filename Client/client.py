# saved as client.py
#Pyro4
#python.exe -m pip install Pyro4
# .\.venv\Scripts\python.exe -m pip install Pyro4
import Pyro4

#Usando os metodos da interface do objeto distribuido
aluno = Pyro4.Proxy("PYRONAME:aluno.ufc.kerb"+"@192.168.31.253:9090")
print(aluno.getDisciplina())