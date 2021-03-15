class TypedTuple:
    def __init__(self, *args, **kwargs):
        self.initialize(args, kwargs)
    
    def initialize(self, args, kwargs):
        a = self.__annotations__
        names = list(a.keys())
        types = list(a.values())
        kwnames = list(kwargs.keys())
        kwvalues = list(kwargs.values())
        for i in range(len(a)):
            n, t = names[i], types[i]
            if i >= len(args):
                kwn = kwnames[i]
                it = kwvalues[i]
                if kwn != n: raise Exception(
                    f'Unknown name "{kwn}" found.'
                )
            else: it = args[i]
            valid = isinstance(it, t)
            if not valid: raise Exception(
                f'Expect Type "{t.__name__}" but "{it.__class__.__name__}"'
                f' (at name "{n}", Item {it}) found.'
            )
            setattr(self, n, it)

    def __str__(self):
        res = []
        a = self.__annotations__
        for i in a:
            res += [f'{i}={getattr(self, i)}']
        return f'{self.__class__.__name__}( {", ".join(res)} )'

    def __repr__(self):
        return str(self)

    @staticmethod
    def of(name, info):
        return type(name, (TypedTuple,), {'__annotations__': info})

    @staticmethod
    def apply(info):
        def _(cls):
            return type(cls.__name__, (cls, TypedTuple), {'__annotations__': info})
        return _
