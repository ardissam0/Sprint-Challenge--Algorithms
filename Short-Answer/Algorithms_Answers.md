#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) O(n) - it is Linear because the difference between the range and the loop is n.


b) O(n log n) - it is Log Linear because the first part of the function is O(n), but the while loop pointer is doubled each loop.


c)O(n) - it is Linear because the function will increment linearly as the value increases.

## Exercise II

 - I would use binary search to solve this problem because based on the problem, this would fit exactly what it is asking for eggs if f is at a certain height above or below.
 -I would take the length of the array of floors and //2 to get the middle.
 -Then if the egg drops on the middle floor and breaks, then get rid of the florrs above that, if it doesn't break then get rid of the bottom floors.
 -Then just keep going and dividing until the highest safe floor is reached.
 -Runtime complexity would be O(log n)


