try:
    # python 3
    from urllib.parse import urlencode, urlparse, urljoin, urlunparse
except ImportError:
    # python 2 backward compatibility
    # noinspection PyUnresolvedReferences
    from urllib.parse import urlencode
    # noinspection PyUnresolvedReferences
    from urllib.parse import urlparse, urljoin, urlunparse
