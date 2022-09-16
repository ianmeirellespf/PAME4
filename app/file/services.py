from app.file.models import File 
from app.file.schemas import FileSchema
from app.services import BaseCRUDServices

class FileServices(BaseCRUDServices, FileSchema):

    def get_by_email(self, nome: str) -> File:
        return self.model.query.filter_by(nome=nome).first()

file_services = FileServices(File)