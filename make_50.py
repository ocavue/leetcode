"""
给一个字符串"123456789",
在任意字符中间插入“+”、“-”、“*”、“/”四种运算符，使最后的计算结果等于50。
例如你可以如此插入：1*2*3*4-56-7+89，使这个式子的最终结果等于50。
输出所有可能的式子结果。
"""

from typing import List, Union, Tuple, Iterable, Set, cast
from typing_extensions import Literal
from functools import lru_cache

OpToken = Union[Literal["+"], Literal["-"], Literal["*"], Literal["/"]]
Token = Union[int, OpToken]
Formula = Tuple[Token, ...]


def split_nums(nums: str) -> Iterable[Tuple[str, str]]:
    """
    >>> list(split_nums("11"))
    [('1', '1')]
    >>> list(split_nums("123"))
    [('1', '23'), ('12', '3')]
    """

    assert len(nums) >= 2

    for i in range(1, len(nums)):
        start = nums[:i]
        reset = nums[i:]
        yield (start, reset)


def calcate_operation(a: int, op: str, b: int):
    return eval("{} {} {}".format(a, op, b))


def calcate_formula(formula: Formula):
    """
    >>> calcate_formula((1, '+', 10, '*', 10, '-', 2, '/', 4))
    100.5
    """

    nums: List[int] = []
    ops: List[OpToken] = []

    for token in formula:
        if isinstance(token, str):
            assert token in ["+", "-", "*", "/"], f"wrong token: {repr(token)}"
            ops.append(token)
        else:
            assert isinstance(token, int)
            if ops and ops[-1] in "*/":
                prev_num = nums.pop()
                prev_op = ops.pop()
                result = calcate_operation(prev_num, prev_op, token)
                nums.append(result)
            else:
                nums.append(token)

    assert len(ops) == len(nums) - 1

    for i, op in enumerate(ops):
        assert op in "+-"
        if op == "-":
            nums[i + 1] *= -1

    return sum(nums)


@lru_cache()
def iter_formulas(nums: str, operators: str = "+-*/") -> List[Formula]:
    """
    >>> iter_formulas('111', '+')
    [(111,), (1, '+', 11), (11, '+', 1), (1, '+', 1, '+', 1)]
    """
    assert nums.isdigit()
    assert len(nums) >= 1

    fs: List[Formula] = [(int(nums),)]

    if len(nums) == 1:
        return fs

    for head, tail in split_nums(nums):
        for o in operators:
            assert o in ["+", "-", "*", "/"]
            for formula in iter_formulas(head, operators):
                fs.append((*formula, cast(OpToken, o), int(tail)))
    return fs


def make_formulas(nums: str, target: float) -> Set[Formula]:
    assert nums.isdigit()

    if int(nums) == target:
        return set([(int(nums),)])
    elif len(nums) <= 1:
        return set()
    else:
        formulas: Set[Formula] = set()

        for head, tail in split_nums(nums):
            assert head + tail == nums
            assert len(head) >= 1
            assert len(tail) >= 1

            # f(head) + tail = target
            for head_formula in make_formulas(str(head), target=target - int(tail)):
                formulas.add((*head_formula, "+", int(tail)))

            # f(head) - tail = target
            for head_formula in make_formulas(str(head), target=int(tail) + target):
                formulas.add((*head_formula, "-", int(tail)))

            # ...head * tail = target
            # ...head / tail = target
            for head_formula in iter_formulas(str(head)):
                f1: Formula = (*head_formula, "*", int(tail))
                f2: Formula = (*head_formula, "/", int(tail))
                for f in [f1, f2]:
                    if calcate_formula(f) == target:
                        formulas.add(f)

        return formulas


def format_formula(formula: Formula) -> str:
    return "".join([str(i) for i in formula])


def make_50(nums: str) -> List[str]:
    result = [format_formula(f) for f in make_formulas(nums, 50)]
    print("DEBUG: formulas number is", len(result))
    return result


if __name__ == "__main__":
    import doctest

    doctest.testmod()

# 不要修改下面的部分
if __name__ == "__main__":
    results = make_50("123456789")
    for result in results:
        assert eval(result) == 50
    print("OK")
