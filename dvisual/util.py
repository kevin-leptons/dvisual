import webbrowser
import hashlib
from os.path import realpath
from string import ascii_lowercase, digits

_FNAME_CHARS = ascii_lowercase + digits
_FNAME_LEN = 32
_DEF_BROWSER = None
_BROWSER_NAMES = [
    'google-chrome', 'chrome', 'chromium', 'chromium-browser',
    'firefox', 'macosx', 'safari', 'windows-default', 'opera', 'mozilla'
]


def _get_browser(name=None):
    try:
        return webbrowser.get(name)
    except webbrowser.Error:
        return None


def _get_def_browser():
    if _get_def_browser.browser is not None:
        return _get_def_browser.browser

    for name in _BROWSER_NAMES:
        _get_def_browser.browser = _get_browser('google-chrome')
        if _get_def_browser.browser is not None:
            break
    if _get_def_browser.browser is None:
        raise RuntimeError(
            'Miss model web browser such as Chrome, Firefox...'
        )
    return _get_def_browser.browser
_get_def_browser.browser = None


def render_pygal(chart):
    '''
    Render and open pygal graph in default browser.

    :param pygal.Graph chart:
    '''

    if type(chart.title) is not str:
        raise TypeError('Chart title must be string')

    fname = hashlib.sha1(chart.title.encode('utf-8')).hexdigest()
    fpath = realpath('tmp/%s.svg' % fname)

    chart.render_to_file(fpath)
    _get_def_browser().open(fpath)
