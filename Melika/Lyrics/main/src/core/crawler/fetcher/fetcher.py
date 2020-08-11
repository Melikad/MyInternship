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
        print(response.text)
        raise HTTPError('Bad Request!')

    def _get(self, request: Request) -> Response:
        request.params.update({'text_format': 'plain'})
        for attempt in range(self.max_attempts):
            try:
                response = self.session.request('GET', request.url, timeout=self.timeout, params=request.params)
                if response.status_code == 200:
                    return response
                raise HTTPError(f'Bad Request {response.status_code}');
            except (Timeout, ConnectionError, HTTPError) as error:
                print(f'{type(error)}}!')
                time_sleep(self.failed_sleep_time)
