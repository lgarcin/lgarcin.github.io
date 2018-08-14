from bokeh.embed import autoload_static
from bokeh.resources import CDN
from glob import glob
import re


def embed_fig(p, js_file):
    js, tag = autoload_static(p, CDN, "/js/" + js_file)
    with open("js/" + js_file, 'w') as f:
        f.write(js)
    reg = '\n<script src="/js/' + js_file + '".*?>.*?</script>'
    for file in glob("_drafts/*.markdown") + glob("_posts/**/*.markdown"):
        with open(file, 'r') as f:
            text = f.read()
        if re.findall(reg, text):
            new_text = re.sub(reg, tag, text)
            with open(file, 'w') as f:
                f.write(new_text)
