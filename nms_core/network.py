import logging

from .models import Network
from .api import Api, types_mapping
from .api_models import RequestBody

logger = logging.getLogger('nms_logger')

class NetworkeController(Api):

    def select(self, id: int) -> Network:
        '''
        Запрос на информацию об одной станции
        :param id: id станции
        :return: объекс класса Station с информацией пр станции
        '''
        body = RequestBody(
            id=id,
            action='select',
            object=types_mapping[Network]
        )

        return self._nms_request(body=body, result_class=Network)

    def list(self):
        return self._list(result_class=Network)