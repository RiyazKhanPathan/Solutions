# this program returns the nth day's date from given date
def leapYear(year):
    return (((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0))

def nthDay(dd,month,year,nthday=0):
    d = {   "January":31,"February":29,"March":31,"April":30,"May":31,
            "June":30,"July":31,"August":31,"September":30,"October":31,
            "November":30,"December":31
        }
    if not leapYear(year):
        d["February"] = 28
         
    months = list(d.keys())
    curr_m = months.index(month)

    while(nthday>0):
        if d[month]-dd > 0:
            dd += 1
            nthday -= 1
        else:
            curr_m += 1
            if curr_m > 11:
                curr_m = 0
                year+=1
            month = months[curr_m]
            dd = 0

    return dd,month,year



print(nthDay(28,"September",2021,nthday=366))
