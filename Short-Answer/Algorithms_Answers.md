# Analysis of Algorithms Answers
## Exercise I

a) Answer: The time complexity of this pseudo code is O(n^3)

b) Answer: O(n^4)
<!-- scratch area -->
L1    L2       L3            L4     
 n * (n-1) * ((n-1)-1) * (((n-1)-1)-1+10) = O(n^4)
<!-- End scratch area -->

c) Answer: O(n)
<!-- Scratch area -->
O(n + 1) = O(n)
<!-- End scratch area -->

## Exercise 2

I would drop an egg at the middle floor and see if it breaks.  If it does I can eliminate the floors above and I would go down half the remaining floors and test there.  If it doesn't then I can eliminate the floors below and I would go up half the floors above me and test again. I would then repeat the process of going to the halfway point of the remaining floors that I haven't eliminated and testing if the egg breaks or not.  During this I would keep track of the most recent floor the egg broken when dropped from and the most recent floor the egg was unbroken when dropped from. When those two numbers are 1 apart, I have my answer, the floor that the eggs broke from.

building_height = _n_
eggs are broken >= _f_
eggs are unbroken <= _f_

_f_ = None
egg_broken=None
egg_unbroken=None

find_floor(arr_of_floors):
  global egg_broken
  global egg_unbroken
  if egg_broken == egg_unbroken + 1
    return _f_ = egg_broken
  <!-- find middle floor of array of floors -->
  var median = arr_of_floors[0] + (len(arr_of_floors) / 2)
  <!-- test drop an egg from middle floor -->
  drop egg from median floor
  if egg_breaks == true:
    <!-- recursively call function subtracting floors that won't work -->
    egg_broken = median
    find_floor(arr_of_floors[:(len(arr_of_floors) / 2)-1])
  else:
    <!--  -->
    egg_unbroken = median
    find_floor(arr_of_floors[len(arr_of_floors) / 2) + 1:])

array = range(_n_)

find_floor(array, None, None)


<!-- funny aside -->
Also we did this experiment in high school.  Eggs typically break from above about 20ft -25ft on grass.  So in reality, I would test floors 2 and 3 first if they're over grass because that's about where they should start to break.  If a hard surface, just drop them on the ground floor, lol.