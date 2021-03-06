"""Bucket Sort"""
def radix_sort(array, base=10):
    def list_to_buckets(array, base, iteration):
        buckets = [[] for x in range(base)]
        # iterate through the input array of number
        for number in array:
            # Isolate the base-digit from the number
            # dividing by base to power of iteration to add
            # to correct bucket per digist starting at LSD.
            digit = (number // (base ** iteration)) % base
            # Drop the number into the correct bucket
            # Put number in correct bucket for this iteration.
            buckets[digit].append(number)
        print(buckets)
        return buckets

    def buckets_to_list(buckets):
        numbers = []
        for bucket in buckets:
            # append the numbers in a bucket
            # sequentially to the returned array
            for number in bucket:
                numbers.append(number)
        return numbers

    maxval = max(array)

    it = 0
    # Iterate, sorting the array by each base-digit
    while base ** it <= maxval:
        array = buckets_to_list(list_to_buckets(array, base, it))
        it += 1

    return array


if __name__=="__main__":
  li = [43, 2, 1, 5, 34, 200, 132]
  print("Unsorted ", li)
  print("Sorted ", radix_sort(li))