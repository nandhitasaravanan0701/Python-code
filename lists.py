def is_leap(year):
   
    return (year % 4 == 0) and (year % 100 != 0 or year % 400 == 0)

if __name__ == '__main__':
    
    my_list = []
    
   
    try:
        N = int(input())
    except EOFError:
        N = 0

    for _ in range(N):
       
        parts = input().split()
        cmd = parts[0]
        args = parts[1:]
        
        
        if cmd == "insert":
            my_list.insert(int(args[0]), int(args[1]))
        elif cmd == "print":
            print(my_list)
        elif cmd == "remove":
            my_list.remove(int(args[0]))
        elif cmd == "append":
            my_list.append(int(args[0]))
        elif cmd == "sort":
            my_list.sort()
        elif cmd == "pop":
            my_list.pop()
        elif cmd == "reverse":
            my_list.reverse()
