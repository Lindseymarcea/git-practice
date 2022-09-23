def most_common_value(number_list):
<<<<<<< HEAD

=======
    """ returns the most common element of the list
    """
<<<<<<< HEAD
>>>>>>> dbafd3956e169a8200f881ebe025f20eb5b64820
    frequency_index = {}
    max_frequency = -1
    most_common_value = None
    for num in number_list:
        if frequency_index.get(num):
            frequency_index[num] += 1
        else:
            frequency_index[num] = 1

        if max_frequency < frequency_index[num]:
            max_frequency = frequency_index[num]
            most_common_value = num

    return most_common_value
<<<<<<< HEAD


if __name__ == "__main__":
    nums = [1, 1, 3, 3, 3, 7, 8, 2, 1, 3]
    print(f"Most common value = {most_common_value(nums)}")
=======
```
>>>>>>> dbafd3956e169a8200f881ebe025f20eb5b64820
=======
  
>>>>>>> 6c831d713ebc5092e0f1ffb53d24c4829fb19c31
