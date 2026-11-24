"""Builds the ProsBros landing in all languages into site/ (and site/<lang>/)."""
import json, os, re, html
from i18n import LANGS, QUOTES

OUT = os.path.join(os.path.dirname(__file__), 'site')
BASE = 'https://prosbros.app'
PH_KEY = 'phc_qAn2hvdsVW6jbmNr34Cai64jjH8Tg7cp7eCmxoNk42ak'

ICONS = [
    '<path d="M3 12a9 9 0 1 0 3-6.7"/><path d="M3 4v5h5"/>',
    '<path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/>',
    '<path d="M18 8a6 6 0 0 0-12 0c0 7-3 9-3 9h18s-3-2-3-9"/><path d="M13.7 21a2 2 0 0 1-3.4 0"/>',
    '<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>',
    '<rect x="6" y="2" width="12" height="20" rx="2"/><path d="M11 18h2"/>',
    '<path d="M3 3v18h18"/><path d="M7 15l4-4 3 3 5-6"/>',
    '<path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/>',
]
def svg(inner, size=24, color='#C2410C'):
    return f'<svg aria-hidden="true" width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="{color}" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">{inner}</svg>'

GLOBE = '<circle cx="12" cy="12" r="9"/><path d="M3 12h18"/><path d="M12 3a14 14 0 0 1 0 18a14 14 0 0 1 0-18z"/>'
CHEV = '<path d="M6 9l6 6 6-6"/>'

CSS = r"""
:root{--ink:#111827;--ink2:#374151;--mute:#4B5563;--line:#E5E2DC;--line2:#F1EEE9;--bg:#F7F6F3;--brand:#C2410C;--brand-d:#9A3412;--peach:#FFF7F1;--peach2:#FFF1E8;--display:'Space Grotesk',sans-serif}
*{box-sizing:border-box}
html{scroll-behavior:smooth;-webkit-text-size-adjust:100%}
body{margin:0;background:var(--bg);color:var(--ink);font-family:Inter,system-ui,sans-serif;line-height:1.5}
a{color:var(--brand)}a:hover{color:var(--brand-d)}
p,h1,h2,h3,ul{margin:0}
input:focus,select:focus,button:focus-visible,a:focus-visible,summary:focus-visible{outline:3px solid #FDBA74;outline-offset:2px}
.wrap{max-width:1200px;margin:0 auto;padding:0 24px}
.d{font-family:var(--display)}
.eyebrow{font-size:14px;font-weight:600;letter-spacing:.06em;text-transform:uppercase;color:var(--brand-d)}
.h2{font-family:var(--display);font-size:clamp(28px,3.6vw,44px);line-height:1.1;letter-spacing:-.01em}
.lead{font-size:18px;line-height:1.55;color:var(--ink2)}
.btn{display:inline-flex;align-items:center;justify-content:center;text-decoration:none;font-weight:600;border-radius:12px;padding:16px 24px;font-size:17px;min-height:52px;text-align:center}
.btn-brand{background:var(--brand);color:#fff}.btn-brand:hover{background:var(--brand-d);color:#fff}
.btn-dark{background:var(--ink);color:#fff}.btn-dark:hover{background:#000;color:#fff}
.btn-light{background:#fff;color:var(--ink);border:1px solid #D6D3CD}.btn-light:hover{color:var(--ink);border-color:#a8a29e}
.card{background:#fff;border:1px solid var(--line);border-radius:16px}
section{scroll-margin-top:12px}

/* header */
.hdr{border-bottom:1px solid var(--line);background:var(--bg)}
.hdr .wrap{display:flex;align-items:center;justify-content:space-between;gap:16px;padding-top:16px;padding-bottom:16px}
.logo img{height:44px;width:auto;display:block}
.nav{display:flex;align-items:center;gap:22px;font-size:15px}
.nav a.l{color:var(--ink2);text-decoration:none}.nav a.l:hover{color:var(--ink)}
.nav .btn{padding:11px 16px;font-size:15px;min-height:44px;border-radius:10px}
.cta-short{display:none}
.lang{position:relative}
.lang summary{list-style:none;cursor:pointer;display:flex;align-items:center;gap:6px;font-size:14px;font-weight:600;color:var(--ink2);padding:10px 8px;border-radius:8px;min-height:44px}
.lang summary::-webkit-details-marker{display:none}
.lang[open] summary,.lang summary:hover{background:#EFEDE8}
.lang ul{position:absolute;right:0;top:calc(100% + 6px);list-style:none;padding:6px;background:#fff;border:1px solid var(--line);border-radius:12px;box-shadow:0 12px 30px rgba(17,24,39,.12);min-width:170px;z-index:20}
.lang li a{display:flex;justify-content:space-between;gap:12px;padding:10px 12px;border-radius:8px;color:var(--ink);text-decoration:none;font-size:15px}
.lang li a:hover{background:var(--bg)}
.lang li a[aria-current]{font-weight:700;color:var(--brand-d)}
.lang li span{color:#9CA3AF;font-size:13px}

/* hero */
.hero{display:flex;flex-wrap:wrap;gap:48px;align-items:center;padding-top:72px;padding-bottom:64px}
.hero-l{flex:1 1 480px;min-width:0;display:flex;flex-direction:column;gap:24px}
.hero h1{font-family:var(--display);font-size:clamp(36px,5vw,60px);line-height:1.05;letter-spacing:-.02em}
.hero .sub{font-size:19px;line-height:1.55;color:var(--ink2);max-width:560px}
.ctas{display:flex;flex-wrap:wrap;gap:12px}
.trust{display:flex;flex-wrap:wrap;gap:6px 16px;font-size:14px;color:var(--mute);list-style:none;padding:0}
.trust li{display:flex;align-items:center;gap:6px}
.trust li::before{content:"";width:16px;height:16px;flex:none;background:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='%23C2410C' stroke-width='3' stroke-linecap='round' stroke-linejoin='round'%3E%3Cpath d='M5 12l5 5L20 7'/%3E%3C/svg%3E") center/contain no-repeat}
.hero-r{flex:1 1 420px;min-width:0}
.inbox{background:#fff;border:1px solid var(--line);border-radius:20px;padding:24px;box-shadow:0 20px 50px rgba(17,24,39,.08);display:flex;flex-direction:column;gap:14px}
.inbox-h{display:flex;justify-content:space-between;align-items:center;gap:12px}
.inbox-h p{font-weight:700;font-size:16px}
.pill{font-size:13px;font-weight:600;color:var(--brand-d);background:var(--peach2);padding:6px 10px;border-radius:999px;white-space:nowrap}
.msg{border:1px solid var(--line2);border-radius:12px;padding:14px 16px;display:flex;flex-direction:column;gap:6px}
.msg b{font-size:15px;font-weight:600}
.msg small{font-size:13px;color:var(--mute)}
.bell{background:var(--ink);color:#fff;border-radius:12px;padding:14px 16px;display:flex;gap:12px;align-items:center;font-size:14px;line-height:1.4}
.bell svg{flex:none}
.inbox-note{font-size:12px;color:#6B7280}

/* stats */
.stats{background:var(--ink);color:#fff}
.stats-g{display:grid;grid-template-columns:repeat(3,1fr);gap:32px;padding-top:56px;padding-bottom:24px}
.stat .n{font-family:var(--display);font-size:44px;font-weight:700;color:#FDBA74;line-height:1.1}
.stat .t{font-size:16px;line-height:1.5;color:#E5E7EB;margin-top:8px}
.src{font-size:12px;color:#9CA3AF;padding-bottom:32px}

/* pilot */
.pilot{padding-top:88px;padding-bottom:40px;display:flex;flex-direction:column;gap:32px}
.pilot-h{display:flex;flex-direction:column;gap:12px;max-width:760px}
.pilot-g{display:grid;grid-template-columns:repeat(4,1fr);gap:16px}
.pc{padding:24px;display:flex;flex-direction:column;gap:6px}
.pc .n{font-family:var(--display);font-size:40px;font-weight:700;line-height:1.1}
.pc .t{font-size:15px;color:var(--mute)}
.pc.hot{background:var(--peach2);border-color:#FED7AA}.pc.hot .n{color:var(--brand-d)}.pc.hot .t{color:#7C2D12}

/* how */
.how{padding-top:72px;padding-bottom:72px;display:flex;flex-direction:column;gap:32px}
.steps{display:grid;grid-template-columns:repeat(3,1fr);gap:20px;list-style:none;padding:0}
.step{padding:28px;display:flex;flex-direction:column;gap:12px}
.num{width:40px;height:40px;border-radius:999px;background:var(--ink);color:#fff;display:flex;align-items:center;justify-content:center;font-weight:700;flex:none}
.step:last-child .num{background:var(--brand)}
.step h3{font-size:21px;line-height:1.25}
.step p{font-size:16px;line-height:1.55;color:var(--mute)}

/* features */
.band{background:#fff;border-top:1px solid var(--line);border-bottom:1px solid var(--line)}
.feat{padding-top:80px;padding-bottom:80px;display:flex;flex-direction:column;gap:32px}
.feat-hint{display:none}
.feat-g{display:grid;grid-template-columns:repeat(auto-fit,minmax(300px,1fr));gap:28px 40px}
.fi summary{list-style:none;display:flex;gap:14px;align-items:flex-start}
.fi summary::-webkit-details-marker{display:none}
.fi summary svg{flex:none}
.fi h3{font-size:18px;line-height:1.3}
.fi .chev{display:none}
.fi p{font-size:15px;line-height:1.55;color:var(--mute);margin:6px 0 0 38px}

/* compare */
.cmp{padding-top:80px;padding-bottom:80px;display:flex;flex-direction:column;gap:28px}
.tbl{overflow-x:auto}
.tbl table{width:100%;border-collapse:collapse;font-size:15px}
.tbl th,.tbl td{padding:16px 20px;text-align:left}
.tbl thead th{padding:18px 20px;font-weight:600;border-bottom:1px solid var(--line)}
.tbl tbody tr{border-bottom:1px solid var(--line2)}.tbl tbody tr:last-child{border-bottom:0}
.tbl tbody th{font-weight:500}
.tbl .us{background:var(--peach);font-weight:600}.tbl thead .us{color:var(--brand-d);font-weight:700}
.cmp-m{display:none;list-style:none;padding:0}

/* pricing */
.price{padding-top:88px;padding-bottom:88px;display:flex;flex-direction:column;gap:32px}
.price-h{display:flex;flex-direction:column;gap:12px;max-width:760px}
.plans{display:grid;grid-template-columns:repeat(4,1fr);gap:20px;align-items:stretch}
.plan{border:1px solid var(--line);border-radius:18px;padding:28px;display:flex;flex-direction:column;gap:16px;background:#fff}
.plan.free{background:var(--bg)}
.plan.top{border:2px solid var(--brand);background:var(--peach)}
.plan-h{display:flex;justify-content:space-between;align-items:center;gap:8px;flex-wrap:wrap}
.plan h3{font-size:20px}
.badge{font-size:11px;font-weight:700;color:#fff;background:var(--brand-d);padding:5px 9px;border-radius:999px;letter-spacing:.02em}
.amt{font-family:var(--display);font-size:44px;font-weight:700;line-height:1}
.per{color:var(--mute)}
.plan ul{padding-left:20px;display:flex;flex-direction:column;gap:8px;font-size:15px;line-height:1.45;color:var(--ink2);flex-grow:1}
.plan .btn{padding:14px;font-size:16px;border-radius:10px;min-height:48px}
.swipe{display:none}
.guar{background:var(--ink);color:#fff;border-radius:16px;padding:22px 26px;display:flex;gap:14px;align-items:center}
.guar svg{flex:none}
.guar p{font-size:17px;line-height:1.5}
.note{font-size:13px;color:#6B7280}

/* faq */
.faq{max-width:900px;padding-top:88px;padding-bottom:88px;display:flex;flex-direction:column;gap:24px}
.faq-l{border-top:1px solid var(--line)}
.qa{border-bottom:1px solid var(--line)}
.qa summary{list-style:none;cursor:pointer;display:flex;justify-content:space-between;align-items:center;gap:16px;padding:20px 0;min-height:56px}
.qa summary::-webkit-details-marker{display:none}
.qa h3{font-size:18px;line-height:1.35}
.qa .chev{flex:none;transition:transform .2s}
.qa[open] .chev{transform:rotate(180deg)}
.qa p{font-size:16px;line-height:1.6;color:var(--mute);padding:0 0 22px}

/* audit */
.audit{background:var(--ink);color:#fff}
.audit .wrap{display:flex;flex-wrap:wrap;gap:48px;align-items:flex-start;padding-top:88px;padding-bottom:88px}
.audit-l{flex:1 1 420px;min-width:0;display:flex;flex-direction:column;gap:16px}
.audit h2{font-family:var(--display);font-size:clamp(28px,4vw,48px);line-height:1.08}
.audit-l p{font-size:18px;line-height:1.55;color:#D1D5DB}
.audit-l ul{padding-left:20px;display:flex;flex-direction:column;gap:8px;font-size:16px;color:#E5E7EB}
form{flex:1 1 420px;min-width:0;background:#fff;color:var(--ink);border-radius:18px;padding:28px;display:flex;flex-direction:column;gap:14px}
.f{display:flex;flex-direction:column;gap:6px}
.f label{font-size:14px;font-weight:600}
.f input,.f select{padding:13px 14px;border:1px solid #C9C5BE;border-radius:10px;font-size:16px;font-family:inherit;background:#fff;color:var(--ink);min-height:48px;width:100%}
.f2{display:grid;grid-template-columns:1fr 1fr;gap:14px}
.chk{display:flex;gap:10px;align-items:flex-start}
.chk input{width:20px;height:20px;margin-top:2px;flex:none}
.chk label{font-size:13px;line-height:1.5;color:var(--mute)}
form button{background:var(--brand);color:#fff;border:none;padding:16px;border-radius:12px;font-size:17px;font-weight:600;font-family:inherit;cursor:pointer;min-height:52px}
form button:hover{background:var(--brand-d)}
form button:disabled{opacity:.7;cursor:default}
#waitlist-ok{display:none;padding:14px 16px;border-radius:10px;background:#ECFDF3;color:#065F46;font-size:15px;font-weight:600}

/* footer */
.ftr{display:flex;flex-wrap:wrap;gap:16px;justify-content:space-between;font-size:13px;color:var(--mute);padding-top:32px;padding-bottom:48px}
.ftr p:last-child{max-width:560px}

/* sticky mobile CTA */
.sticky{display:none}

/* ---------- tablet ---------- */
@media (max-width:1024px){
  .plans{grid-template-columns:repeat(2,1fr)}
  .pilot-g{grid-template-columns:repeat(2,1fr)}
  .nav a.l{display:none}
}
/* ---------- mobile ---------- */
@media (max-width:760px){
  .wrap{padding:0 16px}
  .hdr .wrap{padding-top:10px;padding-bottom:10px;gap:8px}
  .logo img{height:34px}
  .nav{gap:4px}
  .nav .btn{padding:9px 12px;font-size:14px;min-height:40px}
  .cta-full{display:none}.cta-short{display:inline}
  .lang summary{padding:8px 6px;font-size:13px}

  .hero{padding-top:28px;padding-bottom:36px;gap:28px}
  .hero-l{gap:16px}
  .eyebrow{font-size:12px;letter-spacing:.04em}
  .eyebrow .tg{display:none}
  .hero h1{font-size:34px}
  .hero .sub{font-size:16.5px}
  .ctas{flex-direction:column;gap:10px}
  .ctas .btn{width:100%}
  .ctas .btn-light{display:none}
  .trust{font-size:13px;gap:4px 12px}
  .inbox{padding:16px;gap:10px;border-radius:16px}
  .msg{padding:11px 13px}
  .msg:nth-of-type(4){display:none}
  .inbox-note{display:none}

  .stats-g{grid-template-columns:max-content 1fr;gap:14px 14px;align-items:center;padding-top:28px;padding-bottom:12px}
  .stat{display:contents}
  .stat .n{font-size:24px;white-space:nowrap}
  .stat .t{font-size:14px;margin:0;color:#D1D5DB}
  .src{font-size:11px;padding-bottom:20px}

  .pilot{padding-top:44px;padding-bottom:12px;gap:20px}
  .lead{font-size:16px}
  .pilot-g{gap:10px}
  .pc{padding:14px;border-radius:12px}
  .pc .n{font-size:28px}
  .pc .t{font-size:13px;line-height:1.4}

  .how{padding-top:44px;padding-bottom:44px;gap:20px}
  .steps{grid-template-columns:1fr;gap:0}
  .step{flex-direction:row;gap:14px;padding:16px 0;background:none;border:0;border-radius:0;border-bottom:1px solid var(--line)}
  .step:last-child{border-bottom:0}
  .step h3{font-size:17px;margin-bottom:4px}
  .step p{font-size:15px}
  .num{width:32px;height:32px;font-size:14px}

  .feat{padding-top:44px;padding-bottom:44px;gap:14px}
  .feat-hint{display:block;font-size:13px;color:#6B7280}
  .feat-g{grid-template-columns:1fr;gap:0;border-top:1px solid var(--line)}
  .fi{border-bottom:1px solid var(--line)}
  .fi summary{cursor:pointer;align-items:center;padding:14px 0;min-height:52px}
  .fi h3{font-size:16px;flex:1}
  .fi .chev{display:block;flex:none;transition:transform .2s}
  .fi[open] .chev{transform:rotate(180deg)}
  .fi p{margin:0 0 14px 38px;font-size:14.5px}

  .cmp{padding-top:44px;padding-bottom:44px;gap:16px}
  .tbl{display:none}
  .cmp-m{display:block;background:#fff;border:1px solid var(--line);border-radius:16px;padding:0 16px}
  .cmp-m li{padding:13px 0;border-bottom:1px solid var(--line2);background:none;border-radius:0;border-left:0;border-right:0;border-top:0}
  .cmp-m li:last-child{border-bottom:0}
  .cmp-m .q{font-weight:600;font-size:14.5px}
  .cmp-m .us{margin-top:6px;font-size:15px;color:var(--brand-d);font-weight:600;display:flex;gap:6px;align-items:flex-start}
  .cmp-m .us svg{flex:none;margin-top:2px}
  .cmp-m .oth{margin-top:4px;font-size:13px;color:#6B7280}

  .price{padding-top:44px;padding-bottom:44px;gap:18px}
  .plans{display:flex;overflow-x:auto;scroll-snap-type:x mandatory;gap:12px;margin:0 -16px;padding:4px 16px 8px;scrollbar-width:none}
  .plans::-webkit-scrollbar{display:none}
  .plan{flex:0 0 84%;scroll-snap-align:center;padding:22px;gap:12px}
  .amt{font-size:38px}
  .plan ul{font-size:14.5px;gap:6px}
  .swipe{display:flex;justify-content:center;gap:6px;align-items:center;font-size:13px;color:#6B7280}
  .dots{display:flex;gap:6px;justify-content:center}
  .dots i{width:7px;height:7px;border-radius:9px;background:#D6D3CD;display:block}
  .dots i.on{background:var(--brand);width:18px}
  .guar{padding:16px 18px;align-items:flex-start}
  .guar p{font-size:15px}

  .faq{padding-top:44px;padding-bottom:44px;gap:12px}
  .qa summary{padding:16px 0}
  .qa h3{font-size:16px}
  .qa p{font-size:15px;padding-bottom:16px}

  .audit .wrap{padding-top:44px;padding-bottom:44px;gap:24px}
  .audit-l p{font-size:16px}
  .audit-l ul{display:none}
  form{padding:18px;gap:12px;border-radius:16px}
  .f2{grid-template-columns:1fr;gap:12px}

  .ftr{flex-direction:column;gap:10px;padding-bottom:96px}

  .sticky{display:block;position:fixed;left:0;right:0;bottom:0;z-index:30;padding:10px 16px calc(10px + env(safe-area-inset-bottom));background:rgba(247,246,243,.96);backdrop-filter:blur(8px);border-top:1px solid var(--line);transform:translateY(110%);transition:transform .25s}
  .sticky.on{transform:none}
  .sticky .btn{width:100%;min-height:50px;font-size:16px;padding:12px}
}
@media (prefers-reduced-motion:reduce){html{scroll-behavior:auto}.sticky,.qa .chev,.fi .chev{transition:none}}
"""

def ph_snippet():
    return ('<script>\n!function(t,e){var o,n,p,r;e.__SV||(window.posthog=e,e._i=[],e.init=function(i,s,a){function g(t,e){var o=e.split(".");2==o.length&&(t=t[o[0]],e=o[1]),t[e]=function(){t.push([e].concat(Array.prototype.slice.call(arguments,0)))}}(p=t.createElement("script")).type="text/javascript",p.crossOrigin="anonymous",p.async=!0,p.src=s.api_host.replace(".i.posthog.com","-assets.i.posthog.com")+"/static/array.js",(r=t.getElementsByTagName("script")[0]).parentNode.insertBefore(p,r);var u=e;for(void 0!==a?u=e[a]=[]:a="posthog",u.people=u.people||[],u.toString=function(t){var e="posthog";return"posthog"!==a&&(e+="."+a),t||(e+=" (stub)"),e},u.people.toString=function(){return u.toString(1)+".people (stub)"},o="init capture register register_once register_for_session unregister unregister_for_session getFeatureFlag getFeatureFlagPayload isFeatureEnabled reloadFeatureFlags updateEarlyAccessFeatureEnrollment getEarlyAccessFeatures on onFeatureFlags onSessionId getSurveys getActiveMatchingSurveys renderSurvey canRenderSurvey getNextSurveyStep identify setPersonProperties group resetGroups setPersonPropertiesForFlags resetPersonPropertiesForFlags setGroupPropertiesForFlags resetGroupPropertiesForFlags reset get_distinct_id getGroups get_session_id get_session_replay_url alias set_config startSessionRecording stopSessionRecording sessionRecordingStarted captureException loadToolbar get_property getSessionProperty createPersonProfile opt_in_capturing opt_out_capturing has_opted_in_capturing has_opted_out_capturing clear_opt_in_out_capturing debug".split(" "),n=0;n<o.length;n++)g(u,o[n]);e._i.push([i,s,a])},e.__SV=1)}(document,window.posthog||[]);\n'
            f"posthog.init('{PH_KEY}',{{api_host:'https://us.i.posthog.com',person_profiles:'identified_only'}});\n</script>")

def head(L):
    url = BASE + L['path']
    alts = '\n'.join(f'<link rel="alternate" hreflang="{x["code"]}" href="{BASE}{x["path"]}">' for x in LANGS)
    alts += f'\n<link rel="alternate" hreflang="x-default" href="{BASE}/">'
    oglocs = '\n'.join(f'<meta property="og:locale:alternate" content="{x["og_locale"]}">' for x in LANGS if x is not L)
    fonts = 'family=Inter:wght@400;500;600;700&family=Space+Grotesk:wght@500;600;700'
    if L['display_font'] != "'Space Grotesk'":
        fonts += '&family=Manrope:wght@600;700;800'
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
<meta name="theme-color" content="#111827">
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
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?{fonts}&display=swap">
<link rel="stylesheet" href="/assets/site.css">
<style>:root{{--display:{L['display_font']},sans-serif}}</style>
<script type="application/ld+json">{json.dumps(ld, ensure_ascii=False)}</script>
{ph_snippet()}
<script>posthog.register({{site_lang:'{L['code']}'}});</script>
</head>
<body>
'''

def lang_menu(L):
    items = ''.join(
        f'<li><a href="{x["path"]}" hreflang="{x["code"]}" lang="{x["code"]}"{" aria-current=\"page\"" if x is L else ""} data-lang="{x["code"]}">{x["name"]}<span>{x["short"]}</span></a></li>'
        for x in LANGS)
    return f'<details class="lang"><summary aria-label="{L["lang_label"]}">{svg(GLOBE, 18, "currentColor")}{L["short"]}</summary><ul>{items}</ul></details>'

def body(L):
    chev = svg(CHEV, 20, '#6B7280')
    p = L['path']
    out = []
    out.append(f'''<header class="hdr"><div class="wrap">
<a class="logo" href="{p}" aria-label="ProsBros"><img src="/assets/logo-notag.svg" alt="ProsBros" width="188" height="57"></a>
<nav class="nav" aria-label="Main">
<a class="l" href="#how">{L['nav'][0]}</a><a class="l" href="#pricing">{L['nav'][1]}</a><a class="l" href="#faq">{L['nav'][2]}</a>
{lang_menu(L)}
<a class="btn btn-dark" href="#audit"><span class="cta-full">{L['nav_cta']}</span><span class="cta-short">{L['nav_cta_short']}</span></a>
</nav></div></header>
<main>''')
    msgs = ''.join(f'<div class="msg"><b>{q}</b><small>{m}</small></div>' for q, m in zip(QUOTES, L['inbox_meta']))
    trust = ''.join(f'<li>{t}</li>' for t in L['trust'])
    tg, aud = L['eyebrow'].split(' · ', 1)
    eyebrow = f'<span class="tg">{tg} · </span>{aud}'
    out.append(f'''<section id="top" class="wrap hero">
<div class="hero-l">
<p class="eyebrow">{eyebrow}</p>
<h1>{L['h1']}</h1>
<p class="sub">{L['sub']}</p>
<div class="ctas"><a class="btn btn-brand" href="#audit" id="hero-cta">{L['cta1']}</a><a class="btn btn-light" href="#how">{L['cta2']}</a></div>
<ul class="trust">{trust}</ul>
</div>
<div class="hero-r"><div class="inbox" lang="{L['code']}">
<div class="inbox-h"><p>{L['inbox_title']}</p><span class="pill">{L['inbox_badge']}</span></div>
{msgs}
<div class="bell">{svg(ICONS[2], 20, '#FDBA74')}<p>{L['inbox_bell']}</p></div>
<p class="inbox-note">{L['inbox_note']}</p>
</div></div>
</section>''')
    stats = ''.join(f'<div class="stat"><p class="n">{n}</p><p class="t">{t}</p></div>' for n, t in L['stats'])
    out.append(f'<section class="stats"><div class="wrap stats-g">{stats}</div><p class="wrap src">{L["stats_src"]}</p></section>')
    pcs = ''.join(f'<div class="card pc{" hot" if i == 3 else ""}"><p class="n">{n}</p><p class="t">{t}</p></div>' for i, (n, t) in enumerate(L['pilot']))
    out.append(f'''<section class="wrap pilot">
<div class="pilot-h"><p class="eyebrow">{L['pilot_eyebrow']}</p><h2 class="h2">{L['pilot_h2']}</h2><p class="lead">{L['pilot_p']}</p></div>
<div class="pilot-g">{pcs}</div>
</section>''')
    steps = ''.join(f'<li class="card step"><span class="num">{i+1}</span><div><h3>{t}</h3><p>{d}</p></div></li>' for i, (t, d) in enumerate(L['how']))
    out.append(f'<section id="how" class="wrap how"><h2 class="h2">{L["how_h2"]}</h2><ol class="steps">{steps}</ol></section>')
    feats = ''.join(f'<details class="fi" open><summary>{svg(ICONS[i])}<h3>{t}</h3><span class="chev">{chev}</span></summary><p>{d}</p></details>' for i, (t, d) in enumerate(L['feat']))
    out.append(f'<section class="band"><div class="wrap feat"><h2 class="h2">{L["feat_h2"]}</h2><p class="feat-hint">{L["feat_hint"]}</p><div class="feat-g">{feats}</div></div></section>')
    c = L['cmp_cols']
    rows = ''.join(f'<tr><th scope="row">{r[0]}</th><td>{r[1]}</td><td>{r[2]}</td><td class="us">{r[3]}</td></tr>' for r in L['cmp_rows'])
    check = svg('<path d="M5 12l5 5L20 7"/>', 16)
    mrows = ''.join(f'<li><p class="q">{r[0]}</p><p class="us">{check}<span>ProsBros: {r[3]}</span></p><p class="oth">{c[0]}: {r[1]} · {c[1]}: {r[2]}</p></li>' for r in L['cmp_rows'])
    out.append(f'''<section class="wrap cmp"><h2 class="h2">{L['cmp_h2']}</h2>
<div class="card tbl"><table><thead><tr><th scope="col"></th><th scope="col">{c[0]}</th><th scope="col">{c[1]}</th><th scope="col" class="us">{c[2]}</th></tr></thead><tbody>{rows}</tbody></table></div>
<ul class="cmp-m">{mrows}</ul></section>''')
    plans = []
    for pl in L['plans']:
        btn = {'free': 'btn-dark', 'top': 'btn-brand', 'plain': 'btn-light'}[pl['kind']]
        per = '' if pl['price'] == '$0' else f'<span class="per"> {L["per"]}</span>'
        badge = f'<span class="badge">{pl["badge"]}</span>' if pl.get('badge') else ''
        items = ''.join(f'<li>{x}</li>' for x in pl['items'])
        plans.append(f'<div class="plan {pl["kind"]}"{" data-top" if pl["kind"] == "top" else ""}><div class="plan-h"><h3>{pl["name"]}</h3>{badge}</div><p><span class="amt">{pl["price"]}</span>{per}</p><ul>{items}</ul><a class="btn {btn}" href="#audit">{pl["cta"]}</a></div>')
    dots = ''.join('<i></i>' for _ in L['plans'])
    out.append(f'''<section id="pricing" class="band"><div class="wrap price">
<div class="price-h"><h2 class="h2">{L['price_h2']}</h2><p class="lead">{L['price_p']}</p></div>
<div class="plans" id="plans">{''.join(plans)}</div>
<div class="swipe"><div class="dots" id="dots">{dots}</div></div>
<div class="guar">{svg('<path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/><path d="M9 12l2 2 4-4"/>', 26, '#FDBA74')}<p>{L['guarantee']}</p></div>
<p class="note">{L['price_note']}</p>
</div></section>''')
    qas = ''.join(f'<details class="qa"{" open" if i == 0 else ""}><summary><h3>{q}</h3><span class="chev">{chev}</span></summary><p>{a}</p></details>' for i, (q, a) in enumerate(L['faq']))
    out.append(f'<section id="faq" class="wrap faq"><h2 class="h2">{L["faq_h2"]}</h2><div class="faq-l">{qas}</div></section>')
    al = ''.join(f'<li>{x}</li>' for x in L['audit_list'])
    opts = ''.join(f'<option>{o}</option>' for o in L['f_opts'])
    out.append(f'''<section id="audit" class="audit"><div class="wrap">
<div class="audit-l"><h2>{L['audit_h2']}</h2><p>{L['audit_p']}</p><ul>{al}</ul></div>
<form id="waitlist" aria-label="{L['f_btn']}" data-done="{L['f_done']}">
<div class="f"><label for="f-name">{L['f_name']}</label><input id="f-name" name="name" type="text" required autocomplete="name"></div>
<div class="f"><label for="f-biz">{L['f_biz']}</label><input id="f-biz" name="business" type="text" autocomplete="organization"></div>
<div class="f2"><div class="f"><label for="f-email">{L['f_email']}</label><input id="f-email" name="email" type="email" required autocomplete="email" inputmode="email"></div>
<div class="f"><label for="f-phone">{L['f_phone']}</label><input id="f-phone" name="phone" type="tel" autocomplete="tel" inputmode="tel"></div></div>
<div class="f"><label for="f-leads">{L['f_leads']}</label><select id="f-leads" name="leads_per_month">{opts}</select></div>
<div class="chk"><input id="f-sms" name="sms_opt_in" type="checkbox"><label for="f-sms">{L['f_sms']}</label></div>
<button type="submit">{L['f_btn']}</button>
<p id="waitlist-ok" role="status">{L['f_ok']}</p>
</form></div></section>
</main>''')
    ll = L['legal_lang']
    out.append(f'''<footer class="wrap ftr">
<p>© 2026 ProsBros · <a href="/privacy">{L['privacy']}</a> · <a href="/terms">{L['terms']}</a>{ll} · <a href="mailto:hello@prosbros.app">hello@prosbros.app</a></p>
<p>{L['footer_legal']}</p>
</footer>
<div class="sticky" id="sticky" aria-hidden="true"><a class="btn btn-brand" href="#audit" tabindex="-1">{L['sticky']}</a></div>''')
    return '\n'.join(out)

JS = r"""<script>
(function(){
var mq=window.matchMedia('(max-width:760px)');
// features: open on desktop, collapsed on mobile
function feats(){document.querySelectorAll('.fi').forEach(function(d){d.open=!mq.matches;});}
feats(); mq.addEventListener&&mq.addEventListener('change',feats);
document.querySelectorAll('.fi summary').forEach(function(s){s.addEventListener('click',function(e){if(!mq.matches)e.preventDefault();});});
// pricing carousel: start on the most picked plan, sync dots
var pl=document.getElementById('plans'),dots=[].slice.call(document.querySelectorAll('#dots i'));
function syncDots(){var cards=[].slice.call(pl.children),c=pl.scrollLeft+pl.clientWidth/2,best=0,bd=1e9;cards.forEach(function(el,i){var m=el.offsetLeft+el.offsetWidth/2,d=Math.abs(m-c);if(d<bd){bd=d;best=i;}});dots.forEach(function(d,i){d.className=i===best?'on':'';});}
if(pl){ if(mq.matches){var top=pl.querySelector('[data-top]'); if(top){pl.scrollLeft=top.offsetLeft-(pl.clientWidth-top.offsetWidth)/2;}} syncDots(); pl.addEventListener('scroll',function(){window.requestAnimationFrame(syncDots);},{passive:true}); }
// sticky CTA: show after the hero button scrolls away, hide near the form
var st=document.getElementById('sticky'),hero=document.getElementById('hero-cta'),audit=document.getElementById('audit');
if(st&&'IntersectionObserver' in window){var heroOut=false,auditIn=false;function upd(){var on=heroOut&&!auditIn;st.classList.toggle('on',on);st.setAttribute('aria-hidden',on?'false':'true');st.querySelector('a').tabIndex=on?0:-1;}
new IntersectionObserver(function(e){heroOut=!e[0].isIntersecting&&e[0].boundingClientRect.top<0;upd();}).observe(hero);
new IntersectionObserver(function(e){auditIn=e[0].isIntersecting;upd();},{rootMargin:'0px 0px -30% 0px'}).observe(audit);}
// close language menu on outside click
document.addEventListener('click',function(e){document.querySelectorAll('.lang[open]').forEach(function(d){if(!d.contains(e.target))d.open=false;});});
document.querySelectorAll('.lang a').forEach(function(a){a.addEventListener('click',function(){try{posthog.capture('language_switch',{to:a.dataset.lang});}catch(err){}});});
// waitlist
var f=document.getElementById('waitlist');
f.addEventListener('submit',function(e){e.preventDefault();var d={};new FormData(f).forEach(function(v,k){d[k]=v;});d.sms_opt_in=!!f.querySelector('#f-sms').checked;d.site_lang=document.documentElement.lang;
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
    # sitemap with hreflang alternates
    alts = ''.join(f'<xhtml:link rel="alternate" hreflang="{x["code"]}" href="{BASE}{x["path"]}"/>' for x in LANGS) + f'<xhtml:link rel="alternate" hreflang="x-default" href="{BASE}/"/>'
    urls = ''.join(f'<url><loc>{BASE}{x["path"]}</loc><lastmod>2026-11-24</lastmod>{alts}</url>\n' for x in LANGS)
    urls += f'<url><loc>{BASE}/privacy</loc><lastmod>2026-11-24</lastmod></url>\n<url><loc>{BASE}/terms</loc><lastmod>2026-11-24</lastmod></url>\n'
    open(os.path.join(OUT, 'sitemap.xml'), 'w').write(f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">\n{urls}</urlset>\n')

if __name__ == '__main__':
    build()
    print('built')
