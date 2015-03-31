#!/usr/bin/python

#produce random values for kafka queue

# The following values are spit out in each message (comma seperated)
# svisattrN, tvisattrN, ivisattrN, rsid, dsid, visid_high, visid_low

import datetime
import random
from random import randrange
from datetime import timedelta

def random_date(start, end):
    """
    This function will return a random datetime between two datetime objects.
    """
    delta = end - start
    int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
    random_second = randrange(int_delta)
    return start + timedelta(seconds=random_second)


d1 = datetime.datetime.strptime('1/1/2003 1:30 PM', '%m/%d/%Y %I:%M %p')
d2 = datetime.datetime.strptime('1/1/2014 4:50 AM', '%m/%d/%Y %I:%M %p')

# print random_date(d1, d2)
# print random_date(d1, d2).strftime("%s")

from random import randint

while True:
	""" creating single message (comma seperated) """
	message_out = ''

	s = 'svisattr'
	random_num_s = randint(2,10)
	# print random_num_s
	for i in range(random_num_s):
		if i == 0:
			continue
		if i < random_num_s:
			message_out = message_out + s + str(i) + '=' + str(i) + ','

	j = 'ivisattr'
	random_num_s = randint(2,10)
	for i in range(random_num_s):
		if i == 0:
			continue
		if i < random_num_s:
			message_out = message_out + j + str(i) + '=' + str(i) + ','

	t = 'tvisattr'
	random_num_s = randint(2,10)
	for i in range(random_num_s):
		if i == 0:
			continue
		if i < random_num_s:
			message_out = message_out + t + str(i) + '=' + random_date(d1,d2).strftime("%s") + ','

	message_out = message_out + 'rsid=' + 'rsid' + str(randint(1,100)) + ','
	message_out = message_out + 'dsid=' + 'dsid' + str(randint(1,100)) + ','

	message_out = message_out + 'visid_high=' + str(random.getrandbits(64)) + ','
	message_out = message_out + 'visid_low=' + str(random.getrandbits(64))

	print message_out













