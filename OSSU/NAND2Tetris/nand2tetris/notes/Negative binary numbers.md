All systems for representing negative binary numbers need to take into account the bit range of the number (4-bit, 8-bit, 16-bit...).

### Sign Bit approach

Just use the MSB as a sign to denote negative numbers if it equals 1.

| - | 4 | 2 | 1 | decimal |
|--|--|--|--|--|
|1|1|1|1|-7|
|1|1|0|1|-6|
|1|1|1|0|-5|
|1|1|0|0|-4|
|1|0|1|1|-3|
|1|0|1|0|-2|
|1|0|0|1|-1|
|1|0|0|0|-0|
|0|0|0|0|0|
|0|0|0|1|1|
...

But this causes some issues, like having negative 0 or being unable to do addition with them.

## One's Complement

This method consists of flipping the bits to represent a number's negative __complement__. 

| 8 | 4 | 2 | 1 | decimal |
|--|--|--|--|--|
|1|0|0|0|-7|
|1|0|1|0|-6|
|1|0|0|1|-5|
|1|0|1|1|-4|
|1|1|0|0|-3|
|1|1|0|1|-2|
|1|1|1|0|-1|
|1|1|1|1|-0|
|0|0|0|0|0|
|0|0|0|1|1|
...
This works a bit better, but addition is off by one binary digit. Sums of a number and its complement result in -0 (1111) instead of 0 (0000), and all other additions/substractions are off by 1. You could always use this and add one, but it is messy, so you should better use...

# Two's complement

This method consists of flipping the bits and adding one. Alternatively, it can be seen as using the MSB for -(2$^n$). 
| -8 | 4 | 2 | 1 | decimal |
|--|--|--|--|--|
|1|1|1|1|-8|
|1|1|0|1|-7|
|1|1|1|0|-6|
|1|1|0|0|-5|
|1|0|1|1|-4|
|1|0|1|0|-3|
|1|0|0|1|-2|
|1|0|0|0|-1|
|0|0|0|0|0|
|1|0|0|1|1|

This checks out for all additions. All complementary additions result in an overflow (carry the one out of range), followed by zeroes. It also gets rid of the pesky -0.
However, it's a bit more difficult to calculate the complement right off the bat.
__This is the industry standard.__
