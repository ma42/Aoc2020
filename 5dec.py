input = open('5dec.txt').read().splitlines()

def part1():
    higest_ID = 0
    for seat in input:
        binary_seat = seat.replace('F','0').replace('B', '1').replace('L','0').replace('R','1')
        row, col = int(binary_seat[:7], base=2), int(binary_seat[7:], base=2)
        seat_ID = (8*row)+col
        higest_ID = seat_ID if seat_ID > higest_ID else higest_ID
    print(higest_ID)

def part2():
    list_IDs = []
    for seat in input:
        binary_seat = seat.replace('F','0').replace('B', '1').replace('L','0').replace('R','1')
        row, col = int(binary_seat[:7], base=2), int(binary_seat[7:], base=2)
        list_IDs.append((8*row)+col)
    list_IDs.sort()
    for i, seat_ID in enumerate(list_IDs[:-1]):
        if list_IDs[i+1] - seat_ID > 1:
            print("Seat ID is: {}".format(seat_ID+1))
part2()