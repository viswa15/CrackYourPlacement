def sort_0s_1s_2s(head):
    if not head or not head.next:
        return head
    cnt = [0,0,0]
    pnt = head

    while pnt:
        cnt[pnt.val] += 1
        pnt = pnt.next

    pnt = head
    idx = 0
    while pnt:
        if cnt[idx] > 0:
            pnt.val = idx
            cnt[idx] -= 1
            pnt = pnt.next
        else:
            idx += 1

    return head