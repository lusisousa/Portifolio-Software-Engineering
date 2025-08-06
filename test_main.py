#Importa o framework de testes pytest
import pytest

#Importa a função que será testada
from main import mostrar_tarefas

#Testa o comportamento da função mostrar_tarefas quando a lista está vazia
def test_mostrar_tarefas_vazio(capfd):
    mostrar_tarefas([])
    out, err = capfd.readouterr()
    assert "Nenhuma tarefa cadastrada." in out
