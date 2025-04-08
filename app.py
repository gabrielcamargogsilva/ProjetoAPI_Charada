from flask import Flask, jsonify, request
import random 
import firebase_admin
from firebase_admin import credentials, firestore
from flask_cors import CORS
import os
import json
from dotenv import load_dotenv

# Inicialização da aplicação Flask
app = Flask('__name__')
CORS(app)  # Habilita o CORS para permitir requisições de diferentes origens

load_dotenv()

#Pega a variável de ambiente e converte para JSON
FBKEY = json.loads(os.getenv('CONFIG_FIREBASE'))

# Carrega as credenciais do Firebase e inicializa a conexão com Firestore
cred = credentials.Certificate(FBKEY)
firebase_admin.initialize_app(cred)

db = firestore.client()  # Cliente Firestore para manipular o banco de dados

# ---- Rota principal de teste ----
@app.route('/', methods=['GET'])
def index():
    return 'CHARADAS API', 200  # Retorna uma mensagem indicando que a API está funcionando

# ---- Método GET - Retorna uma charada aleatória ----
@app.route('/charadas', methods=['GET'])
def charada_aleatoria():
    charadas = []  # Lista para armazenar as charadas recuperadas do Firestore
    lista = db.collection('charadas').stream()  # Obtém todos os documentos da coleção 'charadas'
    
    # Converte os documentos do Firestore em dicionários e adiciona à lista
    for item in lista:
        charadas.append(item.to_dict())
    
    # Retorna uma charada aleatória caso existam charadas cadastradas
    if charadas:
        return jsonify(random.choice(charadas)), 200
    else:
        return jsonify({'mensagem': 'Erro! Nenhuma charada encontrada'}), 404
    
# ---- Método GET - Listar Charadas ----
@app.route('/charadas/lista', methods=['GET'])
def charada_lista():
    charadas = []  # Lista para armazenar as charadas recuperadas do Firestore
    lista = db.collection('charadas').stream()  # Obtém todos os documentos da coleção 'charadas'
    
    # Converte os documentos do Firestore em dicionários e adiciona à lista
    for item in lista:
        charadas.append(item.to_dict())
    
    # Retorna uma charada aleatória caso existam charadas cadastradas
    if charadas:
        return jsonify(charadas), 200
    else:
        return jsonify({'mensagem': 'Erro! Nenhuma charada encontrada'}), 404
    
    

# ---- Método GET - Busca uma charada específica por ID ----
@app.route('/charadas/<id>', methods=['GET'])
def busca(id):
    doc_ref = db.collection('charadas').document(id)
    doc = doc_ref.get().to_dict()
    
    # Verifica se o documento existe no Firestore
    if doc:
        return jsonify(doc), 200
    else:
        return jsonify({'mensagem': 'Charada não encontrada'}), 404    

# ---- Método POST - Adiciona uma nova charada ----
@app.route('/charadas', methods=['POST'])
def adicionar_charada():
    dados = request.json  # Obtém os dados enviados na requisição
    
    # Verifica se os campos obrigatórios estão presentes
    if "pergunta" not in dados or "resposta" not in dados:
        return jsonify({'mensagem': 'Erro. Campos pergunta e resposta são obrigatórios'}), 400
    
    # Obtém o contador de IDs para definir o novo ID
    contador_ref = db.collection('controle_id').document('contador')
    contador_doc = contador_ref.get().to_dict()
    ultimo_id = contador_doc.get('id')
    novo_id = int(ultimo_id) + 1  # Incrementa o ID
    
    # Atualiza o contador no Firestore
    contador_ref.update({'id': novo_id})
    
    # Adiciona a nova charada com o ID gerado
    db.collection('charadas').document(str(novo_id)).set({
        "id": novo_id,
        "pergunta": dados['pergunta'],
        "resposta": dados['resposta'] 
    })
    
    return jsonify({'mensagem': 'Charada cadastrada com sucesso!'}), 201

# ---- Método PUT - Atualiza uma charada existente ----
@app.route('/charadas/<id>', methods=['PUT'])
def alterar_charada(id):
    dados = request.json  # Obtém os novos dados da charada
    
    # Verifica se os campos obrigatórios estão presentes
    if "pergunta" not in dados or "resposta" not in dados:
        return jsonify({'mensagem': 'Erro. Campos pergunta e resposta são obrigatórios'}), 400
    
    doc_ref = db.collection('charadas').document(id)
    doc = doc_ref.get()
    
    # Verifica se o documento existe antes de atualizar
    if doc.exists:
        doc_ref.update({
            'pergunta': dados['pergunta'],
            'resposta': dados['resposta']
        })
        return jsonify({'mensagem': 'Charada atualizada com sucesso!'}), 201
    else:
        return jsonify({'mensagem': 'Erro. Charada não encontrada!'}), 404

# ---- Método DELETE - Remove uma charada por ID ----
@app.route('/charadas/<id>', methods=['DELETE'])
def deletar_charada(id):
    doc_ref = db.collection('charadas').document(id)
    doc = doc_ref.get()
    
    # Verifica se a charada existe antes de tentar deletar
    if not doc.exists:
        return jsonify({'mensagem': 'Erro. Charada não encontrada!'}), 404
    else:
        doc_ref.delete()
        return jsonify({'mensagem': 'Charada excluída com sucesso!'}), 200

# ---- Execução do servidor Flask ----
if __name__ == '__main__':
    app.run(debug=True)  # Inicia o servidor Flask em modo de depuração