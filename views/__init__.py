import sys,os #lida com o sistema operacional
# print(sys.path) onde o python procura arquivo pra ser importado
sys.path.append(os.path.abspath(os.curdir)) #adicione a raiz do projeto (os.curdir) e adicione isso dentro de sys.path