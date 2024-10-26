import datetime
import enum
from app import db

class TipoEvento(enum.Enum):
    presencial = 'PRESENCIAL'
    hibrido = 'HIBRIDO'
    online = 'ONLINE'

class Evento(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    titulo = db.Column(db.String(120), nullable=False)
    descricao = db.Column(db.String(500))
    valor = db.Column(db.Float, nullable=False)
    data = db.Column(db.DateTime)
    tipoEvento = db.Column(db.Enum(TipoEvento), nullable=False)
    inscricoes = db.relationship('Inscricao', backref='evento', lazy=True)

    def to_dict(self):
        return {
            'id':self.id,
            'titulo':self.titulo,
            'descricao':self.descricao,
            'valor':self.valor,
            'data':self.data,
            'tipoEvento':self.tipoEvento.value,
            'inscricoes':[inscricao.to_dict() for inscricao in self.inscricoes]
        }
    
    def to_dict_resumida(self):
        return {
            'id':self.id,
            'titulo':self.titulo,
            'descricao':self.descricao,
            'valor':self.valor,
            'data':self.data,
            'tipoEvento':self.tipoEvento.value
        }