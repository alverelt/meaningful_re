""" Regular expression builder with chainable methods."""
import re
from .expression import Expression


class MeaningfulRE(Expression):
    def __init__(self, obj=None):
        """
        Parameters
        ----------
        obj : None | str | MeaningfulRE
            In case you have a previous regular expression and want to
            continue building it.
        """
        self._match_start = False
        self._match_end = False

        if obj is None:
            self._regex = ''
        elif isinstance(obj, MeaningfulRE):
            self._regex = obj._regex
            self._match_start = obj._match_start
            self._match_end = obj._match_end
        elif isinstance(obj, str):
            self._regex = obj
            if obj.startswith('^'):
                self._match_start = True
                del self._regex[0]
            if obj.endswith('$'):
                self._match_end = True
                del self._match_end[-1]
        else:
            raise TypeError('Only allowed type: MeaningfulRE|str.')

    def concat(self, *patterns):
        """ Main method for building the regular expression. """
        self._regex += ''.join(str(p) for p in patterns)
        return self

    @property
    def regex(self):
        """ Returns the resulting regular expression. """
        output = ''

        if self._match_start:
            output += MeaningfulRE.MATCH_START

        output += self._regex

        if self._match_end:
            output += MeaningfulRE.MATCH_END

        return output

    @property
    def gi(self):
        """ Adds group opening parenthesis, gi = group init."""
        return self.concat('(')

    @property
    def ge(self):
        """ Adds group ending parenthesis, ge = group end."""
        return self.concat(')')

    @property
    def any_char_except_newline(self):
        """ Adds a dot (.) to the pattern."""
        return self.concat('.')

    @property
    def digit(self):
        """ Adds a \d to the pattern."""
        return self.concat(MeaningfulRE.DIGIT)

    @property
    def word(self):
        """ Adds a \w to the pattern."""
        return self.concat(MeaningfulRE.WORD)

    @property
    def space(self):
        """ Adds a \s to the pattern."""
        return self.concat(MeaningfulRE.SPACE)

    @property
    def tab(self):
        """ Adds a \t to the pattern."""
        return self.concat(MeaningfulRE.TAB)

    @property
    def new_line(self):
        """ Adds a \n to the pattern."""
        return self.concat(MeaningfulRE.NEW_LINE)

    @property
    def carriage_return(self):
        """ Adds a \r to the pattern."""
        return self.concat(MeaningfulRE.CARRIAGE_RETURN)

    @property
    def form_feed(self):
        """ Adds a \f to the pattern."""
        return self.concat(MeaningfulRE.FORM_FEED)

    @property
    def word_boundary(self):
        """ Adds a \b to the pattern."""
        return self.concat(MeaningfulRE.WORD_BOUNDARY)

    @property
    def escape(self):
        """ Adds a \e to the pattern."""
        return self.concat(MeaningfulRE.ESCAPE)

    @property
    def vertical_tab(self):
        """ Adds a \v to the pattern."""
        return self.concat(MeaningfulRE.VERTICAL_TAB)

    @property
    def not_digit(self):
        """ Adds a \D to the pattern."""
        return self.concat(MeaningfulRE.NOT_DIGIT)

    @property
    def not_word(self):
        """ Adds a \W to the pattern."""
        return self.concat(MeaningfulRE.NOT_WORD)

    @property
    def not_space(self):
        """ Adds a \S to the pattern."""
        return self.concat(MeaningfulRE.NOT_SPACE)

    @property
    def not_word_boundary(self):
        """ Adds a \B to the pattern."""
        return self.concat(MeaningfulRE.NOT_WORD_BOUNDARY)

    @property
    def match_start(self):
        """ When called, the pattern will be shown with a ^ at the beginning."""
        self._match_start = True
        return self

    @property
    def match_end(self):
        """ When called, the pattern will be shown with a $ at the end."""
        self._match_end = True
        return self

    def any_of(self, *patterns):
        """ Adds a pattern in the form -> [pattern].

        Example
        -------
        - MeaningfulRE().any_of('a-z', '0-9'), -> [a-z0-9] also

        - MeaningfulRE().any_of('a-z0-9'), -> [a-z0-9]
        """
        patterns = ('[',) + patterns + (']',)
        return self.concat(*patterns)

    def not_any_of(self, *patterns):
        """ Adds a pattern in the form -> [^pattern].

        Example
        -------
        - MeaningfulRE().any_of('a-z', '0-9'), -> [^a-z0-9] also

        - MeaningfulRE().any_of('a-z0-9'), -> [^a-z0-9]
        """
        patterns = ('[^',) + patterns + (']',)
        return self.concat(*patterns)

    def zero_or_one(self, pattern):
        """ Adds a pattern in the form -> pattern?"""
        return self.concat(pattern, '?')

    def zero_or_more(self, pattern):
        """ Adds a pattern in the form -> pattern*"""
        return self.concat(pattern, '*')

    def one_or_more(self, pattern):
        """ Adds a pattern in the form -> pattern+"""
        return self.concat(pattern, '+')

    def exactly(self, times):
        """ Adds a pattern in the form -> {times}"""
        return self.concat('{', str(times), '}')

    def at_least(self, minimum):
        """ Adds a pattern in the form -> {minimum,}"""
        return self.concat('{', str(minimum), ',}')

    def at_least_and_not_more(self, minimum, maximum):
        """ Adds a pattern in the form -> {minimum, maximum}"""
        return self.concat('{', minimum, ',', maximum, '}')

    def or_(self, *patterns):
        """ Adds a pattern in the form -> pattern|pattern|pattern etc.

        Raises
        ------
        ValueError
            You must send at least 2 arguments.
        """
        if len(patterns) < 2:
            raise ValueError('Minimum length allowed: 2.')

        return self.concat('|'.join(patterns))

    def capturing_group(self, *patterns):
        """ Adds a pattern in the form -> (patterns)"""
        patterns = ('(',) + patterns + (')',)
        return self.concat(*patterns)

    def non_capturing_group(self, *patterns):
        """ Adds a pattern in the form -> (?:patterns)"""
        patterns = ('(?:',) + patterns + (')',)
        return self.concat(*patterns)

    def positive_look_behind(self, *patterns):
        """ Adds a pattern in the form -> (?<=patterns)"""
        patterns = ('(?<=',) + patterns + (')',)
        return self.concat(*patterns)

    def negative_look_behind(self, *patterns):
        """ Adds a pattern in the form -> (?<!patterns)"""
        patterns = ('(?<!',) + patterns + (')',)
        return self.concat(*patterns)

    def positive_look_ahead(self, *patterns):
        """ Adds a pattern in the form -> (?=patterns)"""
        patterns = ('(?=',) + patterns + (')',)
        return self.concat(*patterns)

    def negative_look_ahead(self, *patterns):
        """ Adds a pattern in the form -> (?!patterns)"""
        patterns = ('(?!',) + patterns + (')',)
        return self.concat(*patterns)

    def __eq__(self, other):
        if isinstance(other, MeaningfulRE):
            return self.regex == other.regex
        return False

    def __ne__(self, other):
        if isinstance(other, MeaningfulRE):
            return self.regex != other.regex
        return False

    def __str__(self):
        return self.regex
