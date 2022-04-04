def solution(money: int, costs: list) -> int:
    # 동적 프로그래밍? 우선순위 큐 둘다 아님

    monetary_unit = [1, 5, 10, 50, 100, 500]
    # 1원당 생상 단위 클수록 좋음. 1원당 생산단위 순 내림차순 정리
    unit_cost = [monetary_unit[i] / costs[i] for i in range(len(costs))]

    # O(NLogN)
    # 두 개의 리스트를 대응 정렬
    # 다중 조건 정렬? zip(정렬기준이 되는 배열, 정렬할 배열)로 tuple만든후 정렬하면, 앞에 원소 기준으로 정렬됨
    unit_sorted_by_cost = [m for _, m in sorted(zip(unit_cost, monetary_unit), reverse=True)]

    production_cost = 0
    # 가장 싸게 제조할 수 있는 동전을 최대로 생산하기.
    for unit in unit_sorted_by_cost:
        if money == 0:
            break
        # unit 원짜리 동전을 cnt 생샌해 price 어치 동전 생산. 생산비용 cost원.
        # unit: 화폐단위 cnt:생산된 개수 price: 생산된 화폐가치 cost:생산비용
        cnt = money // unit
        price = cnt * unit
        # O(N) 값 검색시..
        cost = costs[monetary_unit.index(unit)] * cnt
        money -= price
        production_cost += cost
        print(f'{unit}동전을 {cnt}개 생산해서 {price}어치 만듬 생산비용 {cost}')
    return production_cost


def solution_hash(money: int, costs: list) -> int:
    units = [1, 5, 10, 50, 100, 500]
    d = {}
    # {화폐단위 : [생산 비용, 비용 1원당 생산된 화폐가치]}
    # 여러 배열을 합쳐서 생각해야 할때. 인덱스가 같으면 같은 값을 가리킬 때 -> zip, hash사용하기(상수시간에 참조가능. 배열로 두면O(n) 걸림)
    for i, unit in enumerate(units):
        d[unit] = [costs[i], unit / costs[i]]

    units = sorted(units, key=lambda x: d[x][1], reverse=True)

    i = 0
    production_cost = 0
    while money != 0 and i < len(units):
        cnt = money // units[i]
        price = units[i] * cnt
        cost = d[units[i]][0] * cnt

        money -= price
        production_cost += cost
        i += 1

    return production_cost


print(solution(4578, [1, 4, 99, 35, 50, 1000]))
print(solution(1999, [2, 11, 20, 100, 200, 600]))
