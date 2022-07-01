def solution(id_list, report, k):
    #중복 횟수 구하기
    report_set = list(set(report))

    ids = []
    for name in id_list:
        ids.append([name])
    
    # id별 신고 당한 횟수 구하기
    for user_bad in report_set:
        user, bad = user_bad.split(' ')
        idx = id_list.index(bad)
        ids[idx].append(user)

    # 신고 처리 결과 메일 받는 횟수 구하기
    ans = [0]*len(id_list)
    for names in ids:
        if len(names)-1 >= k: # 이용정지 당한 아이디
            for name in names[1:]:
                ans[id_list.index(name)] += 1
    
    return ans