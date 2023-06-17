# 방 번호
import math 

room_number = input()

num_dict = dict()

for i in room_number:
    if i not in num_dict:
        num_dict[i] = 1

    else:
        num_dict[i] += 1

if "6" in num_dict and "9" in num_dict:
    num_dict["69"] = (num_dict["6"] + num_dict["9"]) / 2

    del num_dict["6"]
    del num_dict["9"]

elif "6" in num_dict and "9" not in num_dict:
    num_dict["69"] = num_dict["6"] / 2
    del num_dict["6"]

elif "9" in num_dict and "6" not in num_dict:
    num_dict["69"] = num_dict["9"] / 2
    del num_dict["9"]
    

print(math.ceil(max(num_dict.values())))