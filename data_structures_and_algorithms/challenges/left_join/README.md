# Hashmap LEFT JOIN

LEFT JOIN means all the values in the first hashmap are returned, and if values exist in the “right” hashmap, they are appended to the result row. If no values exist in the right hashmap, then some flavor of NULL should be appended to the result row.

## Challenge

**Code Challenge 33:**

- Write a function that LEFT JOINs two hashmaps into a single data structure.
- The first hashmap that has word strings as keys, and a synonym of the key as values.
- The second hashmap that has word strings as keys, and antonyms of the key as values.
- Combine the key and corresponding values (if they exist) into a new data structure according to LEFT JOIN logic.
- The returned data structure that holds the results is up to you. It doesn’t need to exactly match the output below, so long as it achieves the LEFT JOIN logic.

## Approach & Efficiency

Created a function that will combine two hashmaps into a new hashmap that contains all of their values at the corresponding keys.

## Solution

![left_join](../../../assets/left_join.png)
