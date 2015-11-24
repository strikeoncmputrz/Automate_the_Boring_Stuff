import pprint

message = 'It was a bright cold day in April, and the clocks were stiking thirteen.'

count = {}

for chr in message:
	count.setdefault(chr, 0)
	count[chr] = count[chr] + 1

pprint.pprint(count)
