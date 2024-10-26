from app import db

class Inscricao(db.Model):

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_usuario = db.Column(db.Integer, db.ForeignKey("usuario.id"), nullable=False)
    id_evento = db.Column(db.Integer, db.ForeignKey("evento.id"), nullable=False)
    data_inscricao = db.Column(db.DateTime)
    desconto = db.Column(db.Float)
    valor = db.Column(db.Float)

    def to_dict(self):
        return {
            'id':self.id,
            'usuario': self.usuario.to_dict_resumida(),
            'evento': self.evento.to_dict_resumida(),
            'data_inscricao': self.data_inscricao,
            'desconto':self.desconto,
            'valor':self.valor
        }