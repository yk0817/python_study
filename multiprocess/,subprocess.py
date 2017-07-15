import subprocess as sub


# ret = sub.getoutput('date')
# print(ret)
# 
# ret2 = sub.getoutput('date -u')
# print(ret2)
# 
# ret3 = sub.getoutput('date -u | wc')
# print(ret3)
# 
# ret4 = sub.check_output(['date', '-u'])
# print(ret4)

ret5 = sub.call(['date', '-u'])
