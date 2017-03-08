# coding: utf-8

from .apis import Connect, Request


class RecastAI():
  def __init__(self, token=None, language=None, proxy=None):
    for api in [Connect, Request]:
      setattr(self, api.__name__.lower(), api(token=token, language=language, proxy=proxy))
