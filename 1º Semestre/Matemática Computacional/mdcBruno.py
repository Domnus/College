#MDC2
def __mdc_(x,y):
    while(y):
        x,y=y,x%y
    return x

def mdc(nums):

    if len(nums) == 2:
        return __mdc_(nums[0], nums[1])
    else:
        mdc_val = __mdc_(nums[0], nums[1])
        nums[0] = mdc_val
        del nums[1]
        return mdc(nums)

print(mdc([60, 24, 36]))
