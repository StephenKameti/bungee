# Moments 2027 date check, 12 Oct 2026

Scope: every moment marked expected (13) or confirm (12), plus a spot check of 12 fixed dates. Data files: `products/moments-2027/moments_global.py` and `ea.json`. Rebuilt with `python3 build.py` (160 moments, 88 global).

Result: 14 of the 25 records changed (dates, status, markets or copy). 5 dates moved (Holi, Maulid, Zanzibar music festival, Zanzibar film festival, Zambia show), 8 statuses went to fixed, Uganda left the January back to school window. The spot check found 2 wrong fixed dates (AFCON final, Cricket World Cup start), both corrected. Status count now: 143 fixed, 7 expected, 10 confirm (was 135, 13, 12).

## The 25 expected and confirm moments

| # | Moment (pack) | Old date | New date | Status (old to new) | Source | Note |
|---|---|---|---|---|---|---|
| 1 | Ramadan (Global) | 8 Feb to 9 Mar | unchanged | expected | [Khaleej Times, UAE Astronomy Centre](https://www.khaleejtimes.com/uae/ramadan-eid-al-fitr-eid-al-adha-2027-likely-dates) | Expected start Mon 8 Feb. Moon sighted, stays expected. India and some EA markets may start 9 Feb. |
| 2 | Ramadhan (EA) | 8 Feb to 9 Mar | unchanged | expected | same | Same as above. |
| 3 | Eid al Fitr (Global) | 9 to 10 Mar | unchanged | expected | same; [India DoPT 2027 list](https://www.staffnews.in/2026/07/list-of-holidays-for-the-year-2027-gazetted.html); [Singapore MOM](https://www.mom.gov.sg/maintenance/employment-practices/public-holidays/) | UAE calc 9 or 10 Mar. India and Singapore gazette 10 Mar. Range already covers both. |
| 4 | Eid al Fitr (EA) | 9 to 10 Mar | unchanged | expected | same | Kenya, Tanzania, Uganda gazette after sighting. |
| 5 | Holi (Global) | 22 Mar | 22 to 23 Mar | expected to fixed | [DoPT OM 12/2/2023 JCA, 16 Jul 2026 (PDF)](https://www.gconnect.in/gc22/wp-content/uploads/2026/07/Holiday-list-2027.pdf) | India gazettes Holi Tue 23 Mar, Holika Dahan Mon 22 Mar. Old single date was the US panchang day. Angle now names both nights. |
| 6 | World Snooker Championship centenary (Global) | 17 Apr to 3 May | unchanged | confirm to fixed | [Wikipedia citing WST tickets page](https://en.wikipedia.org/wiki/2027_World_Snooker_Championship) | Dates confirmed. Copy fixed: the championship turns 100 (first held 1927); the Crucible hosts for a 51st year, it is not 100. WST page itself could not be fetched; quick eye check advised. |
| 7 | Eid al Adha (Global) | 16 to 17 May | unchanged | expected | Khaleej Times; DoPT; MOM | UAE calc 16 or 17 May. India and Singapore gazette 17 May. |
| 8 | Eid al Adha (EA) | 16 to 17 May | unchanged | expected | same | |
| 9 | Vesak (Global) | 20 May | unchanged | expected to fixed | [Singapore MOM](https://www.mom.gov.sg/maintenance/employment-practices/public-holidays/); DoPT (Buddha Purnima 20 May) | Angle adds that a few national calendars differ. Thailand and Sri Lanka not checked. |
| 10 | Dragon Boat Festival (Global) | 9 Jun | unchanged | expected to fixed | [Hong Kong Labour Dept 2027](https://www.labour.gov.hk/eng/news/latest_holidays2027.htm) | Tuen Ng Festival 9 Jun. |
| 11 | Maulid (EA) | 15 Aug | 14 to 15 Aug | expected | [islamic.app](https://islamic.app/hijri/mawlid/2027); DoPT (Milad un Nabi 15 Aug) | Calculated 14 Aug, India gazettes 15 Aug. Range widened, angle says expected 14 or 15. |
| 12 | Ganesh Chaturthi (Global) | 4 Sep | unchanged | expected to fixed | DoPT restricted list (PDF above) | 4 Sep in India. US panchang shows 3 Sep for the diaspora. |
| 13 | Mid Autumn Festival and Chuseok (Global) | 15 Sep | unchanged | expected to fixed | Hong Kong Labour Dept | Day following Mid Autumn is 16 Sep, so the festival is 15 Sep. |
| 14 | Diwali (EA) | 29 Oct | unchanged | expected to fixed | DoPT (29 Oct); [ShreeKundli Nairobi](https://www.shreekundli.com/diwali-puja-calendar/nairobi/2027) | Lakshmi Puja 29 Oct. Singapore gazettes Deepavali 28 Oct; the global entry already spans 27 to 31 Oct. |
| 15 | Back to school (EA) | 4 to 15 Jan | unchanged, Uganda removed | confirm | [Education News Hub on MoE calendar](https://educationnewshub.co.ke/education-ministry-releases-the-2026-2027-academic-term-dates-for-all-schools/); [Monitor, Uganda 2026](https://www.monitor.co.ug/uganda/news/education/govt-releases-dates-for-2026-school-calendar-5318340) | Kenya Term 1 opens Mon 4 Jan 2027. Uganda opens in February (10 Feb in 2026), so UG dropped from this window and the avoid line says so. Tanzania, Rwanda, Zambia still to confirm. |
| 16 | Ncwala ceremony (EA, ZM) | Feb | unchanged | confirm | [NPA on Ncwala 2026](https://www.npa.gov.zm/?p=5751) | Held late February (2026 on the last weekend). 2027 not announced; likely Sat 27 Feb. |
| 17 | Zanzibar music festival season (EA, TZ) | 1 to 28 Feb | 19 to 21 Mar | confirm to fixed | [Organiser site](https://busaramusic.org/); [Music In Africa, 20 May 2026](https://www.musicinafrica.net/node/391545) | Moved from February. Organisers set 19 to 21 Mar 2027, after Ramadhan and Eid. Angle updated. |
| 18 | Kuomboka ceremony (EA, ZM) | 1 Mar to 15 Apr | unchanged | confirm | [Zambia Tourism, 2026 date](https://www.zambiatourism.com/date-set-for-2026-kuomboka-ceremony/) | Set by the Barotse Royal Establishment each year (28 Mar in 2026). Window holds. |
| 19 | Umutomboko ceremony (EA, ZM) | July | unchanged | confirm | [Zambian Observer, 2026](https://zambianobserver.com/?p=703360) | 25 Jul in 2026 (last Saturday). 2027 likely 24 Jul. |
| 20 | Zanzibar film festival season (EA, TZ) | 1 to 31 Jul | 15 Jun to 15 Jul | confirm | [ZIFF site](https://www.ziff.or.tz/) | 2026 ran 24 to 28 Jun, so July alone missed it. Window moved; avoid line asks to confirm. |
| 21 | Zambia Agricultural and Commercial Show (EA) | 29 Jul to 2 Aug | 28 Jul to 2 Aug | confirm | [ACSZ 2026 brochure](https://acsz.co.zm/files/2026-Brochure.pdf) | 2026 ran Wed 29 Jul to Mon 3 Aug (Farmers' Day). Same pattern in 2027 is Wed 28 Jul to Mon 2 Aug. |
| 22 | Likumbi Lya Mize (EA, ZM) | August | unchanged | confirm | [Kumakonda tour listing](https://kumakonda.com/?p=25886) | Held every August, main day a Saturday late in the month. No 2027 date yet. |
| 23 | Kwita Izina (EA, RW) | September | unchanged | confirm | [ATTA, 12 Aug 2026](https://atta.travel/resource/rwanda-to-name-22-baby-gorillas-at-21st-kwita-izina-ceremony.html) | 2026 held 4 Sep. RDB announces 2027 mid year. |
| 24 | KCSE exams, final ever sitting (EA, KE) | 1 Oct to 30 Nov | unchanged | confirm | [The Standard, KNEC CEO](https://www.standardmedia.co.ke/education/article/2001551672/knec-call-for-kcse-candidates-as-curtain-falls-on-8-4-4-education-system) | KNEC confirms 2027 is the last KCSE; angle no longer says "expected". Exam dates not out (2026 ran 2 to 20 Nov). |
| 25 | Lamu Cultural Festival (EA, KE) | November | unchanged | confirm | [KNA, 8 Oct 2026](https://www.kenyanews.go.ke/rivalry-likely-to-undermine-annual-lamu-cultural-fete/) | Usually November, but 2026 moved to 12 to 15 Dec to avoid Maulidi. Avoid line now says confirm 2027 with the county. |

## Spot check of fixed dates

| Moment | Date in data | Source | Result |
|---|---|---|---|
| Lunar New Year | 6 Feb | [HK Labour Dept](https://www.labour.gov.hk/eng/news/latest_holidays2027.htm), MOM | OK |
| Qingming | 5 Apr | HK Labour Dept | OK |
| Easter (Good Friday 26 Mar) | 28 Mar | DoPT, MOM (Good Friday 26 Mar) | OK |
| Vaisakhi | 14 Apr | DoPT restricted list | OK |
| Durga Puja and Dussehra | 6 to 10 Oct | DoPT (Saptami 6 Oct, Dussehra 9 Oct) | OK |
| Diwali (Global) | 27 to 31 Oct, Diwali 29 Oct | DoPT; [ShreeKundli](https://www.shreekundli.com/diwali-puja-calendar/new-delhi/2027) | OK (Singapore 28 Oct sits inside the range) |
| Super Bowl LXI | 14 Feb | [FBSchedules, 2026 NFL schedule](https://fbschedules.com/nfl-schedule-release-2026-complete-18-week-slate-unveiled/amp/) | OK |
| Champions League final | 5 Jun, Madrid | [Wikipedia](https://en.wikipedia.org/wiki/2027_UEFA_Champions_League_final) | OK |
| FIFA Women's World Cup | 24 Jun to 25 Jul | [Netflix Tudum schedule](https://www.netflix.com/tudum/articles/fifa-womens-world-cup-2027-match-schedule) | OK |
| Men's Rugby World Cup | 1 Oct to 13 Nov | [Sydney.com](https://www.sydney.com/events/rugbyworldcup27) | OK |
| Africa Cup of Nations | 19 Jun to 18 Jul | [ICIR quoting CAF](https://www.icirnigeria.org/caf-announces-afcon-2027-dates/); [SuperSport](https://supersport.com/football/news/0b8d3bac-a49c-4bc3-8a82-e9ee9e7674ca/africa-cup-of-nations-confirm-dates-for-kenya-tanzania-and-uganda) | WRONG. CAF: final Sat 17 Jul. Changed end to 17 Jul. (Flashscore still says 18 Jul.) |
| Men's Cricket World Cup | 4 Oct to 21 Nov | [ICC media release](https://www.icc-cricket.com/media-releases/icc-men-s-cricket-world-cup-2027-schedule-revealed-and-ballot-system-opens) | WRONG. Starts 2 Oct. Changed start to 2 Oct. |

## Build and output checks

* `python3 build.py`: 160 moments, 88 global.
* CSV, JSON and HTML agree row for row on start, end, title and status; every title is in the HTML data.
* ICS: 160 events, 160 unique UIDs, CRLF line endings, DTEND is the day after End for every row. Parsed cleanly with `icalendar` 7.3.0.
* `build.py`: fixed an invalid escape (`"\;"` to `"\\;"`) that raises a SyntaxWarning on newer Python. Output is byte identical.

## Still needs a native or official check later

1. Ramadan start, both Eids and Maulid: national moon sighting announcements in each market (Kenya Chief Kadhi, BAKWATA, UMSC). Stay expected.
2. Kenya, Tanzania, Rwanda and Zambia 2027 school calendars when each ministry publishes; KNEC 2027 KCSE timetable.
3. Zambian ceremonies (Ncwala, Kuomboka, Umutomboko, Likumbi Lya Mize), Kwita Izina, ZIFF, Lamu Cultural Festival and the ACSZ show: organiser announcements, usually two to eight weeks out.
4. Vesak in Thailand and Sri Lanka; Holi date in Nepal.
5. World Snooker Championship: eye check the WST ticket page (fetch was blocked here).
