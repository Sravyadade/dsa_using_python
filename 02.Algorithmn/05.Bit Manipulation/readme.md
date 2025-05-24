**Python Bitwise Operators**:-
Python bitwise operators are used to perform bitwise calculations on integers. 
The integers are first converted into binary and then operations are performed on each bit or corresponding pair of bits,
hence the name bitwise operators. The result is then returned in decimal format.
**Operator**   	**Description**	           **Syntax**
&	               Bitwise AND	               x & y
|	               Bitwise OR	                 x | y
~	               Bitwise NOT	               ~x
^	               Bitwise XOR	               x ^ y
>>	             Bitwise right shift	       x>>
<<	             Bitwise left shift	         x<<

**Bitwise AND Operator**
Python Bitwise AND (&) operator takes two equal-length bit patterns as parameters. 
The two-bit integers are compared. 
If the bits in the compared positions of the bit patterns are 1, then the resulting bit is 1. If not, it is 0.
**Example**: Take two bit values X and Y, where X = 7= (111)2 and Y = 4 = (100)2 . Take Bitwise and of both X & y.

**Bitwise OR Operator**
The Python Bitwise OR (|) Operator takes two equivalent length bit designs as boundaries;
if the two bits in the looked-at position are 0, the next bit is zero. If not, it is 1.
**Example**: Take two bit values X and Y, where X = 7= (111)2 and Y = 4 = (100)2 . Take Bitwise OR of both X, Y

**Bitwise XOR Operator**
The Python Bitwise XOR (^) Operator also known as the exclusive OR operator, 
is used to perform the XOR operation on two operands. XOR stands for "exclusive or", and it returns true if and only if exactly one of the operands is true. 
In the context of bitwise operations, it compares corresponding bits of two operands. If the bits are different, it returns 1; otherwise, it returns 0.
**Example**: Take two bit values X and Y, where X = 7= (111)2 and Y = 4 = (100)2 . Take Bitwise and of both X & Y

**Bitwise NOT Operator**
The preceding three bitwise operators are binary operators, 
necessitating two operands to function. However, unlike the others, this operator operates with only one operand.
Python Bitwise Not (~) Operator works with a single value and returns its one’s complement. 
This means it toggles all bits in the value, transforming 0 bits to 1 and 1 bits to 0, 
resulting in the one’s complement of the binary number.
**Example**: Take two bit values X and Y, where X = 5= (101)2 . Take Bitwise NOT of X.
