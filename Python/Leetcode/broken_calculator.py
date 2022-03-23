class Solution(object):
  def brokenCalc(self, startValue, target):
    """
    :type startValue: int
    :type target: int
    :rtype: int
    """
    muls = 0
    subs = 0
    curr = 0
    if target < startValue:
      return startValue - target
    else:
      curr = target
      while curr > startValue:
        if curr % 2 == 0:
          curr = curr / 2
          muls += 1
        else:
          curr += 1
          subs += 1
    return subs + muls + (startValue - curr)