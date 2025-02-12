# Módulo de conexão entre a classe e o banco de dados


# Imports
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

import applicationseven.conectores.conector_plano as plano
from applicationseven.database.run_sql import run_sql
from applicationseven.classes.membro import Membro
from applicationseven.classes.atividade import Atividade


# Função para retonar a lista de todos os membros
def get_all():

    membros = []

    sql = "SELECT * FROM webuser.TB_MEMBROS ORDER BY nome ASC"
    results = run_sql(sql)

    for row in results:
        
        tipo_plano = plano.get_one(row["plano"])
        
        membro = Membro(row["nome"],
                        row["sobrenome"],
                        row["data_nascimento"],
                        row["endereco"],
                        row["telefone"],
                        row["email"],
                        tipo_plano,
                        row["data_inicio"],
                        row["ativo"],
                        row["id"])

        membros.append(member)

    return membros


# Função para obter um membro
def get_one(id):

    sql = "SELECT * FROM webuser.TB_MEMBROS WHERE id = %s"
    value = [id]
    
    result = run_sql(sql, value)[0]

    if result is not None:

        tipo_plano = plano.get_one(row["plano"])
        
        membro = Membro(row["nome"],
                        row["sobrenome"],
                        row["data_nascimento"],
                        row["endereco"],
                        row["telefone"],
                        row["email"],
                        tipo_plano,
                        row["data_inicio"],
                        row["ativo"],
                        row["id"])

    return membro

    
# Função para obter a lista de atividades de um membro
def get_activities(user_id):

    atividades = []

    sql = "SELECT atividades.* FROM webuser.TB_ATIVIDADES INNER JOIN webuser.TB_AGENDAMENTOS on webuser.TB_ATIVIDADES.id = webuser.TB_AGENDAMENTOS.atividade where webuser.TB_AGENDAMENTOS.membro = %s"
    value = [user_id]
    
    results = run_sql(sql, value)

    for row in results:
        
        tipo_plano = plano.get_one(row["plano"])
        
        atividade = Atividade(row["nome"],
                              row["instrutor"],
                              row["data"],
                              row["ducacao"],
                              row["capacidade"],
                              tipo_plano,
                              row["ativo"],
                              row["id"])

        atividades.append(atividade)

    return atividades


# Função para retornar todos os membros ativos
def get_all_active():

    membros = []

    sql = "SELECT * FROM webuser.TB_MEMBROS where ativo = true ORDER BY nome ASC"
    results = run_sql(sql)

    for row in results:
        
        tipo_plano = plano.get_one(row["plano"])
        
        membro = Membro(row["nome"],
                        row["sobrenome"],
                        row["data_nascimento"],
                        row["endereco"],
                        row["telefone"],
                        row["email"],
                        tipo_plano,
                        row["data_inicio"],
                        row["ativo"],
                        row["id"])

        membros.append(member)

    return membros


# Função para retornar todos os membros inativos
def get_all_inactive():

    membros = []

    sql = "SELECT * FROM webuser.TB_MEMBROS where ativo = false ORDER BY nome ASC"
    results = run_sql(sql)

    for row in results:
        
        tipo_plano = plano.get_one(row["plano"])
        
        membro = Membro(row["nome"],
                        row["sobrenome"],
                        row["data_nascimento"],
                        row["endereco"],
                        row["telefone"],
                        row["email"],
                        tipo_plano,
                        row["data_inicio"],
                        row["ativo"],
                        row["id"])

        membros.append(member)

    return membros


# Função para cadastrar um novo membro
def new(membro):
    
    sql = "INSERT INTO webuser.TB_MEMBROS( nome, sobrenome, data_nascimento, endereco, telefone, email, tipo_plano, data_inicio, ativo ) VALUES ( %s, %s, %s, %s, %s, %s, %s, %s, %s ) RETURNING *;"
    values = [membro.nome, membro.sobrenome, membro.data_nascimento, membro.endereco, membro.telefone, membro.email, membro.tipo_plano.id, membro.data_inicio, membro.ativo]
    
    results = run_sql(sql, values)
    
    membro.id = results[0]["id"]
    
    return membro


# Função para deletar um membro
def delete_one(id):
    sql = "DELETE  FROM webuser.TB_MEMBROS WHERE id = %s"
    value = [id]
    run_sql(sql, value)


# Função para atualizar um membro
def edit(membro):
    
    sql = "UPDATE webuser.TB_MEMBROS SET ( nome, sobrenome, data_nascimento, endereco, telefone, email, tipo_plano, data_inicio, ativo ) = (%s, %s, %s, %s, %s, %s, %s, %s, %s) WHERE id = %s;"
    values = [membro.nome, membro.sobrenome, membro.data_nascimento, membro.endereco, membro.telefone, membro.email, membro.tipo_plano.id, membro.data_inicio, membro.ativo, membro.id]

    run_sql(sql, values)

    
