import functools
"""
By using this utils, you can set a value to a list
"""


def rsetattr(obj, attr, val):
    pre, _, post = attr.rpartition('.')
    return setattr(rgetattr(obj, pre) if pre else obj, post, val)
    """
    How to use:

    Simple String:
        rsetattr(res, "plan.name", "Nama Plan")

    List:
        age_validation = {
            "loc": "dob",
            "msg": f"Usia masuk mulai {min_age} - {max_age} tahun",
            "type": "value_error.not_match"}

        # Set Validation
        rsetattr(res, "validation", [age_validation])
    """


def rgetattr(obj, attr, *args):
    def _getattr(obj, attr):
        return getattr(obj, attr, *args)
    return functools.reduce(_getattr, [obj] + attr.split('.'))
    """
    How to use:

    p = Person()
    print(rgetattr(p, 'pet.favorite.color', 'calico'))
    """
