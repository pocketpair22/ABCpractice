sx, sy, tx, ty = map(int, input().split())

ans = 'R' * (tx-sx) + 'U' * (ty-sy) + 'L' * (tx-sx) + 'D' * (ty-sy+1)
ans += 'R' * (tx-sx+1) + 'U' * (ty-sy+1) + 'LU' + 'L' * (tx-sx+1) + 'D' * (ty-sy+1) + 'R'

print(ans)
