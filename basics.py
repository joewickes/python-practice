print('PRINT BASIC STATEMENT ->', 'Hello, World!');

# Assign a variable
msg = 'Hello World...';

# Print variable value
print('VARIABLE PRINT ->', msg);

# Make a list
singleList = ['one', 'two', 'three'];

# Print item at index from the list
print('ITEM AT 0 ->', singleList[0]);

# Get item from the end of a list
print('ITEM AT 2 (END) ->', singleList[-1]);

# Test type coersion
print('BOOLEAN "1" == 1 ->', 1 == '1');

# Check for value in singleList
print('BOOLEAN VALUE IN LIST ->', 'two' in singleList);
print('BOOLEAN VALUE NOT IN LIST ->', 'seven' not in singleList);


# Make a tuple (immutable list)
tupleOne = (1, 2, 3)

# Print tuple at 0
print ('TUPLE AT 0 ->', tupleOne[0]);