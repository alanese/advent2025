def get_new_pos(x, y, dir):
    match dir:
        case ">":
            return x+1, y
        case "<":
            return x-1, y
        case "^":
            return x, y+1
        case "v":
            return x, y-1
        case _:
            return x,y

santa_x = 0
santa_y = 0

visited = {(0, 0)}

with open("input-03.txt") as f:
    for line in f:
        for dir in line.strip():
            santa_x, santa_y = get_new_pos(santa_x, santa_y, dir)

            visited.add( (santa_x, santa_y) )
        
print(len(visited))

#-----------

santa_x = 0
santa_y = 0
robo_x = 0
robo_y = 0
visited = {(0,0)}
santa_move = True

with open("input-03.txt") as f:
    for line in f:
        for dir in line.strip():
            if santa_move:
                santa_x, santa_y = get_new_pos(santa_x, santa_y, dir)
                visited.add( (santa_x, santa_y) )
            else:
                robo_x, robo_y = get_new_pos(robo_x, robo_y, dir)
                visited.add( (robo_x, robo_y) )
            santa_move = not santa_move

print(len(visited))