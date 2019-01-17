H, W = map(int, input().split())

if H % 3 == 0 or W % 3 == 0:
    print(0)

else:
    result = []
    if ((H - 1) * W) % 2 == 0:
        r = max(W, ((H - 1) * W) // 2) - min(W, ((H - 1) * W) // 2)
    else:
        if (((H - 1) // 2 + 1) * W) - ((H - 1) // 2 * W) > (H - 1) * (W // 2 + 1) - (H - 1) * (W // 2):
            r = max(W, ((H - 1) // 2 + 1) * W) - min(W, ((H - 1) // 2) * W)
        else:
            r = max(W, (H - 1) * (W // 2 + 1)) - min(W, (H - 1) * (W // 2))
    
    for i in range(2, H):
        if ((H - i) * W) % 2 == 0:
            new_r = max(i * W, ((H - i) * W) // 2) - min(i * W, ((H - i) * W) // 2)
            if r <= new_r:
                result.append(r)
                break
            r = new_r
        else:
            if (((H - i) // 2 + 1) * W) - ((H - i) // 2 * W) > (H - i) * (W // 2 + 1) - (H - i) * (W // 2):
                new_r = max(i * W, ((H - i) // 2 + 1) * W) - min(i * W, ((H - i) // 2) * W)
            else:
                new_r = max(i * W, (H - i) * (W // 2 + 1)) - min(i * W, (H - i) * (W // 2))
            if r <= new_r:
                result.append(r)
                break
            r = new_r

    if not result:
        result.append(r)

    if ((W - 1) * H) % 2 == 0:
        r = max(H, ((W - 1) * H) // 2) - min(H, ((W - 1) * H) // 2)
    else:
        if (((W - 1) // 2 + 1) * H) - ((W - 1) // 2 * H) > (W - 1) * (H // 2 + 1) - (W - 1) * (H // 2):
            r = max(H, ((W - 1) // 2 + 1) * H) - min(H, ((W - 1) // 2) * H)
        else:
            r = max(H, (W - 1) * (H // 2 + 1)) - min(H, (W - 1) * (H // 2))
    
    for i in range(2, W):
        if ((W - i) * H) % 2 == 0:
            new_r = max(i * H, ((W - i) * H) // 2) - min(i * H, ((W - i) * H) // 2)
            if r <= new_r:
                result.append(r)
                break
            r = new_r
        else:
            if (((W - i) // 2 + 1) * H) - ((W - i) // 2 * H) > (W - i) * (H // 2 + 1) - (W - i) * (H // 2):
                new_r = max(i * H, ((W - i) // 2 + 1) * H) - min(i * H, ((W - i) // 2) * H)
            else:
                new_r = max(i * H, (W - i) * (H // 2 + 1)) - min(i * H, (W - i) * (H // 2))
            if r <= new_r:
                result.append(r)
                break
            r = new_r

    if len(result) == 1:
        result.append(r)

    print(min(result))
