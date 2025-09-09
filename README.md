# Mucking around with Numerical Expression

## Problem 06: Roman Numerals
Roman numerals are a system of numbering that originated in ancient
Rome and are represented by a combinations of letters from the latin
alphabet. The table below shows the value of the different
letters that make up our "alphabet".

| **Symbol** | `I` | `V` | `X` | `L` | `C` | `D` | `M`  |
|------------|-----|-----|-----|-----|-----|-----|------|
|  **Value** |  1  |  5  | 10  | 50  | 100 | 500 | 1000 |

For the numerals 4 (`IV`) and 9 (`IX`) are written using
\"subtractive notation\", where the first symbol is subtracted from
the larger one. The largest number that can be represented using
roman numerals is 3999 (`MMMCMXCIX`). The function
`roman_numeral`{.python} should take an natural number between 1 and
3999 and return the correct expression in roman numerals.

## Problem 07: Totally Roman
The function `total_roman`{.python}, should take a natural number
and return the what its value would be if you just added up all the
characters in its expression in roman numerals. For example
`total_roman(6) = 6`{.python} because `VI V + I = 5 + 1 = 6`.
Whereas `total_roman(4) = 6`{.python} because
`IV I + V = 1 + 5 = 6`.

## Problem 08: A Chiseled Roman
How many chisel strokes would it take to form a Roman numeral?
`chisel_strokes` takes an integer `n`, and returns the number of
chisel strokes it takes to form that number in Roman numerals. We
say that `C` takes 2 and `D` takes 3. The table below
shows the number of chisel strokes for a selection of inputs.

| **Input** | **Roman Numeral** | **Chisel Strokes** |
|:---------:|:-----------------:|:------------------:|
|    `1`    |        `I`        |        `1`         |
|    `2`    |       `II`        |        `2`         |
|    `4`    |       `IV`        |        `3`         |
|   `46`    |      `XLVI`       |        `7`         |
|   `102`   |       `CII`       |        `4`         |
|   `512`   |      `DXII`       |        `5`         |
|  `1000`   |        `M`        |        `5`         |

## Problem 09: Speak and Say Numbers
The function `describe`{.python} takes in a natural number and
describe it. So for example `23` has \"one 2, one 3\", so
`describe(23) = 1213`{.python}. For example below we have 
a selection of numbers with their descriptions.

| **Input** | **Description** | **Notes**    |
|:---------:|:---------------:|:-------------|
|    `0`    |      `10`       | One 0        |
|    `1`    |      `11`       | One 1        |
|   `10`    |     `1110`      | One 1, One 0 |
|   `11`    |      `21`       | Two 1s       |
|   `22`    |      `22`       | Two 2s       |

## Problem 10: Binary Without Zeros
The function `binary_without_zeros`{.python} takes in a natural
number and converts it into binary, deleting the zeros. So for
example `binary_without_zeros(23) = 1111`{.python} because 23 in
binary is `10111` so removing the zeros leaves `1111`.
