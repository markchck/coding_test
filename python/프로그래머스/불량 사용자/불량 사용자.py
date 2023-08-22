from itertools import permutations


def check(case, banned_id):
    for i in range(len(banned_id)):
        if len(case[i]) != len(banned_id[i]):
            return False
        for j in range(len(case[i])):
            if banned_id[i][j] == '*':
                continue
            if banned_id[i][j] != case[i][j]:
                return False
    return True


def solution(user_id, banned_id):
    answer = []
    user_permutation = list(permutations(user_id, len(banned_id)))

    for case in user_permutation:
        if not check(case, banned_id):
            continue
        else:

            case = set(case)

            if case not in answer:
                answer.append(case)
    return len(answer)


solution(["frodo", "fradi", "crodo", "abc123", "frodoc"],
         ["fr*d*", "*rodo", "******", "******"])


# def solution(user_id, banned_id):
#     # *가 와서 어떤 문자가 와도 되는 경우가 있고
#     # 특정 문자가 와서 그 문자만 와야하는 경우도 있음.
#     answer = []
#     for banned in banned_id:
#         lenB = len(banned)
#         # 단어 길이로 먼저 필터링하자
#         for user in user_id:
#             userLength = len(user)
#             if lenB == userLength:
#                 for i in range(lenB):
#                     if banned[i] == '*':
#                         continue
#                     else:
#                         if user[i] != banned[i]:
#                             break
#                 else:
#                     answer.append([banned, user])
#                 continue
#     print(answer)


solution(["frodo", "fradi", "crodo", "abc123", "frodoc"],
         ["fr*d*", "*rodo", "******", "******"])
