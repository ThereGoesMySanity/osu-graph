import requests
import matplotlib.pyplot as plt
url="https://osu.ppy.sh/api/get_user_best"
key=""
user=""
mode=0
response=requests.get(url, params=
						{"k":key,
						"u":user,
						"m":mode,
						"limit":100,
						"type":"string"
						}
l = list()
for i in response.json():
	l.add(float(i["pp"]))
	y= range(len(l))
m= [l[i]*0.95^^i for i in y]
n= [sum(q for q in m[:i]) for i in y] #partial sums
plt.plot(l,y,m,y,n,y)