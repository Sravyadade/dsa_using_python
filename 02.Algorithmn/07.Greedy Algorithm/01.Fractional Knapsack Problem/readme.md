**Fractional Knapsack Problem**
Given two arrays, val[] and wt[], representing the values and weights of items, 
and an integer capacity representing the maximum weight a knapsack can hold,
the task is to determine the maximum total value that can be achieved by putting items in the knapsack.
You are allowed to break items into fractions if necessary.

Note: Return the maximum value as a double, rounded to 6 decimal places.
**INPUT**
Input: val[] = [60, 100, 120], wt[] = [10, 20, 30], capacity = 50
**OTUPUT**
Output: 240 
Explanation: By taking items of weight 10 and 20 kg and 2/3 fraction of 30 kg. 
Hence total price will be 60+100+(2/3)(120) = 240

**INPUT**
Input:  val[] = [500], wt[] = [30], capacity = 10
**OTUPUT**
Output: 166.667
