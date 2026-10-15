# Moments 2027 calendar test

Thu 15 Oct 2026. Two calendar files tested: the full `Moments-2027.ics` that ships in the zip, and the "My picks" file the almanac page exports.

## Result: two real bugs found and fixed

| # | Problem | Who it hits | Fix |
| --- | --- | --- | --- |
| 1 | **Exported picks landed one day early** in any time zone ahead of UTC. The page turned each date into local midnight, then wrote it out in UTC. In Nairobi, New Year's Day was saved as 31 Dec 2026. Seoul, Europe, Asia and Africa were all affected; the Americas were not. | Every buyer east of London, including Stephen's home market | Dates now stay in UTC end to end. Proven by exporting all 160 picks from a real browser set to Nairobi, Los Angeles and Auckland: every start and end date matches the data in all three. |
| 2 | **All 160 moments would show as busy** for the whole day, so importing the almanac blocked a buyer's calendar all year and broke meeting scheduling. | Everyone who imports | Every event is now marked free (`TRANSP:TRANSPARENT`), in both files. |

## Also tightened

* Lines folded at 75 octets as the calendar standard requires (159 lines were up to 562). Strict importers, Outlook among them, can reject or cut long lines. Folding never splits a multi byte character.
* Added `CALSCALE:GREGORIAN` and `METHOD:PUBLISH`, which Outlook expects for an imported calendar.
* The picks export now carries `DTSTAMP` (required by the standard; it was missing) and the category, and ends with a line break.

## Checks run

* Parsed both files with a standards library: 160 events each, 160 unique IDs, no end before start, categories intact (Holiday 47, Commercial 32, Cultural 27, Religious 24, Sport 15, Sensitive 11, Seasonal 4).
* Every event title and date matches `moments-2027.json`.
* Longest physical line 75 octets; every line valid UTF 8.

## Still needs a person (5 minutes)

The files now meet the standard, but the last proof is importing them into the three apps buyers use. This needs a real account, so it is on Stephen's list:

1. Google Calendar on the web: Settings, Import and export, Import, pick `Moments-2027.ics`, choose a new empty calendar.
2. Outlook on the web: Calendar, Add calendar, Upload from file.
3. Apple Calendar: File, Import.

Check in each: 1 Jan shows New Year's Day on 1 Jan, a multi day moment spans the right days, and the day shows as free.
