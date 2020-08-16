# Standard Library
from abc import ABC, abstractmethod
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

    @abstractmethod
    def _init_session(self) -> None:
        pass

    def _fetch(self, request: Request) -> Response:
        print(f'Requesting [{request.method}] : {request.url}')
        request.headers = self.session.headers
        prepared_request = request.prepare()
        # request.params.update({'text_format': 'plain'})
        for attempt in range(self.max_attempts):
            try:
                response = self.session.send(prepared_request, timeout = self.timeout)
                if response.status_code == 200:
                    return response
                print(response.text)
                raise HTTPError(f'Bad Request {response.status_code}')
            
            except (Timeout, ConnectionError, HTTPError) as error:
                print(f'{type(error)}!')
                time_sleep(self.failed_sleep_time)
