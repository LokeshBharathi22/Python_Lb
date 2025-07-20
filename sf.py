def towers_of_hanoi(n, source, target, auxiliary):
 if n == 1:
    print(f"Move disk from {source} to {target}")
 else:
    towers_of_hanoi(n - 1, source, auxiliary, target)
    print(f"Move disk from {source} to {target}")
    towers_of_hanoi(n - 1, auxiliary, target, source)

 number_of_disks = int(input("Enter the number of disks: "))
 towers_of_hanoi(number_of_disks, 'A', 'C', 'B')
