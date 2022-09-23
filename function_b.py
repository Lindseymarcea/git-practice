# Taken From
# Iterating Over Data
# Problem-Set While Loops #11
def silly_sum():
    ""sdfadfasfdf

def most_common_value(number_list):
    """ returns the most common element of the list
    """
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
```
if __name__ == "__main__":
    print(f"Answer = {silly_sum()}")
