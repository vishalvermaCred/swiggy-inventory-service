from http.client import HTTPException

"""
    functions declared here will be executed before the API runs
"""


class MissingEnvConfigsException(Exception):
    def __init__(self, parameters):
        self.code = 501
        self.message = f"Missing Env Configs: {parameters}"

    def __str__(self):
        return self.message


class HTTPBaseException(HTTPException):
    code = 500
    message = "Helicarrier Base Exception"
