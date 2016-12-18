# coding=utf-8


def run(manager):
    assert not manager['forms'].authorization('namer', 'passot')
    assert manager['forms'].valid_authorization()
