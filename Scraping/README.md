# Scraping assignment (March. 25)

We have already scraped statewide election results for the Missouri presidential primaries in March, but your task for this assignment is to extend that same concept to county-level data.

The Missouri Secretary of State's office makes county-level election results available [here](http://enr.sos.mo.gov/EnrNet/CountyResults.aspx).

Your scraper should:

  - Loop over each county listed in the "counties" dropdown
  - Scrape results ONLY for the five active candidates: Clinton, Sanders, Cruz, Kasich and Trump
  - Display that information (either printed to the terminal or as CSV) in a format resembling this:

```
county, clinton_pct, sanders_pct, cruz_pct, kasich_pct, trump_pct
Adair,  40.745%,     58.797%,     33.487%,  14.758%,     40.391%
etc.
``` 

This assignment will be due **Monday, April 11**.

——————
Three keys to locate the form:
Form, select, submit