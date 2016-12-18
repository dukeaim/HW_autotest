# coding=utf-8


def run(manager):
    assert manager['forms'].search('vape')
    assert not manager['forms'].search('grksdlgksdkajsbkanskvc')

