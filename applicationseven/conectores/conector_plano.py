# Módulo de conexão entre a classe e o banco de dados


# Imports
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

#   No módulo plano importamos a classe TipoPlano
from applicationseven.classes.plano import TipoPlano

#   No módulo database, no módulo run_sql - importamos a função run_sql
from applicationseven.database.run_sql import run_sql


# Função para obter todos os planos
def get_all():

    tipos_planos = []

    # retornando todos os dados em TB_PLANOS
    sql = "SELECT * FROM webuser.TB_PLANOS"
    results = run_sql(sql)

    # para cada linha em resultados
    for row in results:
        # tipo_plano recebe a linha plano e a liinha id
        tipo_plano = TipoPlano(row["plano"], row["id"])
        # adiciona em tipos_planos
        tipos_planos.append(tipo_plano)
    # retorna tipos_planos
    return tipos_planos


# Função para obter um plano
def get_one(id):
    
    sql = "SELECT * FROM webuser.TB_PLANOS WHERE id = %s"
    value = [id]
    
    result = run_sql(sql, value)[0]

    if result is not None:
        tipo_plano = TipoPlano(result["plano"], result["id"])

    return tipo_plano


# Função para cria um tipo de plano
def new(tipo_plano):
    
    sql = "INSERT INTO webuser.TB_PLANOS ( plano ) VALUES ( %s ) RETURNING *;"
    values = [tipo_plano.plano]
    
    results = run_sql(sql, values)
    
    tipo_plano.id = results[0]["id"]

    return tipo_plano


# Função para deletar um plano
def delete_one(id):
    
    sql = "DELETE FROM webuser.TB_PLANOS WHERE id = %s"
    value = [id]
    
    run_sql(sql, value)


# Função para alterar um plano
def edit(tipo_plano):
    
    sql = "UPDATE webuser.TB_PLANOS SET (plano) = (%s) WHERE id = %s;"
    values = [tipo_plano.plano, tipo_plano.id]

    run_sql(sql, values)


