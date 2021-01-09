# Hash Table

## Challenge

**Challenge 30:**

* Can add a key/value to your hashtable results in the value being in the data structure
* Can retrieve a value stored based on a key
* Can successfully return null for a key that does not exist in the hashtable
* Can successfully handle a collision within the hashtable
* Can successfully retrieve a value from a bucket within the hashtable that has a collision
* Can successfully hash a key to an in-range value

## Approach & Efficiency

I created a class which included the required methods.

## API

Available methods:
| Method | Usage|
| --- | --- |
| `add(key,Value)` |  hash the key, and add the key and value pair to the table, handling collisions as needed |
| `get(key)` |   takes in the key and returns the value from the table |
| `contains(key)` |  returns a boolean, indicating if the key exists in the table already |
| `hash(key)` |  returns an index in the collection |
