from flask import Flask, jsonify
import random 

app = Flask('__name__')

charadas = [
  {
    "id": 1,
    "pergunta": "Por que a vassoura não luta caratê?",
    "resposta": "Porque ela já luta capoeira."
  },
  {
    "id": 2,
    "pergunta": "O que é que tem cabeça, mas não tem corpo?",
    "resposta": "O alfinete."
  },
  {
    "id": 3,
    "pergunta": "O que é que está sempre na sua frente, mas não pode ser visto?",
    "resposta": "O futuro."
  },
  {
    "id": 4,
    "pergunta": "O que é que tem muitos dentes, mas não pode morder?",
    "resposta": "O pente."
  },
  {
    "id": 5,
    "pergunta": "O que é que tem folhas, mas não é uma árvore?",
    "resposta": "Um livro."
  },
  {
    "id": 6,
    "pergunta": "O que é que sempre quebra quando você fala?",
    "resposta": "O silêncio."
  },
   {
    "id": 7,
    "pergunta": "O que é que quanto mais se tira, maior fica?",
    "resposta": "O buraco."
  },
  {
    "id": 8,
    "pergunta": "O que é que anda com os pés na cabeça?",
    "resposta": "O piolho."
  },
  {
    "id": 9,
    "pergunta": "O que é que quanto mais se enche, mais leve fica?",
    "resposta": "O balão."
  },
  {
    "id": 10,
    "pergunta": "O que é que cai em pé e corre deitado?",
    "resposta": "A chuva."
  }
]

@app.route('/', methods = ['GET'])
def index():
    return 'CHARADAS API', 200


@app.route('/charadas', methods = ['GET'])
def charada():
    return jsonify(random.choice(charadas)), 200

@app.route('/charadas/<int:id>', methods = ['GET'])
def busca(id):
    for charada in charadas:
        if charada['id'] == id:
            return jsonify(charada), 200
    
    return jsonify({'mensagem': 'Erro! - Charada não encontrada'}), 404
    



if __name__ == '__main__':
    app.run()
    
