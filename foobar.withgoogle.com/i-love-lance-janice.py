def decrypt(letter):
    if letter.isalpha() and letter.islower():
        return chr(ord('a') + ord('z') - ord(letter))
    return letter

def solution(x):
    return "".join(map(decrypt, x))

print(solution(input()))