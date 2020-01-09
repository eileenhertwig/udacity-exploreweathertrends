import csv
import matplotlib.pyplot as plt
import numpy as np

f_glob = open('global.csv')
f_hh = open('hamburg.csv')

d_glob = csv.reader(f_glob)
d_hh = csv.reader(f_hh)

glob = []
hh = []
years = []

rownum = 0
for row in d_glob:
    if rownum==0:
        header = row
    else:
        years.append(int(row[0]))
        if row[1] == '':
            glob.append(np.nan)
        else:
            glob.append(float(row[1]))
    rownum += 1
    
rownum = 0
for row in d_hh:
    if rownum==0:
        header = row
    else:
        if row[1] == '':
            hh.append(None)
        else:
            hh.append(float(row[1]))
    rownum += 1
    
glob = glob[:-2]
hh = hh[7:]
years = years[:-2]

def ma(data,n):
    s = [0]
    r = []
    for i,t in enumerate(data,1):
        s.append(s[i-1]+t)
        if i >= n:
            r.append((s[i] - s[i-n])/n)
    return r

MA5_glob = ma(glob,5)
MA5_hh = ma(hh,5)
MA5 = zip(years[2:-2],MA5_glob,MA5_hh)

MA11_glob = ma(glob,11)
MA11_hh = ma(hh,11)
MA11 = zip(years[5:-5],MA11_glob,MA11_hh)

MA31_glob = ma(glob,31)
MA31_hh = ma(hh,31)
MA31 = zip(years[15:-15],MA31_glob,MA31_hh)

MA51_glob = ma(glob,51)
MA51_hh = ma(hh,51)
MA51 = zip(years[25:-25],MA51_glob,MA51_hh)


plt.plot(years[2:-2],MA5_glob,color='blue',label='global',linewidth=2)
plt.plot(years[2:-2],MA5_hh,color='green',label='Hamburg',linewidth=2)
plt.scatter(years,glob,s=2,c='blue',alpha=0.5)
plt.scatter(years,hh,s=2,color='green',alpha=0.5)
plt.xlim(1750,2013)
plt.ylim(5.5,10.5)
plt.legend(loc='lower right')
plt.xlabel("years")
plt.ylabel("temperature [$^{o}$C]")
plt.title("5-year moving average")
plt.savefig("MA5.png")
plt.close()


plt.plot(years[5:-5],MA11_glob,color='blue',label='global',linewidth=2)
plt.plot(years[5:-5],MA11_hh,color='green',label='Hamburg',linewidth=2)
plt.scatter(years,glob,s=2,c='blue',alpha=0.5)
plt.scatter(years,hh,s=2,color='green',alpha=0.5)
plt.xlim(1750,2013)
plt.ylim(5.5,10.5)
plt.legend(loc='lower right')
plt.xlabel("years")
plt.ylabel("temperature [$^{o}$C]")
plt.title("11-year moving average")
plt.savefig("MA11.png")
plt.close()


plt.plot(years[15:-15],MA31_glob,color='blue',label='global',linewidth=2)
plt.plot(years[15:-15],MA31_hh,color='green',label='Hamburg',linewidth=2)
plt.scatter(years,glob,s=2,c='blue',alpha=0.5)
plt.scatter(years,hh,s=2,color='green',alpha=0.5)
plt.xlim(1750,2013)
plt.ylim(5.5,10.5)
plt.legend(loc='lower right')
plt.xlabel("years")
plt.ylabel("temperature [$^{o}$C]")
plt.title("31-year moving average")
plt.savefig("MA31.png")
plt.close()


plt.plot(years[25:-25],MA51_glob,color='blue',label='global',linewidth=2)
plt.plot(years[25:-25],MA51_hh,color='green',label='Hamburg',linewidth=2)
plt.scatter(years,glob,s=2,c='blue',alpha=0.5)
plt.scatter(years,hh,s=2,color='green',alpha=0.5)
plt.xlim(1750,2013)
plt.ylim(5.5,10.5)
plt.legend(loc='lower right')
plt.xlabel("years")
plt.ylabel("temperature [$^{o}$C]")
plt.title("51-year moving average")
plt.savefig("MA51.png")
plt.close()

