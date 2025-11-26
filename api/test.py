from translator import handler


class MockRequest():
    def __init__(self, _json):
        self._json = _json

    def get_json(self):
        return self._json


json_test_list = [
    [{}, 400],
    [{"q": "Hello"}, 400],
    [{"langpair": "en|uz"}, 400],
    [{"q": "Hello", "langpair": "en|uz"}, 200],
    [{"q": "I", "langpair": "en|uz"}, 200],
    [{"q": "K", "langpair": "en|uz"}, 200],
    [{"q": "Idontknow", "langpair": "en|uz"}, 200],
    [{"q": "Hello", "langpair": ""}, 400],
    [{"q": "Hello", "langpair": " "}, 400],
    [{"q": "Hello", "langpair": "en|"}, 400],
    [{"q": "Hello", "langpair": "enr|uz"}, 400],
    [{"q": "Hello", "langpair": "hello"}, 400],
    [{"q": "Hello", "langpair": "testingTranslator"}, 400],
    [{"q": "", "langpair": "en|uz"}, 400],
    [{"q": " ", "langpair": "en|uz"}, 400],
    [{"q": None, "langpair": "en|uz"}, 400],
    [{"q": "Hello", "langpair": None}, 400],
    [{"q": 123, "langpair": "en|uz"}, 400],
    [{"q": "Hello", "langpair": 123}, 400],
    [{"q": ["Hello"], "langpair": "en|uz"}, 400],
    [{"q": "Hello", "langpair": ["en|uz"]}, 400],
    [{"q": "😂", "langpair": "en|uz"}, 200],
]

for json_data in json_test_list:
    r = MockRequest(json_data[0])
    assert handler(r)["statusCode"] == json_data[
        1], f"Failed test: {json_data[0]}, got {handler(r)}"
