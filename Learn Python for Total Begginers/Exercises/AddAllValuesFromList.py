nest1 = [
    (1,2,3),
    {
        "k1": [8, 1, 300, 2, 77],
         "k2": [10,20,30]
    },
    ["a", "500", "c"]
    ]

item1 = nest1[0][2]
print(item1)

item2 = nest1[1]["k1"][2]
print(item2)

item3 = nest1[1]["k2"][2]
print(item3)

item4 = nest1[2][1]
print(item4)

sum1 = [item1, item2, item3, item4]
print(eval("{} + {} + {} + {}".format(*sum1)))