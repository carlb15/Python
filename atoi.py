"""My atoi function."""
import re


def myAtoi(str):
    """Convert string to integer."""
    """
    :type str: str
    :rtype: int
    """
    str = str.strip()
    str = re.findall('^[+\-]?\d+', str)
    print("String after findall %s" % str)
    try:
        res = int(''.join(str))
        MAX = 2147483647
        MIN = -2147483648
        if res > MAX:
            return MAX
        elif res < MIN:
            return MIN
        return res
    except:
        return 0


if __name__ == "__main__":
    assert(myAtoi("1234") == 1234)
    assert(myAtoi('-213e1000') == -213)
    assert(myAtoi('213e1000') == 213)
    assert(myAtoi('-+213') == 0)
    assert(myAtoi('+213') == 213)
    assert(myAtoi('-') == 0)
    assert(myAtoi('-213') == -213)
    assert(myAtoi('+') == 0)
    assert(myAtoi('-safsadfj') == 0)
    assert(myAtoi('safsadfj') == 0)
    assert(myAtoi('=sf=-safsadfj') == 0)
    assert(myAtoi('       234234    safds') == 234234)
