# Módulo de conexão entre a classe e o banco de dados


# Imports
from applicationseven.database.run_sql import run_sql
from applicationseven.classes.instrutor import Instrutor
from applicationseven.classes.atividade import Atividade

"""Cada atividade está ligada a um instrutor"""


# Função para listar todos os instrutores
def get_all():

    instrutores = []

    sql = "SELECT * FROM webuser.TB_INSTRUTORES"
    results = run_sql(sql)

    for row in results:

        instrutor = Instrutor(row["nome"],
                              row["sobrenome"],
                              row["data_nascimento"],
                              row["endereco"],
                              row["telefone"],
                              row["id"])

        instrutores.append(instrutor)

    return instrutores


# Função para retornar um instrutor
def get_one(id):
    
    sql = "SELECT * FROM webuser.TB_INSTRUTORES WHERE id = %s"
    value = [id]
    
    result = run_sql(sql, value)[0]

    if result is not None:
        instrutor = Instrutor(row["nome"],
                              row["sobrenome"],
                              row["data_nascimento"],
                              row["endereco"],
                              row["telefone"],
                              row["id"])
    return instrutor


# Função para listar todas as atividades de um instrutor
def get_activities(instructor_id):
    
    atividades = []

    sql = "SELECT * FROM webuser.TB_ATIVIDADES WHERE instrutor = %s"
    value = [instructor_id]

    results = run_sql(sql, value)

    for row in results:
        atividade = Atividade(row["nome"],
                              row["instrutor"],
                              row["data"],
                              row["ducacao"],
                              row["capacidade"],
                              row["tipo_plano"],
                              row["ativo"],
                              row["id"])

        atividades.append(atividade)

    return atividades


# Função para cadastrar um instrutor
def new(instrutor):
    
    sql = "INSERT INTO webuser.TB_INSTRUTORES( nome, sobrenome, data_nascimento, endereco, telefone ) VALUES ( %s, %s, %s, %s, %s ) RETURNING *;"
    values = [instrutor.nome, instrutor.sobrenome, instrutor.data_nascimento, instrutor.endereco, instrutor.telefone]
    
    results = run_sql(sql, values)
    
    instrutor.id = results[0]["id"]
    
    return instrutor


# Função para deletar um instrutor
def delete_one(id):
    
    sql = "DELETE FROM webuser.TB_INSTRUTORES WHERE id = %s"
    value = [id]
    
    run_sql(sql, value)


# Função para editar um instrutor
def edit(instrutor):
    
    sql = "UPDATE webuser.TB_INSTRUTORES SET ( nome, sobrenome, data_nascimento, endereco, telefone ) = (%s, %s, %s, %s, %s) WHERE id = %s;"
    values = [instrutor.nome, instrutor.sobrenome, instrutor.data_nascimento, instrutor.endereco, instrutor.telefone, instrutor.id]
    
    run_sql(sql, values)



