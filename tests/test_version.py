import pymerra2


def test_version_definition():
    version = pymerra2.__version__
    assert version >= 0.2


if __name__ == '__main__':
    pass
