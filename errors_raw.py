class HttpUnprocessableEntityError(Exception):
    def __init__(self, message: str) -> None:
        super().__init__(message)
        self.message = message
        self.nome = 'UnprocessableEntity'
        self.status_code = 422



try:
    print('EStou no bloco try')
    raise HttpUnprocessableEntityError('Estou lançando a exception')
except Exception as exception:
    print('Estou no tratamento de erro')
    print(exception.nome)
    print(exception.status_code)
    print(exception.message)