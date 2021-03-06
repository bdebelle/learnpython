import collections 

def new(num_buckets=256):
	"""Initializes a Map with the given number of buckets."""
	aMap =[] # This is a List
	for i in range(0, num_buckets): # Creates more lists inside aMap
		aMap.append([]) # Creates more lists inside aMap
	return aMap

def hash_key(aMap, key):
	"""Given a key this will create a number and then convert it to
	an index for the aMap's bucket."""
	return hash(key) % len(aMap)

def get_bucket(aMap, key):
	"""Given a key, find the bucket where it would go"""
	bucket_id = hash_key(aMap, key)
	return aMap[bucket_id]

def get_slot(aMap, key, default=None):
	"""
	Returns the index key, and value of a slot found in a bucket.
	returns -1, key, and default (None if not set) when not found/
	"""
	bucket = get_bucket(aMap, key)

	for i, kv in enumerate(bucket):
		k, v = kv
		if key == k:
			return i, k, v
	return -1, key, default

def get(aMap, key, default=None):
	"""Gets the value in a bucket for the given key, or the default."""
	i, k, v = get_slot(aMap, key, default=default)
	return v

def set(aMap, key, value):
	"""Sets the key to the value, replacing and existing value."""
	bucket = get_bucket(aMap, key)
	i, k, v = get_slot(aMap, key)

	if i >= 0:
		#the key exists, replace it
		bucket[i] = (key, value)
	else:
		# the key does not, append to create it
		bucket.append((key, value))

def delete(aMap, key):
	"""Deletes the given key from the map."""
	bucket = get_bucket(aMap, key)

	for i in xrange(len(bucket)):
		k, v = bucket[i]
		if key == k:
			del bucket[i]
			break

def list(aMap):
	"""Prints out whats in the map. """
	for bucket in aMap:
		if bucket:
			for k, v in bucket:
				print k, v
				

			
# I dont believe this is what the study drill had in mind 
#but it works to print all the contents of the dictionary
def dump(aMap, foo):
	for states in enumerate(aMap):
		print states
	for cities in enumerate(foo):
		print cities

