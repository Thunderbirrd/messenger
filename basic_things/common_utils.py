from basic_things.main_variables import *
import json
from errors import IncorrectDataReceivedError, NonDictInputError
import sys
sys.path.append('../')
from decorators import log


@log
def get_message(client):
    encoded_response = client.recv(MAX_PACKAGE_BYTE_LENGTH)
    if isinstance(encoded_response, bytes):
        json_response = encoded_response.decode(ENCODING)
        response = json.loads(json_response)
        if isinstance(response, dict):
            return response
        else:
            raise IncorrectDataReceivedError
    else:
        raise IncorrectDataReceivedError


@log
def send_message(socket, message):
    if not isinstance(message, dict):
        raise NonDictInputError
    json_message = json.dumps(message)
    encoded_message = json_message.encode(ENCODING)
    socket.send(encoded_message)
