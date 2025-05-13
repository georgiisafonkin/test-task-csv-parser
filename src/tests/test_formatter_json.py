from formatters.json_formatter import JsonFormatter

def test_json_formatter_output():
    data = {"a": 1, "b": 2}
    output = JsonFormatter.format(data)
    assert isinstance(output, str)
    assert '"a": 1' in output
