from unittest import result


class SortBox:

	def count(self, arr):
		count = [0] * (max(arr) + 1)

		for num in arr:
			count[num] += 1
	
		for i in range(1, len(count)):
			count[i] += count[i-1]

		result = [0] * (len(arr))

		for num in arr:
			idx = count[num]
			result[idx - 1] = num
			count[num] -= 1

		return result

	def bucket(self, seq):
		# make buckets
		buckets =  [[] for _ in range(len(seq))]
		# assign values
		for value in seq:
			bucket_index = value * len(seq) // (max(seq) + 1)
			buckets[bucket_index].append(value)
		# sort & merge
		sorted_list = []
		for bucket in buckets:
			sorted_list.extend(self.quick(bucket))
		return sorted_list

	def quick(self, ARRAY):
		ARRAY_LENGTH = len(ARRAY)
		if( ARRAY_LENGTH <= 1):
			return ARRAY
		else:
			PIVOT = ARRAY[0]
			GREATER = [ element for element in ARRAY[1:] if element > PIVOT ]
			LESSER = [ element for element in ARRAY[1:] if element <= PIVOT ]
			return self.quick(LESSER) + [PIVOT] + self.quick(GREATER)

	def enqueue(self,queue,data): queue.append(data)
	def dequeue(self, queue):
		if len(queue) == 0:
			print('Empty')
			return -1  
		else:
			data = queue.pop(0)
			return data
	def digit(self, d,k):
		temp = 1
		for _ in range(1,k):
			temp *= 10
		d = int(d/temp)
		d %= 10
		return d

	def radix(self, arr):
		queue = [[], [], [], [], [], [], [], [], [], []]
		n = len(arr)
		m = len(str(max(arr)))
		arr.insert(0, "")
		for k in range(1,m+1):
			for i in range(1,n+1):
				kd = self.digit(arr[i],k)
				self.enqueue(queue[kd],arr[i])
			p=0
			for i in range(10):
				while len(queue[i]) != 0:
					p += 1
					arr[p] = self.dequeue(queue[i])
		arr.pop(0)


if __name__ == "__main__":
	SB = SortBox()
	arr = [3, 2, 1, 5, 6, 9, 7, 8, 4]

	result = SB.count(arr)
	print("Count sort: ", result)

	res2 = SB.bucket(arr)
	print("Bucket sort: ", res2)

	SB.radix(arr)
	print(arr)