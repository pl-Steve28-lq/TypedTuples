from typedtuples.utils import toString

class TypedTuple:
    def __init__(self, *args, **kwargs):
        self.initialize(args, kwargs)
    
    def initialize(self, args, kwargs):
        a = self.__annotations__
        
        names, types = zip(*a.items())
        kwnames, kwvalues = zip(*kwargs.items())if kwargs else((),())
        
        for i in range(len(a)):
            n, t = names[i], types[i]
            isKw = i >= len(args)
            it = (kwvalues if isKw else args)[i - len(args)*isKw]
            
            if isKw:
                if kwnames[i-len(args)] != n:
                    raise Exception(f'Unknown name "{kwn}" found.')

            valid = isinstance(it, t)
            if not valid: self.raiseTypeException(
                t.__name__, it.__class__.__name__, n, toString(it)
            )
            setattr(self, n, it)

    def raiseTypeException(self, expect, wrong, name, item):
        raise Exception(
            f'Expected Type "{expect}" but "{wrong}" found.'
            f' (at name "{name}", Item {item})'
        )

    def __str__(self):
        res = []
        a = self.__annotations__
        for i in a:
            res += [f'{i}={toString(getattr(self, i))}']
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
