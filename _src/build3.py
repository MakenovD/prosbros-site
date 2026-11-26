# v3 build: v2 design + copy from the Schwartz / Great Leads review (i18n_v3.py).
import os
import i18n_v3
i18n_v3.apply()
import build2
from build2 import OUT, LANGS, EXTRA, head, body, JS

CSS_ADD = """
.bridge{font-family:var(--display);text-transform:uppercase;font-weight:600;font-size:22px;letter-spacing:.01em;color:#fff;padding-bottom:10px}
.safe{font-size:14px;line-height:1.55;color:var(--td);margin:-4px 0 18px;max-width:560px}
.safe b{color:#fff;font-weight:600}
@media (min-width:761px){.steps{grid-template-columns:repeat(4,1fr)}.hero h1{font-size:clamp(40px,4.6vw,66px)}}
@media (min-width:761px) and (max-width:1080px){.steps{grid-template-columns:repeat(2,1fr)}.steps::before{display:none}}
@media (max-width:760px){.bridge{font-size:17px;padding-bottom:6px}.safe{font-size:13px}}
"""


def page(L):
    h = head(L).replace("site_version:'v2'", "site_version:'v3'").replace('site.css?v=2', 'site.css?v=3')
    b = body(L)
    X = EXTRA[L['code']]
    b = b.replace('<p class="wrap src">', f'<p class="wrap bridge">{L["bridge"]}</p><p class="wrap src">', 1)
    b = b.replace('<div class="qs" role="group">', f'<p class="safe">{L["safe"]}</p><div class="qs" role="group">', 1)
    assert 'class="wrap bridge"' in b and 'class="safe"' in b
    return h + b + '\n' + JS + '\n</body>\n</html>\n'


def build():
    os.makedirs(os.path.join(OUT, 'assets'), exist_ok=True)
    open(os.path.join(OUT, 'assets', 'site.css'), 'w').write(build2.CSS.strip() + '\n' + CSS_ADD.strip() + '\n')
    for L in LANGS:
        d = OUT if L['path'] == '/' else os.path.join(OUT, L['code'])
        os.makedirs(d, exist_ok=True)
        open(os.path.join(d, 'index.html'), 'w', encoding='utf-8').write(page(L))


if __name__ == '__main__':
    build()
    print('built v3')
