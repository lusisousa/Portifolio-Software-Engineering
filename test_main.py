#Importa o framework de testes pytest
import pytest

#Importa a função que será testada
from main import mostrar_tarefas, filtrar_tarefas_por_status

#Testa o comportamento das funções
def test_mostrar_tarefas_vazio(capfd):
    mostrar_tarefas([])
    out, err = capfd.readouterr()
    assert "Nenhuma tarefa cadastrada." in out


def test_mostrar_tarefas_com_dados(capfd):
    tarefas = [{"descricao": "Estudar", "status": "pendente"}]
    mostrar_tarefas(tarefas)
    out, err = capfd.readouterr()
    assert "1. Estudar [pendente]" in out


def test_filtrar_tarefas_por_status_encontrado(monkeypatch, capfd):
    tarefas = [
        {"descricao": "Estudar", "status": "pendente"},
        {"descricao": "Academia", "status": "concluída"},
    ]
    #Simula o input com monkeypatch
    monkeypatch.setattr("builtins.input", lambda _: "pendente")
    filtrar_tarefas_por_status(tarefas)
    out, _ = capfd.readouterr()
    assert "1. Estudar" in out


def test_filtrar_tarefas_por_status_nao_encontrado(monkeypatch, capfd):
    tarefas = [
        {"descricao": "Estudar", "status": "pendente"},
    ]
    monkeypatch.setattr("builtins.input", lambda _: "em andamento")
    filtrar_tarefas_por_status(tarefas)
    out, _ = capfd.readouterr()
    assert "Nenhuma tarefa com status" in out
