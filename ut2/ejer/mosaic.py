for i in range(5):
    for j in range(5):
        if i == j:
            print("X", end=" ")
        else:
            if i < j:
                print("U", end=" ")
            if i > j:
                print("D", end=" ")
    print()
