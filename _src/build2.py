"""ProsBros landing v2: dark hero with photo + animated phone chat, trades strip, Ask-Bro demo. All languages."""
import json, os, html
from i18n import LANGS, QUOTES
from i18n_extra import EXTRA, CHAT, DEMO, PHOTOS
from build import ph_snippet, svg, ICONS, GLOBE, CHEV, BASE

OUT = os.path.join(os.path.dirname(__file__), 'site')

def img(pid, w, h=None, q=70):
    u = f'https://images.unsplash.com/{pid}?auto=format&fit=crop&w={w}&q={q}'
    return u + (f'&h={h}' if h else '')

CSS = r"""
:root{--ink:#0D1117;--ink2:#141A22;--ink3:#1C2430;--ld:rgba(255,255,255,.10);--td:#D0D7DE;--md:#8B949E;
--brand:#F26B1D;--brand-d:#C2410C;--brand-l:#FFB27A;--cream:#F6F3EE;--line:#E6E0D7;--t:#0D1117;--t2:#2B3440;--mute:#5B6573;
--display:'Oswald','Arial Narrow',sans-serif;--r:18px}
*{box-sizing:border-box}
html{scroll-behavior:smooth;-webkit-text-size-adjust:100%;overflow-x:clip}
body{overflow-x:clip;-webkit-tap-highlight-color:transparent}
.wrap>*{min-width:0}
body{margin:0;background:var(--cream);color:var(--t);font-family:Inter,system-ui,sans-serif;line-height:1.5;-webkit-font-smoothing:antialiased}
p,h1,h2,h3,ul,ol{margin:0}
a{color:var(--brand-d)}
img{max-width:100%;display:block}
:focus-visible{outline:3px solid var(--brand-l);outline-offset:2px}
.wrap{max-width:1240px;margin:0 auto;padding:0 28px}
.d{font-family:var(--display);text-transform:uppercase;letter-spacing:.005em}
.eyebrow{font-size:13px;font-weight:700;letter-spacing:.12em;text-transform:uppercase;color:var(--brand-d)}
.dark .eyebrow{color:var(--brand-l)}
.h2{overflow-wrap:break-word;font-family:var(--display);text-transform:uppercase;font-weight:700;font-size:clamp(34px,4.4vw,60px);line-height:1;letter-spacing:.005em}
.lead{font-size:18px;line-height:1.6;color:var(--t2)}
.dark{background:var(--ink);color:#fff}
.dark .lead{color:var(--td)}
.btn{display:inline-flex;align-items:center;justify-content:center;gap:10px;text-decoration:none;font-weight:700;border-radius:999px;padding:17px 28px;font-size:16.5px;min-height:54px;text-align:center;border:0;cursor:pointer;font-family:inherit;transition:transform .15s,background .15s,box-shadow .15s}
.btn:hover{transform:translateY(-1px)}
.btn-brand{background:var(--brand);color:#fff;box-shadow:0 10px 30px -8px rgba(242,107,29,.7)}
.btn-brand:hover{background:#ff7a2c;color:#fff}
.btn-ghost{background:transparent;color:#fff;border:1.5px solid rgba(255,255,255,.28)}
.btn-ghost:hover{border-color:#fff;color:#fff}
.btn-ink{background:var(--ink);color:#fff}.btn-ink:hover{background:#000;color:#fff}
.btn-line{background:#fff;color:var(--t);border:1.5px solid var(--line)}.btn-line:hover{border-color:var(--t);color:var(--t)}
.btn svg{flex:none}
section{scroll-margin-top:70px;position:relative}

/* reveal */
.js .rv{opacity:0;transform:translateY(22px);transition:opacity .7s ease,transform .7s cubic-bezier(.2,.7,.2,1)}
.js .rv.in{opacity:1;transform:none}
.js .rv.d1{transition-delay:.08s}.js .rv.d2{transition-delay:.16s}.js .rv.d3{transition-delay:.24s}

/* header */
.refbar{background:var(--brand);color:#fff;text-align:center;font-weight:600;font-size:14.5px;line-height:1.45;padding:10px 18px}
.hdr{position:sticky;top:0;z-index:40;background:rgba(13,17,23,.78);backdrop-filter:saturate(1.4) blur(14px);-webkit-backdrop-filter:saturate(1.4) blur(14px);border-bottom:1px solid var(--ld)}
.hdr .wrap{display:flex;align-items:center;justify-content:space-between;gap:16px;height:72px}
.logo img{height:40px;width:auto}
.nav{display:flex;align-items:center;gap:26px;font-size:15px}
.nav a.l{color:var(--td);text-decoration:none;font-weight:500}.nav a.l:hover{color:#fff}
.nav .btn{padding:11px 18px;min-height:44px;font-size:14.5px}
.cta-short{display:none}
.lang{position:relative}
.lang summary{list-style:none;cursor:pointer;display:flex;align-items:center;gap:6px;font-size:14px;font-weight:600;color:var(--td);padding:10px 10px;border-radius:999px;min-height:44px}
.lang summary::-webkit-details-marker{display:none}
.lang[open] summary,.lang summary:hover{background:rgba(255,255,255,.08);color:#fff}
.lang ul{position:absolute;right:0;top:calc(100% + 8px);list-style:none;padding:6px;background:#fff;border-radius:14px;box-shadow:0 20px 50px rgba(0,0,0,.35);min-width:180px;z-index:50}
.lang li a{display:flex;justify-content:space-between;gap:12px;padding:11px 12px;border-radius:9px;color:var(--t);text-decoration:none;font-size:15px}
.lang li a:hover{background:var(--cream)}
.lang li a[aria-current]{font-weight:700;color:var(--brand-d)}
.lang li span{color:#9CA3AF;font-size:13px}

/* hero */
.hero{overflow:hidden;background:radial-gradient(900px 520px at 88% 8%,rgba(242,107,29,.22),transparent 60%),radial-gradient(700px 500px at 0% 100%,rgba(242,107,29,.08),transparent 60%),var(--ink)}
.hero::before{content:"";position:absolute;inset:0;background-image:linear-gradient(rgba(255,255,255,.035) 1px,transparent 1px),linear-gradient(90deg,rgba(255,255,255,.035) 1px,transparent 1px);background-size:56px 56px;mask-image:linear-gradient(180deg,#000 0%,transparent 85%);-webkit-mask-image:linear-gradient(180deg,#000 0%,transparent 85%);pointer-events:none}
.hero .wrap{display:grid;grid-template-columns:minmax(0,1.02fr) minmax(0,1fr);gap:56px;align-items:center;padding-top:76px;padding-bottom:84px;position:relative}
.hero-l{display:flex;flex-direction:column;gap:26px}
.badge{align-self:flex-start;display:inline-flex;align-items:center;gap:10px;padding:8px 14px 8px 10px;border:1px solid var(--ld);border-radius:999px;font-size:13.5px;font-weight:600;color:var(--td);background:rgba(255,255,255,.04)}
.pulse{width:9px;height:9px;border-radius:9px;background:var(--brand);box-shadow:0 0 0 0 rgba(242,107,29,.7);animation:pulse 2s infinite}
@keyframes pulse{70%{box-shadow:0 0 0 9px rgba(242,107,29,0)}100%{box-shadow:0 0 0 0 rgba(242,107,29,0)}}
.fl .hero .wrap{opacity:0}
.hero .wrap{transition:opacity .25s}
.hero h1{font-family:var(--display);text-transform:uppercase;font-weight:700;font-size:clamp(44px,5.6vw,80px);line-height:.95;letter-spacing:.003em}
.hl{color:var(--brand);position:relative;white-space:nowrap}
.hero .sub{font-size:19px;line-height:1.6;color:var(--td);max-width:560px}
.ctas{display:flex;flex-wrap:wrap;gap:12px}
.trust{display:flex;flex-wrap:wrap;gap:8px 18px;font-size:14px;color:var(--md);list-style:none;padding:0}
.trust li{display:flex;align-items:center;gap:7px}
.trust li::before{content:"";width:16px;height:16px;flex:none;background:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='%23F26B1D' stroke-width='3' stroke-linecap='round' stroke-linejoin='round'%3E%3Cpath d='M5 12l5 5L20 7'/%3E%3C/svg%3E") center/contain no-repeat}

.vis{position:relative;height:600px}
.photo{position:absolute;right:0;top:0;width:80%;height:90%;border-radius:28px;overflow:hidden;box-shadow:0 40px 80px -30px rgba(0,0,0,.8)}
.photo img{width:100%;height:100%;object-fit:cover;object-position:40% 50%}
.photo::after{content:"";position:absolute;inset:0;background:linear-gradient(200deg,rgba(13,17,23,0) 40%,rgba(13,17,23,.55) 100%)}
.phone{position:absolute;left:0;bottom:0;width:292px;height:568px;border-radius:46px;background:#05070A;padding:11px;box-shadow:0 50px 90px -20px rgba(0,0,0,.85),0 0 0 1px rgba(255,255,255,.08);z-index:2}
.scr{position:relative;width:100%;height:100%;border-radius:36px;background:#F4F4F6;overflow:hidden;display:flex;flex-direction:column}
.notch{position:absolute;top:8px;left:50%;transform:translateX(-50%);width:96px;height:26px;border-radius:20px;background:#05070A;z-index:3}
.ph-h{padding:44px 16px 12px;background:#fff;border-bottom:1px solid #ECECEF;display:flex;gap:10px;align-items:center}
.av{width:36px;height:36px;border-radius:36px;background:#E8DFF5;color:#5B3E8E;font-weight:700;display:flex;align-items:center;justify-content:center;font-size:15px;flex:none}
.ph-h b{display:block;font-size:14px;color:#111}
.ph-h small{display:flex;align-items:center;gap:5px;font-size:11.5px;color:var(--brand-d);font-weight:600}
.ph-h small i{width:6px;height:6px;border-radius:6px;background:var(--brand);display:block;animation:pulse 2s infinite}
.chat{flex:1;padding:14px 12px;display:flex;flex-direction:column;gap:8px;justify-content:flex-end;overflow:hidden}
.bub{max-width:84%;padding:9px 12px;border-radius:18px;font-size:13px;line-height:1.38;color:#111;background:#fff;box-shadow:0 1px 1px rgba(0,0,0,.05);align-self:flex-start;border-bottom-left-radius:6px}
.bub.b{align-self:flex-end;background:var(--ink);color:#fff;border-bottom-left-radius:18px;border-bottom-right-radius:6px}
.bub.typing{gap:4px;padding:12px 14px;display:none}
.bub.typing.b i{background:#6E7681}
.bub.typing i{width:6px;height:6px;border-radius:6px;background:#9AA1AB;animation:blink 1.2s infinite}
.bub.typing i:nth-child(2){animation-delay:.15s}.bub.typing i:nth-child(3){animation-delay:.3s}
@keyframes blink{0%,60%,100%{opacity:.25}30%{opacity:1}}
.js .chat .bub{display:none}
.js .chat .bub.on{display:block;animation:pop .35s cubic-bezier(.2,.9,.3,1.2)}
.js .chat .bub.typing.on{display:flex}
@keyframes pop{from{opacity:0;transform:translateY(8px) scale(.96)}to{opacity:1;transform:none}}
.ph-in{margin:0 10px 12px;padding:10px 14px;border-radius:22px;background:#fff;border:1px solid #E5E5EA;font-size:12.5px;color:#9AA1AB}
.notif{position:absolute;left:10px;right:10px;top:42px;z-index:4;background:rgba(255,255,255,.97);border-radius:18px;padding:11px 12px;display:flex;gap:10px;align-items:center;box-shadow:0 12px 30px rgba(0,0,0,.18);transform:translateY(-140%);transition:transform .5s cubic-bezier(.2,.9,.3,1.1)}
.notif.on{transform:none}
.notif .ic{width:34px;height:34px;border-radius:10px;background:var(--brand);display:flex;align-items:center;justify-content:center;flex:none}
.notif b{display:block;font-size:13px;color:#111}
.notif small{font-size:12px;color:#555}
.mproof{display:none}
.chip{position:absolute;z-index:3;display:flex;align-items:center;gap:9px;padding:10px 14px;border-radius:14px;background:rgba(20,26,34,.82);backdrop-filter:blur(10px);-webkit-backdrop-filter:blur(10px);border:1px solid rgba(255,255,255,.12);color:#fff;font-size:13.5px;font-weight:600;box-shadow:0 18px 40px -12px rgba(0,0,0,.6);animation:float 6s ease-in-out infinite;white-space:nowrap}
.chip .dot{width:26px;height:26px;border-radius:8px;display:flex;align-items:center;justify-content:center;background:rgba(242,107,29,.18);flex:none}
.chip.c1{top:7%;right:56%}
.chip.c2{top:38%;right:-2%;animation-delay:-2s}
.chip.c3{bottom:16%;right:6%;animation-delay:-4s;background:var(--brand);border-color:transparent}
.chip.c3 .dot{background:rgba(255,255,255,.22)}
@keyframes float{0%,100%{transform:translateY(0)}50%{transform:translateY(-8px)}}

/* trades */
.trades{background:var(--ink);border-top:1px solid var(--ld);padding:34px 0 40px}
.trades .wrap{display:flex;flex-direction:column;gap:18px}
.trades h2{font-size:13px;font-weight:700;letter-spacing:.14em;text-transform:uppercase;color:var(--md)}
.tr-g{display:grid;grid-template-columns:repeat(6,1fr) auto;gap:12px;list-style:none;padding:0;align-items:stretch}
.tr{position:relative;height:116px;border-radius:16px;overflow:hidden;background:var(--ink3)}
.tr img{width:100%;height:100%;object-fit:cover;transition:transform .5s;filter:saturate(.85)}
.tr:hover img{transform:scale(1.06)}
.tr::after{content:"";position:absolute;inset:0;background:linear-gradient(180deg,transparent 30%,rgba(0,0,0,.78))}
.tr span{position:absolute;left:12px;bottom:10px;z-index:2;font-family:var(--display);text-transform:uppercase;font-weight:600;font-size:17px;letter-spacing:.02em;color:#fff}
.tr-more{display:flex;align-items:center;justify-content:center;padding:0 18px;border:1px dashed rgba(255,255,255,.22);border-radius:16px;color:var(--td);font-size:14px;font-weight:600;text-align:center;min-width:120px}

/* stats */
.stats{background:var(--ink2);border-top:1px solid var(--ld)}
.stats-g{display:grid;grid-template-columns:repeat(3,1fr);gap:0;padding-top:56px;padding-bottom:20px}
.stat{padding:0 32px;border-left:1px solid var(--ld)}
.stat:first-child{border-left:0;padding-left:0}
.stat .n{font-family:var(--display);font-size:62px;font-weight:700;line-height:1;color:var(--brand);text-transform:uppercase}
.stat .t{font-size:16px;line-height:1.5;color:var(--td);margin-top:12px;max-width:320px}
.src{font-size:12px;color:#6E7681;padding-bottom:36px}

/* pilot */
.pilot .wrap{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1fr);gap:56px;align-items:center;padding-top:110px;padding-bottom:110px}
.pilot-l{display:flex;flex-direction:column;gap:20px}
.pilot-g{display:grid;grid-template-columns:1fr 1fr;gap:12px;margin-top:8px}
.pc{background:#fff;border:1px solid var(--line);border-radius:var(--r);padding:20px 22px}
.pc .n{font-family:var(--display);font-size:46px;font-weight:700;line-height:1}
.pc .t{font-size:14.5px;color:var(--mute);margin-top:8px;line-height:1.45}
.pc.hot{background:var(--brand);border-color:var(--brand);color:#fff}.pc.hot .t{color:rgba(255,255,255,.9)}
.case{background:var(--ink);color:#fff;border-radius:28px;padding:26px;display:flex;flex-direction:column;gap:12px;box-shadow:0 40px 80px -40px rgba(13,17,23,.6);position:relative;overflow:hidden}
.case::before{content:"";position:absolute;width:320px;height:320px;right:-120px;top:-140px;background:radial-gradient(circle,rgba(242,107,29,.35),transparent 65%)}
.case-h{display:flex;justify-content:space-between;align-items:center;gap:12px;position:relative}
.case-h p{font-size:13px;font-weight:700;letter-spacing:.1em;text-transform:uppercase;color:var(--md)}
.pill{font-size:12.5px;font-weight:700;color:#fff;background:var(--brand);padding:6px 11px;border-radius:999px;white-space:nowrap}
.msg{position:relative;background:var(--ink3);border:1px solid var(--ld);border-radius:16px;padding:14px 16px;display:flex;flex-direction:column;gap:6px}
.msg b{font-size:15.5px;font-weight:600}
.msg small{font-size:13px;color:var(--md)}
.msg::after{content:"";position:absolute;right:14px;top:16px;width:8px;height:8px;border-radius:8px;background:var(--brand)}
.bell{position:relative;background:#fff;color:var(--t);border-radius:16px;padding:14px 16px;display:flex;gap:12px;align-items:center;font-size:14.5px;line-height:1.4;font-weight:500}
.bell svg{flex:none}
.case-cap{font-size:12px;color:var(--md);position:relative}

/* how */
.how{background:#fff;border-top:1px solid var(--line)}
.how .wrap{padding-top:100px;padding-bottom:100px;display:flex;flex-direction:column;gap:44px}
.steps{display:grid;grid-template-columns:repeat(3,1fr);gap:28px;list-style:none;padding:0;counter-reset:s;position:relative}
.steps::before{content:"";position:absolute;left:0;right:0;top:44px;height:2px;background:repeating-linear-gradient(90deg,var(--line) 0 10px,transparent 10px 18px)}
.step{position:relative;display:flex;flex-direction:column;gap:14px}
.num{font-family:var(--display);font-weight:700;font-size:88px;line-height:1;color:transparent;-webkit-text-stroke:2px var(--t);background:#fff;align-self:flex-start;padding-right:14px;position:relative}
.step:last-child .num{-webkit-text-stroke-color:var(--brand)}
.step h3{font-size:22px;line-height:1.25;font-weight:700}
.step p{font-size:16px;line-height:1.6;color:var(--mute)}

/* demo */
.demo{background:radial-gradient(800px 500px at 100% 0%,rgba(242,107,29,.16),transparent 60%),var(--ink)}
.demo .wrap{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1.05fr);gap:56px;align-items:center;padding-top:110px;padding-bottom:110px}
.demo-l{display:flex;flex-direction:column;gap:20px}
.qs{display:flex;flex-direction:column;gap:10px;margin-top:6px}
.q{display:flex;align-items:center;justify-content:space-between;gap:12px;text-align:left;width:100%;padding:15px 18px;border-radius:14px;border:1px solid var(--ld);background:rgba(255,255,255,.04);color:#fff;font-size:15.5px;font-weight:600;font-family:inherit;cursor:pointer;transition:background .15s,border-color .15s;min-height:52px}
.q:hover{background:rgba(255,255,255,.08)}
.q[aria-pressed="true"]{border-color:var(--brand);background:rgba(242,107,29,.12)}
.q svg{flex:none;opacity:.6}
.demo-note{font-size:13px;color:var(--md)}
.win{background:#F4F4F6;border-radius:26px;overflow:hidden;box-shadow:0 50px 90px -30px rgba(0,0,0,.8);min-height:420px;display:flex;flex-direction:column}
.win-h{background:#fff;padding:14px 18px;display:flex;align-items:center;gap:8px;border-bottom:1px solid #E7E7EC}
.win-h i{width:11px;height:11px;border-radius:11px;background:#E5E5EA;display:block}
.win-h span{margin-left:8px;font-size:13px;font-weight:600;color:#555}
.log{height:330px;overflow:hidden;padding:22px;display:flex;flex-direction:column;gap:10px;justify-content:flex-end}
.log .who{font-size:11.5px;font-weight:600;color:#888;margin:4px 2px -4px}
.log .who.b{align-self:flex-end;color:var(--brand-d)}
.log .bub{font-size:14.5px;max-width:80%;padding:11px 15px}
.rtag{align-self:flex-end;font-size:12px;font-weight:600;color:#1F7A4D;background:#E7F6EE;padding:4px 10px;border-radius:999px;margin-top:-2px}
.ctrl{display:flex;align-items:center;gap:10px;font-family:var(--display);text-transform:uppercase;font-weight:600;font-size:20px;letter-spacing:.02em;color:#fff}
.ctrl svg{flex:none}
.empty{color:#8A9099;font-size:15px;text-align:center;margin:auto 0}
.win-cta{padding:0 22px 22px}
.win-cta .btn{width:100%}

/* features */
.feat{background:var(--cream)}
.feat .wrap{padding-top:100px;padding-bottom:100px;display:flex;flex-direction:column;gap:40px}
.feat-hint{display:none}
.feat-g{display:grid;grid-template-columns:repeat(auto-fit,minmax(280px,1fr));gap:14px}
.fi{background:#fff;border:1px solid var(--line);border-radius:var(--r);padding:24px;transition:transform .2s,box-shadow .2s}
.fi:hover{transform:translateY(-3px);box-shadow:0 20px 40px -24px rgba(13,17,23,.35)}
.fi-h{all:unset;display:flex;flex-direction:column;gap:14px;width:100%;box-sizing:border-box;cursor:default}
.ico{width:46px;height:46px;border-radius:13px;background:#FFF0E6;display:flex;align-items:center;justify-content:center}
.fi h3{font-size:18px;line-height:1.3;font-weight:700}
.fi .chev{display:none}
.fi p{font-size:15px;line-height:1.6;color:var(--mute);margin-top:8px}

/* compare */
.cmp{background:#fff;border-top:1px solid var(--line);border-bottom:1px solid var(--line)}
.cmp .wrap{padding-top:100px;padding-bottom:100px;display:flex;flex-direction:column;gap:36px}
.tbl{overflow-x:auto;border:1px solid var(--line);border-radius:22px}
.tbl table{width:100%;border-collapse:collapse;font-size:15.5px}
.tbl th,.tbl td{padding:18px 22px;text-align:left}
.tbl thead th{font-weight:700;border-bottom:1px solid var(--line);font-size:14px;color:var(--mute)}
.tbl tbody tr{border-bottom:1px solid #F0ECE6}.tbl tbody tr:last-child{border-bottom:0}
.tbl tbody th{font-weight:500}
.tbl .us{background:var(--ink);color:#fff;font-weight:600}
.tbl thead .us{color:var(--brand-l);font-family:var(--display);text-transform:uppercase;font-size:20px;letter-spacing:.02em}
.cmp-m{display:none;list-style:none;padding:0}

/* pricing */
.price{background:var(--cream)}
.price .wrap{padding-top:100px;padding-bottom:100px;display:flex;flex-direction:column;gap:40px}
.price-h{display:flex;flex-direction:column;gap:14px;max-width:780px}
.plans{display:grid;grid-template-columns:repeat(4,1fr);gap:16px;align-items:stretch}
.plan{border:1px solid var(--line);border-radius:24px;padding:28px;display:flex;flex-direction:column;gap:18px;background:#fff}
.plan.top{background:var(--ink);color:#fff;border:2px solid var(--brand);box-shadow:0 30px 60px -30px rgba(242,107,29,.6);transform:translateY(-10px)}
.plan.top ul{color:var(--td)}.plan.top .per{color:var(--md)}
.plan-h{display:flex;justify-content:space-between;align-items:center;gap:8px;flex-wrap:wrap}
.plan h3{font-family:var(--display);text-transform:uppercase;font-size:22px;font-weight:600;letter-spacing:.02em}
.badge2{font-size:11px;font-weight:800;color:#fff;background:var(--brand);padding:6px 10px;border-radius:999px;letter-spacing:.04em}
.amt{font-family:var(--display);font-size:58px;font-weight:700;line-height:1}
.per{color:var(--mute);font-weight:500}
.plan ul{padding-left:0;list-style:none;display:flex;flex-direction:column;gap:10px;font-size:15px;line-height:1.45;color:var(--t2);flex-grow:1}
.plan li{display:flex;gap:9px}
.plan li::before{content:"";width:16px;height:16px;flex:none;margin-top:2px;background:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='%23F26B1D' stroke-width='3' stroke-linecap='round' stroke-linejoin='round'%3E%3Cpath d='M5 12l5 5L20 7'/%3E%3C/svg%3E") center/contain no-repeat}
.plan .btn{width:100%;padding:15px;min-height:50px}
.swipe{display:none}
.guar{background:var(--ink);color:#fff;border-radius:22px;padding:24px 28px;display:flex;gap:16px;align-items:center}
.guar svg{flex:none}
.guar p{font-size:17px;line-height:1.5}
.guar strong{color:var(--brand-l)}
.note{font-size:13px;color:var(--mute)}

/* faq */
.faq{background:#fff;border-top:1px solid var(--line)}
.faq .wrap{max-width:920px;padding-top:100px;padding-bottom:100px;display:flex;flex-direction:column;gap:32px}
.faq-l{display:flex;flex-direction:column;gap:10px}
.qa{border:1px solid var(--line);border-radius:18px;background:var(--cream);transition:background .2s}
.qa[open]{background:#fff;box-shadow:0 14px 30px -22px rgba(13,17,23,.35)}
.qa summary{list-style:none;cursor:pointer;display:flex;justify-content:space-between;align-items:center;gap:16px;padding:20px 22px;min-height:60px}
.qa summary::-webkit-details-marker{display:none}
.qa h3{font-size:17.5px;line-height:1.35;font-weight:700}
.qa .chev{flex:none;transition:transform .2s}
.qa[open] .chev{transform:rotate(180deg)}
.qa p{font-size:16px;line-height:1.6;color:var(--mute);padding:0 22px 22px}

/* audit */
.audit{background:radial-gradient(700px 500px at 0% 0%,rgba(242,107,29,.22),transparent 60%),radial-gradient(600px 400px at 100% 100%,rgba(242,107,29,.12),transparent 60%),var(--ink);color:#fff}
.audit .wrap{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1fr);gap:56px;align-items:center;padding-top:110px;padding-bottom:110px}
.audit-l{display:flex;flex-direction:column;gap:20px}
.audit h2{font-family:var(--display);text-transform:uppercase;font-weight:700;font-size:clamp(36px,4.6vw,64px);line-height:1}
.audit-l p{font-size:18px;line-height:1.6;color:var(--td)}
.audit-l ul{list-style:none;padding:0;display:flex;flex-direction:column;gap:10px;font-size:16px;color:#fff}
.audit-l li{display:flex;gap:10px;align-items:center}
.audit-l li::before{content:"";width:20px;height:20px;flex:none;border-radius:20px;background:var(--brand) url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='white' stroke-width='3.5' stroke-linecap='round' stroke-linejoin='round'%3E%3Cpath d='M6 12l4 4 8-8'/%3E%3C/svg%3E") center/12px no-repeat}
form{background:#fff;color:var(--t);border-radius:26px;padding:30px;display:flex;flex-direction:column;gap:14px;box-shadow:0 50px 90px -30px rgba(0,0,0,.7)}
.f{display:flex;flex-direction:column;gap:6px}
.f label{font-size:13.5px;font-weight:700}
.f input,.f select{padding:13px 14px;border:1.5px solid #DCD6CC;border-radius:12px;font-size:16px;font-family:inherit;background:#fff;color:var(--t);min-height:50px;width:100%}
.f input:focus,.f select:focus{border-color:var(--brand);outline:none;box-shadow:0 0 0 4px rgba(242,107,29,.15)}
.f2{display:grid;grid-template-columns:1fr 1fr;gap:14px}
.chk{display:flex;gap:10px;align-items:flex-start}
.chk input{width:20px;height:20px;margin-top:2px;flex:none;accent-color:var(--brand)}
.chk label{font-size:12.5px;line-height:1.5;color:var(--mute)}
form button{background:var(--brand);color:#fff;border:none;padding:17px;border-radius:999px;font-size:17px;font-weight:700;font-family:inherit;cursor:pointer;min-height:56px;box-shadow:0 12px 30px -10px rgba(242,107,29,.8)}
form button:hover{background:#ff7a2c}
form button:disabled{opacity:.7;cursor:default}
#waitlist-ok{display:none;padding:14px 16px;border-radius:12px;background:#ECFDF3;color:#065F46;font-size:15px;font-weight:600}

/* footer */
.ftr{background:var(--ink);color:var(--md);border-top:1px solid var(--ld)}
.ftr .wrap{display:flex;flex-wrap:wrap;gap:20px;justify-content:space-between;align-items:center;font-size:13px;padding-top:34px;padding-bottom:44px}
.ftr a{color:var(--td)}
.ftr img{height:32px;width:auto}
.ftr p:last-child{max-width:560px}

.sticky{display:none}

/* tablet */
@media (max-width:1080px){
  .nav a.l{display:none}
  .hero .wrap,.pilot .wrap,.demo .wrap,.audit .wrap{grid-template-columns:minmax(0,1fr)}
  .vis{max-width:640px;width:100%;margin:0 auto}
  .tr-g{grid-template-columns:repeat(3,1fr)}
  .tr-more{min-height:60px}
  .plans{grid-template-columns:repeat(2,1fr)}
  .plan.top{transform:none}
}
/* mobile */
@media (max-width:760px){
  .wrap{padding:0 18px}
  .hdr .wrap{height:60px;gap:8px}
  .logo img{height:32px}
  .nav{gap:4px}
  .nav .btn{padding:9px 14px;font-size:13.5px;min-height:40px}
  .cta-full{display:none}.cta-short{display:inline}
  .lang summary{padding:8px;font-size:13px}

  .js .rv{opacity:1!important;transform:none!important;transition:none!important}
  .hero .wrap{display:flex;flex-direction:column;justify-content:center;min-height:calc(100svh - 60px);padding-top:20px;padding-bottom:24px;gap:0}
  .hero-l{gap:14px}
  .badge{font-size:12px;padding:5px 11px 5px 9px}
  .hero h1{font-size:clamp(34px,10.4vw,44px);line-height:.98}
  .hl{white-space:normal}
  .hero .sub{font-size:15.5px;line-height:1.5}
  .ctas{flex-direction:column;margin-top:2px}
  .ctas .btn{width:100%;min-height:52px;padding:14px 16px;font-size:15.5px;white-space:nowrap}
  .ctas .btn-ghost{display:none}
  .trust{font-size:12.5px;gap:4px 12px}
  .vis{display:none}
  .mproof{display:flex;align-items:center;gap:10px;background:rgba(255,255,255,.06);border:1px solid var(--ld);border-radius:16px;padding:10px 12px;margin-top:4px}
  .mproof .ic{width:34px;height:34px;border-radius:10px;background:var(--brand);display:flex;align-items:center;justify-content:center;flex:none}
  .mproof b{display:block;font-size:13.5px;color:#fff}
  .mproof small{font-size:12px;color:var(--md)}
  .mproof .tag{margin-left:auto;display:flex;align-items:center;gap:4px;font-size:11.5px;font-weight:600;color:var(--brand-l);white-space:nowrap}
}
@media (max-width:430px){
  .mproof .tag{display:none}
  .mproof small{white-space:nowrap;overflow:hidden;text-overflow:ellipsis;display:block}
}
@media (max-width:760px) and (max-height:720px){
  .hero .badge{display:none}
  .hero .sub{font-size:15px}
}
@media (max-width:760px) and (max-height:620px){
  .mproof{display:none}
  .hero h1{font-size:clamp(32px,9.6vw,40px)}
}
@media (max-width:760px){
  .vis{height:480px}
  .photo{width:84%;height:74%;border-radius:22px}
  .phone{width:224px;height:440px;border-radius:38px;padding:8px}
  .scr{border-radius:31px}
  .notch{width:76px;height:22px;top:6px}
  .ph-h{padding:34px 12px 9px}
  .av{width:30px;height:30px;font-size:13px}
  .ph-h b{font-size:12.5px}.ph-h small{font-size:10.5px}
  .bub{font-size:11.5px;padding:7px 10px}
  .notif{top:32px;padding:9px 10px}.notif b{font-size:12px}.notif small{font-size:11px}.notif .ic{width:28px;height:28px}
  .ph-in{font-size:11px;padding:8px 12px}
  .chip{font-size:12px;padding:8px 11px}
  .chip .dot{width:22px;height:22px}
  .chip.c1{top:4%;right:auto;left:30%}
  .chip.c2{display:none}
  .chip.c3{bottom:12%;right:2%}

  .trades{padding:24px 0 28px}
  .tr-g{display:flex;overflow-x:auto;scroll-snap-type:x mandatory;gap:10px;margin:0 -18px;padding:0 18px 4px;scrollbar-width:none}
  .tr-g::-webkit-scrollbar{display:none}
  .tr{flex:0 0 140px;height:96px;scroll-snap-align:start}
  .tr span{font-size:15px}
  .tr-more{flex:0 0 130px}

  .stats-g{grid-template-columns:max-content 1fr;gap:16px 16px;align-items:center;padding-top:30px;padding-bottom:12px}
  .stat{display:contents}
  .stat .n{font-size:32px;white-space:nowrap}
  .stat .t{font-size:14px;margin:0}
  .src{font-size:11px;padding-bottom:22px}

  .pilot .wrap{padding-top:52px;padding-bottom:52px;gap:28px}
  .h2{font-size:36px}
  .lead{font-size:16px}
  .pilot-g{gap:10px}
  .pc{padding:14px 15px;border-radius:14px}
  .pc .n{font-size:32px}
  .pc .t{font-size:13px}
  .case{padding:18px;border-radius:22px;gap:10px}
  .msg{padding:11px 13px}.msg b{font-size:14px}
  .msg:nth-of-type(4){display:none}
  .case-cap{display:none}

  .how .wrap{padding-top:52px;padding-bottom:52px;gap:24px}
  .steps{grid-template-columns:1fr;gap:20px}
  .steps::before{display:none}
  .step{flex-direction:row;gap:16px}
  .num{font-size:52px;-webkit-text-stroke-width:1.5px;padding-right:0;min-width:58px}
  .step h3{font-size:18px;margin-bottom:4px}
  .step p{font-size:15px}

  .demo .wrap{padding-top:52px;padding-bottom:52px;gap:24px}
  .qs{flex-direction:row;overflow-x:auto;margin:0 -18px;padding:0 18px 4px;scrollbar-width:none}
  .qs::-webkit-scrollbar{display:none}
  .q{flex:0 0 auto;width:auto;font-size:14px;padding:12px 14px;min-height:46px;white-space:nowrap}
  .q svg{display:none}
  .win{min-height:0;border-radius:20px}
  .log{padding:16px;height:300px}
  .log .bub{font-size:13.5px}
  .win-cta{padding:0 16px 16px}

  .feat .wrap{padding-top:52px;padding-bottom:52px;gap:16px}
  .feat-hint{display:block;font-size:13px;color:var(--mute)}
  .feat-g{grid-template-columns:1fr;gap:8px}
  .fi{padding:0 16px;border-radius:14px}
  .fi:hover{transform:none;box-shadow:none}
  .fi-h{flex-direction:row;align-items:center;cursor:pointer;padding:12px 0;min-height:56px;gap:12px}
  .fi p{display:none}
  .fi.open p{display:block}
  .ico{width:36px;height:36px;border-radius:10px;flex:none}
  .ico svg{width:20px;height:20px}
  .fi h3{font-size:15.5px;flex:1}
  .fi .chev{display:block;flex:none;transition:transform .2s}
  .fi.open .chev{transform:rotate(180deg)}
  .fi p{margin:0 0 14px 48px;font-size:14.5px}

  .cmp .wrap{padding-top:52px;padding-bottom:52px;gap:18px}
  .tbl{display:none}
  .cmp-m{display:block;border:1px solid var(--line);border-radius:18px;padding:0 16px;background:#fff}
  .cmp-m li{padding:13px 0;border-bottom:1px solid #F0ECE6}
  .cmp-m li:last-child{border-bottom:0}
  .cmp-m .q2{font-weight:700;font-size:14.5px}
  .cmp-m .us{margin-top:6px;font-size:14.5px;color:var(--brand-d);font-weight:700;display:flex;gap:6px;align-items:flex-start}
  .cmp-m .us svg{flex:none;margin-top:2px}
  .cmp-m .oth{margin-top:4px;font-size:12.5px;color:#7A828E}

  .price .wrap{padding-top:52px;padding-bottom:52px;gap:20px}
  .plans{display:flex;overflow-x:auto;scroll-snap-type:x mandatory;gap:12px;margin:0 -18px;padding:14px 18px 10px;scrollbar-width:none}
  .plans::-webkit-scrollbar{display:none}
  .plan{flex:0 0 84%;scroll-snap-align:center;padding:22px;gap:14px}
  .plan.top{transform:none}
  .amt{font-size:46px}
  .plan ul{font-size:14.5px;gap:8px}
  .swipe{display:flex;justify-content:center}
  .dots{display:flex;gap:6px;justify-content:center}
  .dots i{width:7px;height:7px;border-radius:9px;background:#D6D0C6;display:block;transition:width .2s}
  .dots i.on{background:var(--brand);width:20px}
  .guar{padding:16px 18px;align-items:flex-start;border-radius:18px}
  .guar p{font-size:15px}

  .faq .wrap{padding-top:52px;padding-bottom:52px;gap:18px}
  .qa summary{padding:15px 16px}
  .qa h3{font-size:15.5px}
  .qa p{font-size:15px;padding:0 16px 16px}

  .audit .wrap{padding-top:52px;padding-bottom:52px;gap:26px}
  .audit h2{font-size:38px}
  .audit-l p{font-size:16px}
  .audit-l ul{display:none}
  form{padding:20px;gap:12px;border-radius:20px}
  .f2{grid-template-columns:1fr;gap:12px}

  .ftr .wrap{flex-direction:column;align-items:flex-start;gap:12px;padding-bottom:100px}

  .sticky{display:block;position:fixed;left:0;right:0;bottom:0;z-index:30;padding:10px 16px calc(10px + env(safe-area-inset-bottom));background:rgba(13,17,23,.9);backdrop-filter:blur(12px);-webkit-backdrop-filter:blur(12px);border-top:1px solid var(--ld);transform:translateY(110%);transition:transform .25s}
  .sticky.on{transform:none}
  .sticky .btn{width:100%;min-height:50px;font-size:16px;padding:12px}
}
@media (prefers-reduced-motion:reduce){
  html{scroll-behavior:auto}
  *,*::before,*::after{animation:none!important;transition:none!important}
  .js .rv{opacity:1;transform:none}
}
"""

def head(L):
    url = BASE + L['path']
    alts = '\n'.join(f'<link rel="alternate" hreflang="{x["code"]}" href="{BASE}{x["path"]}">' for x in LANGS)
    alts += f'\n<link rel="alternate" hreflang="x-default" href="{BASE}/">'
    oglocs = '\n'.join(f'<meta property="og:locale:alternate" content="{x["og_locale"]}">' for x in LANGS if x is not L)
    ld = [
        {"@context": "https://schema.org", "@type": "Organization", "name": "ProsBros", "url": BASE, "logo": BASE + "/icon-512.png", "email": "hello@prosbros.app", "slogan": "Every Pro Needs a Bro", "parentOrganization": {"@type": "Organization", "name": "Flowsell, Inc."}},
        {"@context": "https://schema.org", "@type": "SoftwareApplication", "name": "ProsBros", "url": url, "inLanguage": L['code'], "applicationCategory": "BusinessApplication", "operatingSystem": "Web", "description": html.unescape(L['desc']),
         "offers": [{"@type": "Offer", "name": p['name'], "price": p['price'].strip('$'), "priceCurrency": "USD"} for p in L['plans']]},
        {"@context": "https://schema.org", "@type": "FAQPage", "inLanguage": L['code'], "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in L['faq']]},
    ]
    return f'''<!doctype html>
<html lang="{L['code']}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{L['title']}</title>
<meta name="description" content="{L['desc']}">
<link rel="canonical" href="{url}">
{alts}
<meta name="theme-color" content="#0D1117">
<link rel="icon" href="/favicon.ico" sizes="any">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
<link rel="manifest" href="/site.webmanifest">
<meta property="og:type" content="website">
<meta property="og:site_name" content="ProsBros">
<meta property="og:locale" content="{L['og_locale']}">
{oglocs}
<meta property="og:title" content="{L['title']}">
<meta property="og:description" content="{L['desc']}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{BASE}/og-image.png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{L['title']}">
<meta name="twitter:description" content="{L['desc']}">
<meta name="twitter:image" content="{BASE}/og-image.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="preconnect" href="https://images.unsplash.com" crossorigin>
<link rel="preload" as="image" href="{img(PHOTOS['hero'], 1100)}">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=Oswald:wght@500;600;700&display=swap">
<link rel="stylesheet" href="/assets/site.css?v=2">
<script>(function(d){{d.className+=' js fl';var done=function(){{d.className=d.className.replace(' fl','');}};if(document.fonts&&document.fonts.ready){{document.fonts.ready.then(done);}}setTimeout(done,900);}})(document.documentElement);</script>
<script type="application/ld+json">{json.dumps(ld, ensure_ascii=False)}</script>
{ph_snippet()}
<script>posthog.register({{site_lang:'{L['code']}',site_version:'v2'}});</script>
</head>
<body>
'''

def lang_menu(L):
    items = ''.join(
        f'<li><a href="{x["path"]}" hreflang="{x["code"]}" lang="{x["code"]}"{" aria-current=\"page\"" if x is L else ""} data-lang="{x["code"]}">{x["name"]}<span>{x["short"]}</span></a></li>'
        for x in LANGS)
    return f'<details class="lang"><summary aria-label="{L["lang_label"]}">{svg(GLOBE, 18, "currentColor")}{L["short"]}</summary><ul>{items}</ul></details>'

ARROW = '<path d="M5 12h14"/><path d="M13 6l6 6-6 6"/>'
PLAY = '<path d="M8 5v14l11-7z" fill="currentColor"/>'
CHECK = '<path d="M5 12l5 5L20 7"/>'
BOLT = '<path d="M13 2L4 14h7l-1 8 9-12h-7z"/>'
CAL = '<rect x="3" y="5" width="18" height="16" rx="2"/><path d="M3 10h18M8 3v4M16 3v4"/>'

def body(L):
    X = EXTRA[L['code']]
    chev = svg(CHEV, 20, '#8A9099')
    p = L['path']
    o = []
    o.append(f'''<header class="hdr"><div class="wrap">
<a class="logo" href="{p}" aria-label="ProsBros"><img src="/assets/logo-notag-dark.svg" alt="ProsBros" width="188" height="57"></a>
<nav class="nav" aria-label="Main">
<a class="l" href="#how">{L['nav'][0]}</a><a class="l" href="#pricing">{L['nav'][1]}</a><a class="l" href="#faq">{L['nav'][2]}</a>
{lang_menu(L)}
<a class="btn btn-brand" href="#audit"><span class="cta-full">{L['nav_cta']}</span><span class="cta-short">{L['nav_cta_short']}</span></a>
</nav></div></header>
<main>''')
    h1 = L['h1'].replace(X['h1_hl'], f'<span class="hl">{X["h1_hl"]}</span>', 1)
    trust = ''.join(f'<li>{t}</li>' for t in L['trust'])
    chat = ''
    for who, t in CHAT:
        chat += f'<div class="bub typing{" b" if who == "b" else ""}" aria-hidden="true"><i></i><i></i><i></i></div><div class="bub {"b" if who == "b" else "c"}">{html.escape(t)}</div>'
    o.append(f'''<section id="top" class="hero dark"><div class="wrap">
<div class="hero-l">
<span class="badge rv"><span class="pulse"></span>{X['badge']}</span>
<h1 class="rv d1">{h1}</h1>
<p class="sub rv d2">{L['sub']}</p>
<div class="ctas rv d3"><a class="btn btn-brand" href="#audit" id="hero-cta">{L['cta1']} {svg(ARROW, 18, '#fff')}</a><a class="btn btn-ghost" href="#demo">{svg(PLAY, 16, '#fff')} {X['cta2']}</a></div>
<ul class="trust rv d3">{trust}</ul>
<div class="mproof"><span class="ic">{svg(CAL, 18, '#fff')}</span><div><b>{X['notif_t']}</b><small>{X['notif_d']}</small></div><span class="tag">{svg(BOLT, 13, '#FFB27A')}{X['chip1']}</span></div>
</div>
<div class="vis rv d2" aria-hidden="true">
<div class="photo"><img src="{img(PHOTOS['hero'], 1100)}" alt="" width="900" height="1100" fetchpriority="high"></div>
<div class="phone"><div class="scr" id="phone">
<span class="notch"></span>
<div class="notif" id="notif"><span class="ic">{svg(CAL, 18, '#fff')}</span><div><b>{X['notif_t']}</b><small>{X['notif_d']}</small></div></div>
<div class="ph-h"><span class="av">S</span><div><b>{X['phone_name']}</b><small><i></i>{X['phone_status']}</small></div></div>
<div class="chat">{chat}</div>
<div class="ph-in">{X['phone_input']}</div>
</div></div>
<span class="chip c1"><span class="dot">{svg(BOLT, 15, '#FFB27A')}</span>{X['chip1']}</span>
<span class="chip c2"><span class="dot">{svg(ICONS[0], 15, '#FFB27A')}</span>{X['chip2']}</span>
<span class="chip c3"><span class="dot">{svg(CHECK, 15, '#fff')}</span>{X['chip3']}</span>
</div>
</div></section>''')
    keys = ['handyman', 'cleaning', 'moving', 'painting', 'plumbing', 'electrical']
    tr = ''.join(f'<li class="tr"><img src="{img(PHOTOS[k], 420, 300)}" alt="" loading="lazy" width="420" height="300"><span>{n}</span></li>' for k, n in zip(keys, X['trades']))
    o.append(f'<section class="trades"><div class="wrap"><h2>{X["trades_h"]}</h2><ul class="tr-g">{tr}<li class="tr-more">{X["trades_more"]}</li></ul></div></section>')
    stats = ''.join(f'<div class="stat rv{" d" + str(i) if i else ""}"><p class="n">{n}</p><p class="t">{t}</p></div>' for i, (n, t) in enumerate(L['stats']))
    o.append(f'<section class="stats dark"><div class="wrap stats-g">{stats}</div><p class="wrap src">{L["stats_src"]}</p></section>')
    pcs = ''.join(f'<div class="pc{" hot" if i == 3 else ""}"><p class="n">{n}</p><p class="t">{t}</p></div>' for i, (n, t) in enumerate(L['pilot']))
    msgs = ''.join(f'<div class="msg"><b>{q}</b><small>{m}</small></div>' for q, m in zip(QUOTES, L['inbox_meta']))
    o.append(f'''<section class="pilot"><div class="wrap">
<div class="pilot-l rv"><p class="eyebrow">{L['pilot_eyebrow']}</p><h2 class="h2">{L['pilot_h2']}</h2><p class="lead">{L['pilot_p']}</p><div class="pilot-g">{pcs}</div></div>
<div class="case rv d2"><div class="case-h"><p>{X['case_label']}</p><span class="pill">{L['inbox_badge']}</span></div>{msgs}
<div class="bell">{svg(ICONS[2], 20, '#F26B1D')}<p>{L['inbox_bell']}</p></div><p class="case-cap">{X['case_cap']}</p></div>
</div></section>''')
    steps = ''.join(f'<li class="step rv{" d" + str(i) if i else ""}"><span class="num">0{i+1}</span><div><h3>{t}</h3><p>{d}</p></div></li>' for i, (t, d) in enumerate(L['how']))
    o.append(f'<section id="how" class="how"><div class="wrap"><h2 class="h2 rv">{L["how_h2"]}</h2><ol class="steps">{steps}</ol></div></section>')
    qs = ''.join(f'<button type="button" class="q" data-i="{i}" aria-pressed="false">{html.escape(q)}{svg(ARROW, 18, "#fff")}</button>' for i, (q, a) in enumerate(DEMO))
    o.append(f'''<section id="demo" class="demo dark"><div class="wrap">
<div class="demo-l rv"><p class="eyebrow">{X['demo_eyebrow']}</p><h2 class="h2">{X['demo_h2']}</h2><p class="lead">{X['demo_p']}</p><p class="ctrl">{svg('<path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/><path d="M9 12l2 2 4-4"/>', 20, '#FFB27A')}{X['ctrl']}</p><div class="qs" role="group">{qs}</div><p class="demo-note">{X['demo_note']}</p></div>
<div class="win rv d2"><div class="win-h"><i></i><i></i><i></i><span>{X['demo_bro']}</span></div><div class="log" id="log" aria-live="polite"><p class="empty">{X['demo_start']}</p></div><div class="win-cta"><a class="btn btn-brand" href="#audit">{X['demo_cta']} {svg(ARROW, 18, '#fff')}</a></div></div>
</div></section>''')
    feats = ''.join(f'<div class="fi rv{" d" + str(i % 3) if i % 3 else ""}"><button type="button" class="fi-h" aria-expanded="false"><span class="ico">{svg(ICONS[i], 24)}</span><h3>{t}</h3><span class="chev">{chev}</span></button><p>{d}</p></div>' for i, (t, d) in enumerate(L['feat']))
    o.append(f'<section class="feat"><div class="wrap"><h2 class="h2 rv">{L["feat_h2"]}</h2><p class="feat-hint">{L["feat_hint"]}</p><div class="feat-g">{feats}</div></div></section>')
    c = L['cmp_cols']
    rows = ''.join(f'<tr><th scope="row">{r[0]}</th><td>{r[1]}</td><td>{r[2]}</td><td class="us">{r[3]}</td></tr>' for r in L['cmp_rows'])
    mrows = ''.join(f'<li><p class="q2">{r[0]}</p><p class="us">{svg(CHECK, 16)}<span>ProsBros: {r[3]}</span></p><p class="oth">{c[0]}: {r[1]} · {c[1]}: {r[2]}</p></li>' for r in L['cmp_rows'])
    o.append(f'''<section class="cmp"><div class="wrap"><h2 class="h2 rv">{L['cmp_h2']}</h2>
<div class="tbl rv"><table><thead><tr><th scope="col"></th><th scope="col">{c[0]}</th><th scope="col">{c[1]}</th><th scope="col" class="us">{c[2]}</th></tr></thead><tbody>{rows}</tbody></table></div>
<ul class="cmp-m">{mrows}</ul></div></section>''')
    plans = []
    for i, pl in enumerate(L['plans']):
        btn = {'free': 'btn-ink', 'top': 'btn-brand', 'plain': 'btn-line'}[pl['kind']]
        per = '' if pl['price'] == '$0' else f'<span class="per"> {L["per"]}</span>'
        badge = f'<span class="badge2">{pl["badge"]}</span>' if pl.get('badge') else ''
        items = ''.join(f'<li>{x}</li>' for x in pl['items'])
        plans.append(f'<div class="plan {pl["kind"]} rv{" d" + str(i) if i else ""}"{" data-top" if pl["kind"] == "top" else ""}><div class="plan-h"><h3>{pl["name"]}</h3>{badge}</div><p><span class="amt">{pl["price"]}</span>{per}</p><ul>{items}</ul><a class="btn {btn}" href="#audit">{pl["cta"]}</a></div>')
    dots = ''.join('<i></i>' for _ in L['plans'])
    o.append(f'''<section id="pricing" class="price"><div class="wrap">
<div class="price-h rv"><h2 class="h2">{L['price_h2']}</h2><p class="lead">{L['price_p']}</p></div>
<div class="plans" id="plans">{''.join(plans)}</div>
<div class="swipe"><div class="dots" id="dots">{dots}</div></div>
<div class="guar rv">{svg('<path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/><path d="M9 12l2 2 4-4"/>', 30, '#FFB27A')}<p>{L['guarantee']}</p></div>
<p class="note">{L['price_note']}</p>
</div></section>''')
    qas = ''.join(f'<details class="qa"{" open" if i == 0 else ""}><summary><h3>{q}</h3><span class="chev">{chev}</span></summary><p>{a}</p></details>' for i, (q, a) in enumerate(L['faq']))
    o.append(f'<section id="faq" class="faq"><div class="wrap"><h2 class="h2 rv">{L["faq_h2"]}</h2><div class="faq-l">{qas}</div></div></section>')
    al = ''.join(f'<li>{x}</li>' for x in L['audit_list'])
    opts = f'<option value="" selected>{X["f_choose"]}</option>' + ''.join(f'<option>{op}</option>' for op in L['f_opts'])
    o.append(f'''<section id="audit" class="audit"><div class="wrap">
<div class="audit-l rv"><h2>{L['audit_h2']}</h2><p>{L['audit_p']}</p><ul>{al}</ul></div>
<form id="waitlist" class="rv d2" aria-label="{L['f_btn']}" data-done="{L['f_done']}">
<div class="f"><label for="f-name">{L['f_name']}</label><input id="f-name" name="name" type="text" required autocomplete="name"></div>
<div class="f"><label for="f-biz">{L['f_biz']}</label><input id="f-biz" name="business" type="text" autocomplete="organization"></div>
<div class="f2"><div class="f"><label for="f-email">{L['f_email']}</label><input id="f-email" name="email" type="email" required autocomplete="email" inputmode="email"></div>
<div class="f"><label for="f-phone">{L['f_phone']}</label><input id="f-phone" name="phone" type="tel" autocomplete="tel" inputmode="tel"></div></div>
<div class="f"><label for="f-leads">{L['f_leads']}</label><select id="f-leads" name="leads_per_month">{opts}</select></div>
<div class="chk"><input id="f-sms" name="sms_opt_in" type="checkbox"><label for="f-sms">{L['f_sms']}</label></div>
<input type="text" name="website" tabindex="-1" autocomplete="off" aria-hidden="true" style="position:absolute;left:-9999px;width:1px;height:1px;opacity:0">
<button type="submit">{L['f_btn']}</button>
<p id="waitlist-ok" role="status">{L['f_ok']}</p>
</form></div></section>
</main>''')
    o.append(f'''<footer class="ftr"><div class="wrap">
<img src="/assets/logo-notag-dark.svg" alt="ProsBros" width="188" height="57">
<p>© 2026 ProsBros · <a href="/privacy">{L['privacy']}</a> · <a href="/terms">{L['terms']}</a>{L['legal_lang']} · <a href="mailto:hello@prosbros.app">hello@prosbros.app</a></p>
<p>{L['footer_legal']}</p>
</div></footer>
<div class="sticky" id="sticky" aria-hidden="true"><a class="btn btn-brand" href="#audit" tabindex="-1">{L['sticky']}</a></div>''')
    demo_json = json.dumps({'a': [a for q, a in DEMO], 'q': [q for q, a in DEMO], 't': X['demo_tags'], 'you': X['demo_you'], 'bro': X['demo_bro']}, ensure_ascii=False)
    o.append(f'<script id="demo-data" type="application/json">{demo_json}</script>')
    return '\n'.join(o)

JS = r"""<script>window.SIGNUP_URL='https://script.google.com/macros/s/AKfycbztYv8yAHyx6XuHL0YxAkPHzfOkV-wTxPOzFWAAKcNIBzgt4GQ1XJ9VNIGehiwFCas/exec';</script>
<script>
(function(){
// referral: ?ref=<code> is remembered on this device, shown as a banner for known partners, and sent with the signup
var PARTNERS={eduard:{n:'Eduard',b:'HandyGurus, Los Angeles'}};
var RT={en:'{n} ({b}) invited you: 14 days free + founding price $99/mo for life. First 20 pros only, until Dec 31.',
ru:'Вас пригласил {n} ({b}): 14 дней бесплатно + цена основателя $99/мес навсегда. Только первые 20 мастеров, до 31 декабря.',
es:'{n} ({b}) te invitó: 14 días gratis + precio de fundador $99/mes de por vida. Solo los primeros 20 pros, hasta el 31 de diciembre.',
uk:'Вас запросив {n} ({b}): 14 днів безкоштовно + ціна засновника $99/міс назавжди. Лише перші 20 майстрів, до 31 грудня.'};
var ref=null;
try{var m=location.search.match(/[?&]ref=([a-z0-9_-]{2,32})/i);if(m){ref=m[1].toLowerCase();try{localStorage.setItem('pb_ref',ref);}catch(e){}}else{try{ref=localStorage.getItem('pb_ref');}catch(e){}}}catch(e){}
window.PB_REF=ref;
if(ref){
 try{posthog.register({ref:ref});}catch(e){}
 document.querySelectorAll('.lang a').forEach(function(a){try{var u=new URL(a.getAttribute('href'),location.href);u.searchParams.set('ref',ref);a.setAttribute('href',u.pathname+u.search);}catch(e){}});
 var P=PARTNERS[ref];
 if(P){var lg=(document.documentElement.lang||'en').slice(0,2),bn=document.createElement('div');bn.className='refbar';bn.setAttribute('role','note');bn.textContent=(RT[lg]||RT.en).replace('{n}',P.n).replace('{b}',P.b);document.body.insertBefore(bn,document.body.firstChild);}
}
var reduce=window.matchMedia('(prefers-reduced-motion: reduce)').matches;
var mq=window.matchMedia('(max-width:760px)');
// reveal on scroll
var rv=[].slice.call(document.querySelectorAll('.rv'));
if('IntersectionObserver' in window&&!reduce){var io=new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting){e.target.classList.add('in');io.unobserve(e.target);}});},{rootMargin:'0px 0px -8% 0px'});rv.forEach(function(el){io.observe(el);});}else{rv.forEach(function(el){el.classList.add('in');});}
// hero phone chat loop
var ph=document.getElementById('phone');
if(ph){var bubs=[].slice.call(ph.querySelectorAll('.chat .bub')),nt=document.getElementById('notif');
 function reset(){bubs.forEach(function(b){b.classList.remove('on');});nt.classList.remove('on');}
 if(reduce){bubs.forEach(function(b){if(!b.classList.contains('typing'))b.classList.add('on');});nt.classList.add('on');}
 else{var run=function(){reset();var t=500;for(var i=0;i<bubs.length;i+=2){(function(ty,msg,at,isBro){setTimeout(function(){ty.classList.add('on');},at);setTimeout(function(){ty.classList.remove('on');msg.classList.add('on');},at+(isBro?1300:800));})(bubs[i],bubs[i+1],t,bubs[i+1].classList.contains('b'));t+=(bubs[i+1].classList.contains('b')?1300:800)+1200;}
   setTimeout(function(){nt.classList.add('on');},t);setTimeout(run,t+4200);};
   var started=false;new IntersectionObserver(function(e){if(e[0].isIntersecting&&!started){started=true;run();}}).observe(ph);}
}
// demo
var dd=JSON.parse(document.getElementById('demo-data').textContent),log=document.getElementById('log'),busy=false;
function bubble(cls,txt,who){var w=document.createElement('p');w.className='who'+(cls==='b'?' b':'');w.textContent=who;var b=document.createElement('div');b.className='bub '+cls;b.style.display='block';b.textContent=txt;log.appendChild(w);log.appendChild(b);return b;}
document.querySelectorAll('.q').forEach(function(btn){btn.addEventListener('click',function(){if(busy)return;busy=true;var i=+btn.dataset.i;
 document.querySelectorAll('.q').forEach(function(x){x.setAttribute('aria-pressed',x===btn?'true':'false');});
 log.innerHTML='';bubble('c',dd.q[i],dd.you);
 var ty=document.createElement('div');ty.className='bub typing b';ty.style.display='flex';ty.innerHTML='<i></i><i></i><i></i>';log.appendChild(ty);
 try{posthog.capture('demo_question',{i:i});}catch(e){}
 setTimeout(function(){ty.remove();var b=bubble('b','',dd.bro),s=dd.a[i],k=0;if(reduce){b.textContent=s;var t=document.createElement('p');t.className='rtag';t.textContent='✓ '+dd.t[i];log.appendChild(t);busy=false;return;}
   var tag=function(){var t=document.createElement('p');t.className='rtag';t.textContent='✓ '+dd.t[i];log.appendChild(t);};
   var iv=setInterval(function(){k+=3;b.textContent=s.slice(0,k);if(k>=s.length){clearInterval(iv);tag();busy=false;}},16);},reduce?0:1100);
});});
// features: tap to expand on phones only
document.querySelectorAll('.fi-h').forEach(function(b){b.addEventListener('click',function(){if(!mq.matches)return;var f=b.parentNode,o=f.classList.toggle('open');b.setAttribute('aria-expanded',o?'true':'false');});});
// pricing carousel
var pl=document.getElementById('plans'),dots=[].slice.call(document.querySelectorAll('#dots i'));
function syncDots(){var cards=[].slice.call(pl.children),c=pl.scrollLeft+pl.clientWidth/2,best=0,bd=1e9;cards.forEach(function(el,i){var m=el.offsetLeft+el.offsetWidth/2,d=Math.abs(m-c);if(d<bd){bd=d;best=i;}});dots.forEach(function(d,i){d.className=i===best?'on':'';});}
if(pl){if(mq.matches){var top=pl.querySelector('[data-top]');if(top){pl.scrollLeft=top.offsetLeft-(pl.clientWidth-top.offsetWidth)/2;}}syncDots();pl.addEventListener('scroll',function(){requestAnimationFrame(syncDots);},{passive:true});}
// sticky CTA
var st=document.getElementById('sticky'),hero=document.getElementById('hero-cta'),audit=document.getElementById('audit');
if(st&&'IntersectionObserver' in window){var heroOut=false,auditIn=false;function upd(){var on=heroOut&&!auditIn;st.classList.toggle('on',on);st.setAttribute('aria-hidden',on?'false':'true');st.querySelector('a').tabIndex=on?0:-1;}
new IntersectionObserver(function(e){heroOut=!e[0].isIntersecting&&e[0].boundingClientRect.top<0;upd();}).observe(hero);
new IntersectionObserver(function(e){auditIn=e[0].isIntersecting;upd();},{rootMargin:'0px 0px -30% 0px'}).observe(audit);}
// language menu
document.addEventListener('click',function(e){document.querySelectorAll('.lang[open]').forEach(function(d){if(!d.contains(e.target))d.open=false;});});
document.querySelectorAll('.lang a').forEach(function(a){a.addEventListener('click',function(){try{posthog.capture('language_switch',{to:a.dataset.lang});}catch(err){}});});
// waitlist
var f=document.getElementById('waitlist');
f.addEventListener('submit',function(e){e.preventDefault();var d={};new FormData(f).forEach(function(v,k){d[k]=v;});d.sms_opt_in=!!f.querySelector('#f-sms').checked;d.site_lang=document.documentElement.lang;
var payload=new URLSearchParams();Object.keys(d).forEach(function(k){payload.append(k,d[k]);});payload.append('page',location.href);payload.append('referrer',(ref?'ref:'+ref+(document.referrer?' | ':''):'')+(document.referrer||''));if(ref){d.ref=ref;}
if(window.SIGNUP_URL&&!d.website){try{fetch(window.SIGNUP_URL,{method:'POST',mode:'no-cors',body:payload,keepalive:true});}catch(err){}}
if(d.website){return;}
delete d.website;
try{posthog.identify(d.email,{email:d.email,name:d.name,business:d.business,phone:d.phone,leads_per_month:d.leads_per_month,sms_opt_in:d.sms_opt_in,site_lang:d.site_lang});posthog.capture('waitlist_signup',d);}catch(err){}
var b=f.querySelector('button[type=submit]');b.disabled=true;b.textContent=f.dataset.done;document.getElementById('waitlist-ok').style.display='block';});
document.querySelectorAll('a[href="#audit"]').forEach(function(a){a.addEventListener('click',function(){try{posthog.capture('cta_click',{label:a.textContent.trim()});}catch(err){}});});
})();
</script>"""

def build():
    os.makedirs(os.path.join(OUT, 'assets'), exist_ok=True)
    open(os.path.join(OUT, 'assets', 'site.css'), 'w').write(CSS.strip() + '\n')
    for L in LANGS:
        d = OUT if L['path'] == '/' else os.path.join(OUT, L['code'])
        os.makedirs(d, exist_ok=True)
        open(os.path.join(d, 'index.html'), 'w', encoding='utf-8').write(head(L) + body(L) + '\n' + JS + '\n</body>\n</html>\n')

if __name__ == '__main__':
    build()
    print('built v2')
