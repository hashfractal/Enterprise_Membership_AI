
def solution(skill: str, skill_trees: [str]):
    slist = ""
    for i in skill_trees:
        if i in skill:
            slist += i

    for i in range(len(slist)):
        if slist[i] != skill[i]:
            print(f"{slist[i]}스킬을 배우기 전에 {skill[i]} 스킬을 먼저 배워야 합니다 불가능한 스킬트리입니다")
            return
    print("가능한 스킬트리 입니다.")
    return

solution("CBD", "BACDE")
solution("CBD", "CBADF")
solution("CBD", "AECB")
solution("CBD", "BDA")

# print(f"{skill[j]}스킬을 배우기 전에 {i} 스킬을 먼저 배워야 합니다 불가능한 스킬트리입니다")
# return
# print("가능한 스킬트리 입니다.")
