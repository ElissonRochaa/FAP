from flask import Blueprint, jsonify, request
from entity.evento import Evento, TipoEvento
from service.evento_service import EventoService
from datetime import datetime

evento_bp = Blueprint('evento', __name__)


@evento_bp.route('', methods=['GET'])
def buscar_todos():
    eventos = EventoService.buscar_todos()
    return jsonify([evento.to_dict() for evento in eventos])

@evento_bp.route('', methods=['POST'])
def criar_evento():
    data = request.get_json()
    print(data)
    # Converter a data de string para datetime
    data_evento = datetime.strptime(data.get("data"), "%Y/%m/%d")
        
    # Converter tipoEvento para enum
    tipo_evento = TipoEvento[data.get("tipoEvento")]
    evento = Evento(titulo=data['titulo'], descricao=data['descricao'],
                    valor=data['valor'], data=data_evento, tipoEvento=tipo_evento)
    
    try:
        evento = EventoService.create(evento)
        return jsonify(evento.to_dict()), 201

    except Exception as e:
        return jsonify({"error":str(e)}), 400