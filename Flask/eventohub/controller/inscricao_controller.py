from flask import Blueprint, jsonify, request
from service.inscricao_service import InscricaoService
from entity.inscricao import Inscricao
from datetime import datetime

inscricao_bp = Blueprint("Inscricao", __name__)

@inscricao_bp.route('', methods=['GET'])
def buscar_todos():
    inscricoes = InscricaoService.buscar_todos()
    #return jsonify([inscricao.to_dict() for inscricao in inscricoes])
    inscricoes_dict = []
    for inscricao in inscricoes:
        inscricoes_dict.append(inscricao.to_dict())
    return jsonify(inscricoes_dict)

@inscricao_bp.route('', methods=['POST'])
def criar_inscricao():
    data = request.get_json()
    print(data)
    data_inscricao = datetime.strptime(data['data_inscricao'], '%Y/%m/%d')
    inscricao = Inscricao(id_usuario=data['id_usuario'],
                          id_evento=data['id_evento'],
                          data_inscricao=data_inscricao,
                          desconto=data['desconto'],
                          valor=data['valor'])
    
    try:
        inscricao = InscricaoService.criar_inscricao(inscricao)
        return jsonify(inscricao.to_dict()), 201
    except Exception as e:
        return jsonify({'error':str(e)}), 400
    