# facebook-friends-comparer

Comparison of two Facebook friend lists formed from Facebook Data backups: [https://www.youtube.com/watch?v=pOMO_9FLHn8](https://www.youtube.com/watch?v=pOMO_9FLHn8)

### Problem:

It is necessary to compare two lists of friends from Facebook backup files in the JSON format and identify new and deleted (deleted) friends.

Old Friends List:

![alt text](old_friends.png)

New Friends List:

![alt text](new_friends.png)

See examples in **/examples** folder.

### Usage:

> python3 compare.py

### Result:

**diff.json** in **/data** folder

Diff List:

![alt text](result_3.png)

Console Output:

![alt text](result_1.png)

![alt text](result_2.png)
