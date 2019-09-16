from marshmallow import fields, ValidationError


class StringList(fields.Field):
    '''
    # serialize
    >>> dump('red|blue|green')

        ['red','blue','green']

    # deserialize
    >>> load(['red','blue','green'])

        'red|blue|green'
    '''
    def _serialize(self, value, attr, obj):
        # DUMP
        if not value:
            return []
        return value.split('|~|')

    def _deserialize(self, value, attr, obj):
        # LOAD
        if not value:
            return ''
        return '|~|'.join(value)


class Uppercase(fields.Field):

    def _serialize(self, value, attr, obj):
        # DUMP
        if not value:
            value = ''
        return value.upper()


class SafeUrl(fields.Field):
    '''
    This is a safe way to filter urls. Inputs can assume
    to be sanitized on load. Otherwise identical urls that
    differ only by a trailing slash may otherwise be indexed
    as two different entries. This causes orhan tasks to propegate.

    As this field is always required, ValidationError is called
    upon unsuccessful handling.

    1.3.1   raise error manually if decoding fails
    '''
    def _serialize(self, value, attr, obj):
        # DUMP

        if not value:
            # value = ''
            raise ValidationError('schemas.custom.SafeUrl `{0}` unable to validate `{1}.'.format(value, attr))
        return value.strip('/')

    def _deserialize(self, value, attr, obj):
        # LOAD
        if not value:
            # value = ''
            raise ValidationError('schemas.custom.SafeUrl `{0}` unable to validate `{1}.'.format(value, attr))
        return value.strip('/')
