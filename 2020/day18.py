f = open("day18.txt").read().splitlines()


def eval_exp(exp, nums, ops):
    # print(exp, nums, ops)
    if len(exp) == 0:
        while(len(ops) != 0):
            if ops[-1] == '+':
                a = nums.pop()
                b = nums.pop()
                op = ops.pop()
                nums.append(calc(a,b,op))
            else:
                a = nums.pop()
                b = nums.pop()
                op = ops.pop()
                # a = nums.pop(0)
                # b = nums.pop(0)
                # op = ops.pop(0)
                # print('{} {} {}'.format(a, op, b))
                nums.insert(0, calc(a,b,op))
        return nums[0]

    if not (exp[0] in ['+','-','*','/','(',')']):
        nums.append(int(exp[0]))
        return eval_exp(exp[1:], nums, ops)
    elif exp[0] in ['+','-','*','/']:
        if exp[0] == '+' or not (exp[0] in ['*'] and (len(ops) != 0 and ops[-1] == '+')):
            ops.append(exp[0])
            return eval_exp(exp[1:], nums, ops)
        else:
            while not (len(ops) == 0 or (ops[-1] != '+')):
                a = nums.pop()
                b = nums.pop()
                op = ops.pop()
                # print('{} {} {}'.format(a, op, b))
                nums.append(calc(a,b,op))
            ops.append(exp[0])
            return eval_exp(exp[1:], nums, ops)
    elif exp[0] == '(':
        ops.append(exp[0])
        return eval_exp(exp[1:], nums, ops)
    elif exp[0] == ')':
        while not ops[-1] == '(':
            if ops[-1] == '+':
                a = nums.pop()
                b = nums.pop()
                op = ops.pop()
                nums.append(calc(a,b,op))
            else:
                i = len(ops)-1
                idx = 0
                while i > 0:
                    if ops[i] == '(':
                        idx = i
                        break
                    i-=1
                # print('i', len(ops)-i)
                a = nums.pop(-(len(ops)-i))
                b = nums.pop(-(len(ops)-i)+1)
                op = ops.pop(i+1)
                # print('{} {} {}'.format(a,op,b))
                nums.insert(i,calc(a,b,op))
        ops.pop()
        return eval_exp(exp[1:], nums, ops)


def calc(a, b, op):
    if op == '+': return a + b
    elif op == '-': return a - b
    elif op == '*': return a * b
    elif op == '/': return a / b


silver = 0
for line in f:
    line = line.strip()
    line = line.replace('(', '( ')
    line = line.replace(')', ' )')
    ans = eval_exp(line.split(' '), [], [])
    print('ans ', ans)
    silver += ans
print('gold', silver) # wrote over part 1 for this.


