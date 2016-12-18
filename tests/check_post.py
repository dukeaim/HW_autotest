# coding=utf-8

need_authorization = True


def run(manager):
    assert manager['navigation'].create_comment()
