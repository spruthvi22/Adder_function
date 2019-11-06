"""
Author: Pruthvi Suryadevara
Email:  pruthvi.suryadevara@tifr.res.in
Simple code adding multiple strings, lists and float

"""
def adder(*arg):
    su=arg[0]
    for i in range(len(arg)-1):
        su=su+arg[i+1]
    return(su)

print(adder('pink',' floyd',' rocks'))
print(adder([1,2,3],[6,7,8]))
print(adder(2.3,1.8))
