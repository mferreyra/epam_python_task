# epam_python_task
### Solutions to Python tasks assigned for the course: [Specialization] Cloud&amp; DevOps External LatAm



## Task 1

Create a class Dictionary to which you can add words and their entries.
```
>>> d = Dictionary()

>>> d.newentry('Apple', 'A fruit that grows on trees')

>>> print(d.look('Apple'))
outputs: A fruit that grows on trees

>>> print(d.look('Banana'))
outputs: Can´t find entry for Banana
```


## Task 2

Given a Dictionary of items and their costs and an array specifying the items bought, calculate the total costs of the items plus a given tax.

If the item doesn´t exist in the given cost values, the item is ignored.
Output should be rounded to two decimal places.

```
>>> costs = {'socks':5, 'shoes':60, 'sweater':30}

>>> print(get_total_cost(costs, ['socks', 'shoes', 'asdf'], 0.09))
outputs: 70.85
```


## Task 3

Complete the function that takes an array of words.

You must concatenate the *n* th letter from each word to construct a new word which should be return as a string, where *n* is the position of the word in the list.

```
>>> my_list = ["yoda", "best", "has"]

>>> print(word_from_list(my_list))
outputs: yes
```


## TODO
- ~~Unit test~~
- ~~Dockerize~~
- CI/CD
