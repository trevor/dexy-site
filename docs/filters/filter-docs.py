from pygments import highlight
from pygments.formatters.html import HtmlFormatter
from pygments.lexers.agile import PythonLexer
import dexy.introspect
import inspect
import json

filters = dexy.introspect.filters()

py_lexer = PythonLexer()
fm = HtmlFormatter(lineanchors = "l", anchorlinenos=True, linenos='table')

filter_info = {}
for k, v in filters.items():
    name = v.__name__
    if not filter_info.has_key(name):
        source = inspect.getsource(v)
        html_source = highlight(source, py_lexer, fm)
        filter_info[name] = {
            'aliases' : v.ALIASES,
            'final' : v.FINAL,
            'parentclass' : v.__base__.__name__,
            'doc' : v.__doc__,
            'source' : source,
            'module' : v.__module__,
            'html_source' : html_source
        }

with open("dexy--filter-info.json", "w") as f:
    json.dump(filter_info, f, sort_keys=True, indent=4)

