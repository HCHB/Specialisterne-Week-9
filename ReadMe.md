Searching for cereals are done through a query string. 
F.x.

    localhost/cereal?fat=1&calories[lt]=100&calories[gt]=10&shelf=1

The brackets are used for determining what kind of comparison is being performed, where no brackets means a simple equals

[lt]  = less than
[leq] = less than or equal
[gt]  = greater than
[geq] = greater than or equal
[ne]  = not equal
