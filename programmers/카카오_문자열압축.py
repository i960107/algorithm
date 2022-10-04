def get_maximum_compressed_length(s: str) -> int:
    def get_compressed_length_by_unit(unit: int) -> int:
        i = 0
        prev = ""
        count = 1
        compressed_length = 0
        compressed = ""
        while i < len(s):
            curr = s[i:i + unit]

            if prev == curr:
                count += 1

            else:
                if count == 1:
                    compressed_length += len(prev)
                    compressed += prev
                else:
                    compressed_length += (1 + len(prev))
                    compressed += str(count) + prev
                prev = curr
                count = 1

            i += unit

        if count == 1:
            compressed_length += len(prev)
            compressed += prev

        else:
            compressed_length += (1 + len(prev))
            compressed += str(count) + prev

        # print("단위", unit, ":", compressed, "길이", compressed_length)
        return compressed_length

    answer = len(s)

    for unit in range(1, (len(s) // 2) + 1):
        answer = min(answer, get_compressed_length_by_unit(unit))

    return answer


print(get_maximum_compressed_length("aabbaccc"))
print(get_maximum_compressed_length("ababcdcdababcdcd"))
print(get_maximum_compressed_length("abcabcdede"))
print(get_maximum_compressed_length("abcabcabcabcdededededede"))
print(get_maximum_compressed_length("xababcdcdababcdcd"))
