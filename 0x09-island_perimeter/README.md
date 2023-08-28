# Island Parameter
In this project, we attempt to find the perimeter of the island suspended in a water body.
## Logic
We assign a grade to every piece of land, based on whether the parts surrounding it in up/down direction contain land, or those in right/left direction contain land. For every land-bordering surface, we give the grade of 1. For every water bordering, we leave the grade to 0.

In the end, we compute a total which is the sum of `(4 - grade[x])` for every land piece x.
