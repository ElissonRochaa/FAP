from app import db

class Usuario(db.Model):
    __tablename__ = "usuario"
    #ID
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    #Nome
    nome = db.Column(db.String(128), nullable=False)
    #Email
    email = db.Column(db.String(100), unique=True, nullable=False)
    #Senha
    senha = db.Column(db.String(510), nullable=False)
    #CPF
    cpf = db.Column(db.String(14))
    #Registro de inscricoes
    inscricoes = db.relationship('Inscricao', backref='usuario', lazy=True)

    def to_dict(self):
        return {
            'id':self.id,
            'nome': self.nome,
            'email': self.email,
            'cpf': self.cpf,
            'inscricoes':[inscricao.to_dict() for inscricao in self.inscricoes]
        }
    
    def to_dict_resumida(self):
        return {
            'id':self.id,
            'nome': self.nome,
            'email': self.email,
            'cpf': self.cpf
        }
