# meaningful_re
Regular expression builder with chainable methods.

Instead of having to read and figure out the meaning of those weird strings, you can use an object to build your regex with methods with more sense.


### Example

Let's say you want to make a regular expression like `r'^[hc]at$'`, you can do it like this:

```python
from meaningful_re import MeaningfulRE as MRE

mre = (MRE('[hc]')
    .concat('at')
    .match_start
    .match_end)

print mre.regex
```

> Note: It doesn't matter if you use `match_start` or `match_end` at the beginning, middle or end of you chaining methods, when you show the `regex` they will be in their corresponding string position.



Or if you want to make an email regular expression like `r'\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b'`, not everybody can read that, but, with meaningful_re it makes more sense doing it.

```python
from meaningful_re import MeaningfulRE as MRE

mre = (MRE()
    .word_boundary
    .any_of(MRE.RANGE_UPPERCASE_ALPHABET, MRE.RANGE_NUMBERS, '._%+-')
    .concat('+@')
    .any_of(MRE.RANGE_UPPERCASE_ALPHABET, MRE.RANGE_NUMBERS, '.-')
    .concat('+\.')
    .any_of(MRE.RANGE_UPPERCASE_ALPHABET).at_least(2)
    .word_boundary)
```


Another example using capturing group, if you would like to match all string starting with **IMG** and ending with either **.png** or **jpeg** like `r'^(IMG\d+)\.(png|jpeg)$'`, can be built this way:

```python
from meaningful_re import MeaningfulRE as MRE

mre = (MRE()
    .match_start
    .gi
        .one_or_more('IMG' + MRE.DIGIT)
    .ge
    .concat('\.')
    .gi
        .or_('png', 'jpeg')
    .ge)
```