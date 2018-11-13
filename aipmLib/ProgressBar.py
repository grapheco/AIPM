import sys

def view_bar(num, total):
    rate = num / total  # get the rate，0<rate<1
    rate_num = int(rate * 100)  # trans to precent_rate，0<rate_num<100
    r = '\r[%s%s]' % (">" * rate_num, " " * (100 - rate_num))  # make the progress bar
    sys.stdout.write(r)  # show the progress bar
    sys.stdout.write(str(rate_num) + '%')  # show the precent rate
    sys.stdout.flush()  # flush the output
