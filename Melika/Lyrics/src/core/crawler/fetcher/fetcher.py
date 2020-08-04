# Standard Library
from abc import ABC, abstractclassmethod
from typing import Union
from time import sleep as time_sleep

# Site Packages
from requests import Session, Request, Response, PreparedRequest, Timeout, HTTPError, ConnectionError


"""
Abstract Class Fetcher
    Sends request -> Recieves Response
"""
class Fetcher(ABC):

    __slot__ = 'session', 'max_attempts', 'failed_sleep_time', 'timeout'

    def __init__(self, max_attempts: int, failed_sleep_time: Union[float, int], timeout: Union[float, int]):
        self.max_attempts = max_attempts
        self.failed_sleep_time = failed_sleep_time
        self.timeout = timeout

    @abstractclassmethod
    def _init_session(self) -> None:
        pass

    def _send_request(self, request: Request) -> Response:
        response: Response = self.session.send(request)
        if response.status_code == 200:
            return response
        raise HTTPError('Bad Request!')

    def _fetch(self, request: Request) -> Response:
        prepared_request: PreparedRequest = request.prepare()
        for attempt in range(self.max_attempts):
            try:
                return self._send_request(prepared_request)
            except Timeout:
                time_sleep(self.failed_sleep_time)
            except ConnectionError:
                print('Net Qate!')
                time_sleep(self.failed_sleep_time)
            except HTTPError:
                print('Bad Request!')
                time_sleep(self.failed_sleep_time)
