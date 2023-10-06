from __future__ import annotations


def string_special(s: str, string_list: list[str]) -> bool:
    curr_str = s
    while curr_str:
        for comp_str in reversed(string_list):
            val = s.find(comp_str)
            if val != -1:
                curr_str = curr_str[:val] + curr_str[val + len(comp_str) :]
                break
        else:
            return False
    return True


def good_longest_streak(arr: list[int]) -> int:
    # convert list of 1s and 0s to sequence of tuples
    curr, streak, seq = arr[0], 1, []
    for val in arr[1:]:
        if curr != val:
            seq.append((streak, curr))
            curr, streak = val, 1
        else:
            streak += 1
    seq.append((streak, curr))

    # iterate over tuples, getting largest streak
    idx_max, val_max = -1, 0
    idx_curr, len_seq = 0, len(seq)
    for idx, (streak, val) in enumerate(seq):
        if val == 1:
            idx_curr += streak
            continue

        left = seq[idx - 1][0] if idx > 0 else 0
        right = seq[idx + 1][0] if idx < len_seq - 1 else 0

        if streak == 1:
            val_curr = left + right + 1
            idx_zero = idx_curr
        else:
            if left >= right:
                val_curr = left + 1
                idx_zero = idx_curr  # zero at beginning for left streak
            else:
                val_curr = right + 1
                idx_zero = idx_curr + streak - 1  # zero at end for right streak
            # if left is larger, we need
            val_curr = max(left, right) + 1
        idx_curr += streak

        # check and set the max if needed
        if val_curr > val_max:
            val_max = val_curr
            idx_max = idx_zero
    return idx_max


def bad_longest_streak(arr: list[int]) -> int:
    idx_max, max_len = -1, 0
    idx_a, a_len, idx_b, b_len = -1, 0, -1, 0

    for idx, val in enumerate(arr):
        if val == 1:
            a_len += 1
        else:
            a_len += 1
            b_len += 1
            idx_b = idx
            break
    else:
        return -1

    for idx, val in enumerate(arr[idx_a + 1 :]):
        if val == 1:
            a_len += 1
            b_len += 1
        else:
            if max_len < a_len:
                max_len = a_len
                idx_max = idx_a
            a_len, idx_a = b_len, idx_b
            b_len = 1
            idx_b = idx
    return idx_max
