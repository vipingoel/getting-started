import sys


def compute_lps(pat):
    # computes longest proper prefix which is also a suffix
    # for string ending from 1 to length of pattern
    n = len(pat)
    lps = [0]*n
    for i in range(1, n):
        sub = pat[:i+1]

        j = i
        # longest proper prefix
        while j >= 0:
            if str.endswith(sub, sub[:j]):
                lps[i] = j
                break
            j -= 1
    return lps


def search(txt, pat):
    lps = compute_lps(pat)
    # print(lps)
    matched_at = []
    n = len(txt)
    m = len(pat)

    i = 0
    j = 0
    while i < n:
        while j < m:
            # print(i, j)
            if txt[i] == pat[j]:
                j += 1
                i += 1
            else:
                break
        else:
            # print("matched: ", i, j)
            matched_at.append(i-m)

        # reset j
        if j == 0:
            # no more next index to match, so lets start searching from next char again
            i += 1
        else:
            j = lps[j-1]

    return matched_at


# Write your code here
if __name__ == "__main__":
    pat = sys.stdin.readline().strip()
    txt = sys.stdin.readline().strip()
    print(search(txt, pat))
