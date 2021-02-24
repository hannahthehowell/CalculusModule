# absv stands for "absolute value."
# objects of this class represent absolute values of
# mathematical expressions.

class absv(object):
    def __init__(self, expr):
        self.__expr__ = expr

    def get_expr(self):
        return self.__expr__

    def __str__(self):
        return '|' + str(self.__expr__) + '|'

