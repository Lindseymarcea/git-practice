def most_common_value(number_list):
<<<<<<< HEAD

=======
    """ returns the most common element of the list
    """
   #HIYA HERE'S JAIME'S VERSION. 
def most_common_value(number_list):
    """ returns the most common element of the list
    """
>>>>>>> bb6ae4fa94c4e6cdce4c6bf2a38a01d4d4f76090
    frequency_index = {}
    max_frequency = -1
    most_common_value = None
    for num in number_list:
        if frequency_index.get(num):
            frequency_index[num] += 1
        else:
            frequency_index[num] = 1
<<<<<<< HEAD

        if max_frequency < frequency_index[num]:
            max_frequency = frequency_index[num]
            most_common_value = num

    return most_common_value
=======
>>>>>>> bb6ae4fa94c4e6cdce4c6bf2a38a01d4d4f76090

        # if max_frequency < frequency_index[num]:
        #     max_frequency = frequency_index[num]
        #     most_common_value = num

    return most_common_value
if __name__ == "__main__":
    nums = [1, 1, 3, 3, 3, 7, 8, 2, 1, 3]
    print(f"Most common value = {most_common_value(nums)}")
