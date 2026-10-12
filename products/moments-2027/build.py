import json, csv, datetime as dt, html
from moments_global import G
CN={"KE":"Kenya","UG":"Uganda","TZ":"Tanzania","RW":"Rwanda","ZM":"Zambia"}
rows=[]
for s,e,r,t,c,f,a,h,av in G:
    rows.append(dict(start=s,end=e or s,regions=["Worldwide" if x=="World" else x for x in r],countries=[],pack="Global",title=t,category=c,status={"":"fixed","est":"expected","confirm":"confirm"}[f],angle=a,hook=h,avoid=av))
ea=json.load(open('ea.json'))['moments']
for m in ea:
    rows.append(dict(start=m['start'],end=m['end'],regions=["East Africa"],countries=[CN[c] for c in m['countries']],pack="East Africa",title=m['title'],category=m['category'],status=m['date_status'],angle=m['angle'],hook=m['hook'],avoid=m['avoid']))
rows.sort(key=lambda r:(r['start'],r['end']!=r['start'],r['pack']!='Global',r['title']))
for i,r in enumerate(rows): r['id']=f"m{i:03d}"
import os; os.makedirs('out',exist_ok=True)
json.dump({"edition":2027,"packs":["Global","East Africa"],"moments":rows},open('out/moments-2027.json','w'),ensure_ascii=False,indent=1)
with open('out/Moments-2027.csv','w',newline='') as f:
    w=csv.writer(f); w.writerow(["Start","End","Pack","Regions","Countries","Moment","Category","Date status","Content angle","Sample hook","Avoid"])
    for r in rows: w.writerow([r['start'],r['end'],r['pack'],", ".join(r['regions']),", ".join(r['countries']),r['title'],r['category'],r['status'],r['angle'],r['hook'],r['avoid']])
def esc(s): return s.replace("\\","\\\\").replace(",","\\,").replace(";","\\;").replace("\n","\\n")
L=["BEGIN:VCALENDAR","VERSION:2.0","PRODID:-//Bungee//Moments 2027//EN","X-WR-CALNAME:Bungee Moments 2027"]
for r in rows:
    d0=dt.date.fromisoformat(r['start']); d1=dt.date.fromisoformat(r['end'])+dt.timedelta(days=1)
    desc=f"{r['angle']}\nHook: {r['hook']}\nAvoid: {r['avoid']}\nRegions: {', '.join(r['regions'])}"+(f"\nMarkets: {', '.join(r['countries'])}" if r['countries'] else "")
    L+=["BEGIN:VEVENT",f"UID:bungee-2027-{r['id']}@bungee","DTSTAMP:20260928T000000Z",f"DTSTART;VALUE=DATE:{d0:%Y%m%d}",f"DTEND;VALUE=DATE:{d1:%Y%m%d}","SUMMARY:"+esc(("[EA] " if r['pack']!='Global' else "")+r['title']),"DESCRIPTION:"+esc(desc),"CATEGORIES:"+r['category'],"END:VEVENT"]
L.append("END:VCALENDAR")
open('out/Moments-2027.ics','w').write("\r\n".join(L)+"\r\n")
t=open('template.html').read().replace('/*DATA*/',json.dumps(rows,ensure_ascii=False))
open('out/Moments-2027.html','w').write(t)
print(len(rows),"moments", sum(r['pack']=='Global' for r in rows),"global")
