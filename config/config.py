from typing import List


class Config :
    selector: str
    id: str
    query: List[str]
    comment: str

    def __init__(self, _dict):
        self.selector = _dict.get('selector')
        self.id = _dict.get('id')
        self.query = _dict.get('query')
        self.comment = _dict.get('comment')
