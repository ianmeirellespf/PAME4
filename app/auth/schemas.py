from ..extensions import ma


class SenhaNovaSchema(ma.Schema):
    email = ma.Email(required=True)
    senha = ma.String(required=True, load_only=True)
    verificationPin = ma.String(required=True, load_only=True)