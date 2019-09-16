import pytest
from marshmallow import Schema


def test_custom_schema_field_stringlist():
    from artifice.scraper.schemas.custom import StringList

    class TestSchema(Schema):
        string_list = StringList()

    schema = TestSchema()

    good_data = {'string_list': ['dog', 'cat', 'bat']}
    data, errors = schema.load(good_data)

    assert not errors
    assert data

    output, errors = schema.dump(data)

    assert not errors
    assert good_data == output

    empty_data = {'string_list': []}
    data, errors = schema.load(empty_data)

    assert not errors
    assert data

    empty_data = {'string_list': ''}
    data, errors = schema.dump(empty_data)

    assert not errors
    assert data
