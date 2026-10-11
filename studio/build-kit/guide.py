import re, html, pathlib
E=html.escape
P=pathlib.Path('/home/claude/studio')
def blocks(md):
    out=[]
    for m in re.finditer(r"^## (\S+) (.+?)\n\n(?:\((.*?)\))?\s*(?:_(.*?)_)?\s*```\n(.*?)\n```\n(?:\n\*\*Check:\*\* (.*?)\n)?",md,re.S|re.M):
        out.append(dict(id=m.group(1),title=m.group(2).strip(),tag=m.group(3),when=m.group(4),body=m.group(5),check=m.group(6)))
    return out
smd=(P/'stitch/STITCH-PROMPTS.md').read_text(); cmd=(P/'claude-code/BUILD-PROMPTS.md').read_text()
ds=re.search(r"## Design system \(paste first\)\n\n```\n(.*?)\n```",smd,re.S).group(1)
S=[]
for m in re.finditer(r"^## (S\d+) (.+?) \((.+?)\)\n\n```\n(.*?)\n```",smd,re.S|re.M): S.append(dict(id=m.group(1),title=m.group(2),tag=m.group(3),body=m.group(4)))
C=[];IT=[]
main,iter_=cmd.split("# Iteration prompts")
for m in re.finditer(r"^## (CC\d+) (.+?)\n\n(?:_(.+?)_\n\n)?```\n(.*?)\n```\n\n\*\*Check:\*\* (.+?)\n",main,re.S|re.M): C.append(dict(id=m.group(1),title=m.group(2),when=m.group(3),body=m.group(4),check=m.group(5)))
for i,m in enumerate(re.finditer(r"^## (.+?)\n\n```\n(.*?)\n```",iter_,re.S|re.M),1): IT.append(dict(id=f"IT{i}",title=m.group(1),body=m.group(2)))
plan=[l.split('|')[1:-1] for l in (P/'docs/BUILD-PLAN.md').read_text().split('\n') if re.match(r'\| \d',l)]
rmd=(P/'docs/RESEARCH.md').read_text()
research=[l.split('|')[1:-1] for l in rmd.split('\n') if re.match(r'\| \d+ \|',l)]
steps=[l.strip() for l in (P/'README.md').read_text().split('\n')]
STEPS=[];cur=None
for l in steps:
    if l.startswith('## ') and STEPS: cur=None
    if l.startswith('### '): cur=(re.sub(r'^### \d+\. ','',l),[]);STEPS.append(cur)
    elif l.startswith('- ') and cur and len(STEPS)<=6: cur[1].append(l[2:])
STEPS=STEPS[:6]
def plate(pid,title,sub,body,check=None,tag=None):
    return f'''<article class="pc" id="{pid}"><header><div><span class="pid">{E(pid)}</span><h4>{E(title)}</h4>{f'<p class="sub">{E(sub)}</p>' if sub else ''}</div>{f'<span class="dev">{E(tag)}</span>' if tag else ''}</header>
<div class="plate"><button class="cp" data-copy>Copy prompt</button><pre class="txt">{E(body)}</pre></div>{f'<p class="chk"><b>Check.</b> {E(check)}</p>' if check else ''}</article>'''
journey=[("Brief","Paste, upload or speak the brief. Pick a brand kit and tools","A chat screenshot becomes a clean brief"),("Read back","Check the spine, answer one sharp question","Assumptions are tagged, the plan is visible"),("Explore","Scan a spread of options, shortlist, compare","Real range, not eight versions of one idea"),("Refine","Direct with chips, generate previews, adapt","Make it simpler actually simplifies"),("Deliver","Export or share","Client ready in one click")]
tools=[("Key Visual","key-visual-builder","6 to 8 routes, copy suites, adaptation kits, build sheets, previews","Route book, PDF, prompt pack"),("Retail Theatre","fsu-display-units","One device per unit, a family from floor to counter, honesty check","Spec sheet, prompt pack, renders"),("Deck Designer","designed-deck-builder","Three design languages, locked type, slide by slide prompts","Slides PDF, PPTX, prompt pack"),("Content Calendar","social-content-calendar-builder","Month grid with 160 cultural moments, captions in each market language","XLSX, CSV, ICS, PDF"),("Campaign Strategy","campaign-strategy-builder","Nine sections with insight and territory checkpoints","DOCX, PDF, deck outline")]
nav=[("overview","Overview"),("preview","Design preview"),("research","Research"),("journey","User journey"),("architecture","Architecture"),("steps","Step by step"),("stitch","Stitch prompts"),("code","Claude Code prompts"),("iterate","Iteration prompts"),("plan","Build plan"),("pack","Starter pack")]
o=[]
o.append('''<section id="overview" class="sec"><div class="sh"><span class="n">01</span><h2>The recommendation</h2></div>
<div class="lede"><p><b>Build one studio, not five apps.</b> One shell, one login, one brand kit and one brief that flows into all five tools. Sell it as Solo (one tool), Studio (all five) and Agency (five seats). Cheaper to build, easier to maintain, and the hero feature, one brief feeding five tools, is something no generic AI tool offers.</p>
<p><b>Your skills are the engines.</b> Each tool loads its skill file as the system prompt and returns structured JSON the interface renders as cards, sheets and grids. Market modules plug in per country, so the same engine works in Lisbon, Lagos or Lima.</p>
<p><b>Stitch designs, Claude Code builds.</b> Stitch exports a DESIGN.md and connects to Claude Code through its MCP server, so the build reads your designs directly instead of guessing.</p></div>
<div class="kpis"><div><b>17</b><span>Stitch screens</span></div><div><b>19</b><span>Claude Code prompts</span></div><div><b>12</b><span>weeks to launch</span></div><div><b>160</b><span>cultural moments, 8 regions</span></div></div></section>''')
o.append('''<section id="preview" class="sec"><div class="sh"><span class="n">02</span><h2>Darkroom and Lightbox</h2></div><p class="intro">The design concept in one screen: dark tools so imagery glows, warm paper for every finished piece of work. This is a live CSS sketch of the route spread, not a screenshot.</p>
<div class="mock" aria-label="Sketch of the key visual route spread screen">
 <div class="mk-side"><div class="mk-logo">Bungee Studio</div><div class="mk-new">New brief</div><div class="mk-nav"><i>Home</i><i>Projects</i><i>Brand kits</i><i>Moments</i></div><div class="mk-nav mk-tools"><i class="on">Key Visual</i><i>Retail Theatre</i><i>Deck Designer</i><i>Content Calendar</i><i>Campaign Strategy</i></div><div class="mk-cred"><span>142 of 200 credits</span><b><i style="width:71%"></i></b></div></div>
 <div class="mk-main"><div class="mk-top"><span class="mk-steps"><i>Brief</i><i>Read back</i><i class="on">Explore</i><i>Refine</i><i>Deliver</i></span><span class="mk-search">Search or press Cmd K</span></div>
 <div class="mk-title"><h5>Northwind Coffee, Lisbon launch</h5><em>The first cup is yours.</em></div>
 <div class="mk-grid">
  <div class="mk-card"><div class="mk-img a"></div><b>01</b><h6>Morning Light</h6><span class="t s">Strong</span><p>Steam lifting from one cup on a sill at first light.</p></div>
  <div class="mk-card"><div class="mk-img b"></div><b>02</b><h6>Full Table</h6><span class="t sa">Safe</span><p>Six hands, one pot, nobody looking at the camera.</p></div>
  <div class="mk-card"><div class="mk-img c"></div><b>03</b><h6>Low Tide</h6><span class="t w">Wild</span><p>A cup the size of a boat on the sand at dawn.</p></div>
  <div class="mk-card"><div class="mk-img d"></div><b>04</b><h6>Second Half</h6><span class="t s">Strong</span><p>The 3pm cup, shot like a match winner.</p></div>
 </div>
 <div class="mk-fire"><span>Fire these first</span><i>01 Morning Light</i><i>02 Full Table</i><i class="alt">03 Low Tide, the alternate</i></div></div>
</div>
<div class="tokens"><div class="sw"><i style="background:#0F0E0D"></i><b>Darkroom</b><span>#0F0E0D</span></div><div class="sw"><i style="background:#F4EFE7;border:1px solid #DED5C6"></i><b>Lightbox paper</b><span>#F4EFE7</span></div><div class="sw"><i style="background:#E2572B"></i><b>Clay</b><span>#E2572B</span></div><div class="sw"><i style="background:#2A9D8F"></i><b>Lake, safe</b><span>#2A9D8F</span></div><div class="sw"><i style="background:#E9A23B"></i><b>Saffron, strong</b><span>#E9A23B</span></div><div class="sw"><i style="background:#7A5AF8"></i><b>Violet, wild</b><span>#7A5AF8</span></div><div class="sw"><i style="background:linear-gradient(90deg,#E2572B,#E9A23B,#2A9D8F)"></i><b>Horizon line</b><span>signature only</span></div></div>
<div class="type"><p class="t1">Instrument Serif for titles, route names and big numerals.</p><p class="t2">Hanken Grotesk for every label, body and button. Never all caps.</p><p class="t3">JetBrains Mono for prompts on dark plates.</p></div></section>''')
o.append('<section id="research" class="sec"><div class="sh"><span class="n">03</span><h2>What award winning apps teach</h2></div><p class="intro">Ten principles, where each comes from, and the feature it becomes.</p><div class="tbl"><table><thead><tr><th></th><th>Principle</th><th>Learned from</th><th>Becomes in Bungee Studio</th></tr></thead><tbody>'+
 "".join(f'<tr><td class="num">{int(a):02d}</td><td><b>{E(b.strip())}</b></td><td>{E(c.strip())}</td><td>{E(d.strip())}</td></tr>' for a,b,c,d in research)+'</tbody></table></div>'
 '<div class="twocol"><div class="card"><h3>The 2026 awards lens</h3><p>Jurors score design, usability, creativity and content, and the winners share three things at once: a specific art direction where every choice serves one idea, directed motion that explains rather than decorates, and performance on real mid range phones. For a working tool that means restraint plus craft: one point of view, motion that shows progress, a hard performance budget.</p></div><div class="card"><h3>Avoid</h3><ul><li>Chat as the main interface</li><li>Sparkle icons and magic language</li><li>Spinners with no information</li><li>Costs discovered after the click</li><li>Stock people and placeless scenes</li><li>Spectacle that stutters on a phone</li></ul></div></div></section>')
o.append('<section id="journey" class="sec"><div class="sh"><span class="n">04</span><h2>One journey, every tool</h2></div><p class="intro">Every tool walks the same five steps, so the product feels like one studio wherever it runs.</p><ol class="steps5">'+
 "".join(f'<li><span>{i}</span><h3>{E(a)}</h3><p>{E(b)}</p><em>{E(c)}</em></li>' for i,(a,b,c) in enumerate(journey,1))+'</ol>'
 '<div class="hero-j"><h3>The hero journey</h3><p>A strategist uploads a brief and runs <b>Campaign Strategy</b>. The chosen platform flows into <b>Key Visual</b>. The winning route flows into <b>Retail Theatre</b> and <b>Content Calendar</b> with its copy and look, in every market language the brand kit holds. The strategy outline opens in <b>Deck Designer</b> with the route imagery. The client gets one share link.</p></div>'
 '<div class="tbl"><table><thead><tr><th>Tool</th><th>Engine</th><th>What it makes</th><th>Exports</th></tr></thead><tbody>'+"".join(f'<tr><td><b>{E(a)}</b></td><td class="mono">{E(b)}</td><td>{E(c)}</td><td>{E(d)}</td></tr>' for a,b,c,d in tools)+'</tbody></table></div></section>')
o.append('''<section id="architecture" class="sec"><div class="sh"><span class="n">05</span><h2>Architecture</h2></div>
<div class="arch"><div class="col"><h4>Browser</h4><p>React, Vite, TypeScript, Tailwind, Motion. Tokens from DESIGN.md. Streams progress over Server Sent Events.</p></div>
<div class="col"><h4>API</h4><p>Express, Zod, Drizzle. Workspace isolation, entitlements and credits checked on every request.</p></div>
<div class="col accent"><h4>AI engine</h4><p>Skill file as system prompt with caching. Market modules per country. Staged runs, JSON through tool use, Zod validated, one repair retry, copy guards.</p></div>
<div class="col"><h4>Models, storage, money</h4><p>Claude for text, Gemini for image previews. Postgres, Redis jobs, object storage. Stripe by default behind a provider interface so regional payment methods plug in per country, with prices in local currency.</p></div></div></section>''')
st='<section id="steps" class="sec"><div class="sh"><span class="n">06</span><h2>Step by step</h2></div><p class="intro">Tick items as you go. Progress is saved in this browser.</p><div class="stepgrid">';k=0
for n,(t,items) in enumerate(STEPS,1):
    st+=f'<div class="stepc"><h3><span>{n}</span>{E(t)}</h3><ul>'
    for x in items: k+=1; st+=f'<li><label><input type="checkbox" data-k="s{k}"><span>{E(x)}</span></label></li>'
    st+='</ul></div>'
o.append(st+'</div></section>')
o.append('<section id="stitch" class="sec"><div class="sh"><span class="n">07</span><h2>Google Stitch prompts</h2></div><p class="intro">One project. Paste the design system first, then one screen per prompt, in order.</p>'+plate("DS","Design system","Paste this first. Every screen below refers to it.",ds,None,"All screens")+"".join(plate(s['id'],s['title'],None,s['body'],None,s['tag']) for s in S)+'</section>')
o.append('<section id="code" class="sec"><div class="sh"><span class="n">08</span><h2>Claude Code prompts</h2></div><p class="intro">Run in order. One prompt per session, /clear between them, commit after every passing check.</p>'+"".join(plate(c['id'],c['title'],c['when'],c['body'],c['check']) for c in C)+'</section>')
o.append('<section id="iterate" class="sec"><div class="sh"><span class="n">09</span><h2>Iteration prompts</h2></div><p class="intro">For when something is nearly right. Change one thing at a time.</p>'+"".join(plate(i['id'],i['title'],None,i['body']) for i in IT)+'</section>')
o.append('<section id="plan" class="sec"><div class="sh"><span class="n">10</span><h2>Build plan, Q4 2026</h2></div><p class="intro">Twelve weeks from 5 October, three tasks a week, soft launch in January 2027.</p><div class="tbl"><table><thead><tr><th>Week</th><th>Dates</th><th>Three tasks</th><th>Done when</th></tr></thead><tbody>'+"".join(f'<tr><td class="num">{E(a.strip())}</td><td class="nowrap">{E(b.strip())}</td><td>{E(c.strip())}</td><td>{E(d.strip())}</td></tr>' for a,b,c,d in plan)+'</tbody></table></div><div class="twocol"><div class="card"><h3>Running costs, estimates</h3><ul><li>Claude API text: USD 50 to 150 a month while building; keep AI cost under 30 percent of revenue</li><li>Image previews: around USD 0.10 per 2K image, covered by plan credits</li><li>Postgres, hosting, Redis, storage: under USD 50 while building</li></ul></div><div class="card"><h3>Launch metrics</h3><ul><li>40 percent of new workspaces export within 20 minutes</li><li>60 percent of routes shortlisted or exported</li><li>50 percent of paying workspaces active in week 4</li><li>100 paying workspaces in 90 days</li></ul></div></div></section>')
o.append('''<section id="pack" class="sec"><div class="sh"><span class="n">11</span><h2>The starter pack</h2></div><p class="intro">Unzip it as your repo. Claude Code reads it in the first session.</p>
<div class="tree"><div><b>CLAUDE.md</b><span>Rules for every session</span></div><div><b>DESIGN.md</b><span>Starter tokens, replace with your Stitch export</span></div><div><b>docs/</b><span>PRD, journeys, research, build plan</span></div><div><b>docs/apps/</b><span>Stages, schemas and exports per tool</span></div><div><b>prompts/skills/</b><span>The five engines with market modules</span></div><div><b>data/</b><span>160 moments, global plus regional packs</span></div><div><b>templates/</b><span>Route book export with the motion brief panel</span></div><div><b>brand/</b><span>The Bungee logo files</span></div><div><b>.claude/agents/</b><span>Reviewer and UI critic</span></div><div><b>stitch/ and claude-code/</b><span>Every prompt on this page as text, CC19 launch film included</span></div></div></section>''')
tpl=open('/home/claude/guide_tpl.html').read()
open('/mnt/user-data/outputs/bungee-studio-build-kit.html','w').write(tpl.replace('<!--NAV-->',"".join(f'<a href="#{a}">{E(b)}</a>' for a,b in nav)).replace('<!--BODY-->',"\n".join(o)))
print(len(S),len(C),len(IT),len(research),len(plan),[len(x[1]) for x in STEPS])
