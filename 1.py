#!/usr/bin/python3
i=j=k=1
for i in range(1,5):
	for j in range(1,5):
		for k in range(1,5):
			if (i!=k) and (k!=j) and (i!=j):
				print(i,j,k)
