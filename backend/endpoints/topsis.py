# author: topr
# last updated: 10.11.2020
# currently used: yes
# description: includes topsis function

from topsis import topsis

weights = [0.2, 0.5, 0.3]
topsis_data = [
    {
        "id": 1,
        "mat_desc": "Elektrische Zahnbuerste A",
        "price": 1.9,
        "co2": 0.75,
        "recycling": 0.75
    },
    {
        "id": 2,
        "mat_desc": "Elektrische Zahnbuerste B",
        "price": 2.0,
        "co2": 0.8,
        "recycling": 0.9
    },
    {
        "id": 3,
        "mat_desc": "Elektrische Zahnbuerste C",
        "price": 1.6,
        "co2": 0.7,
        "recycling": 0.55
    },
    {
        "id": 4,
        "mat_desc": "Elektrische Zahnbuerste D",
        "price": 1.2,
        "co2": 0.8,
        "recycling": 0.3
    }]

alternatives = [list(element.values())[2:] for element in topsis_data]
directions = [0, 1, 1]  # 0 = minimize, 1 = maximize
result = topsis(alternatives, weights, directions)
result.calc()
scores = result.C
ranks = [sorted(scores, reverse=True).index(x)+1 for x in scores]
for i in range(0, len(scores)):
    topsis_data[i]["score"] = scores[i]
    topsis_data[i]["ranks"] = ranks[i]
print(topsis_data)


class Topsis(Resource):

    def get(self, topsis_data, weights):
        alternatives = [list(element.values())[2:] for element in topsis_data]
        directions = [0, 1, 1]  # 0 = minimize, 1 = maximize
        result = topsis(alternatives, weights, directions)
        result.calc()
        scores = result.C
        ranks = [sorted(scores, reverse=True).index(x)+1 for x in scores]
        for i in range(0, len(scores)):
            topsis_data[i]["score"] = scores[i]
            topsis_data[i]["ranks"] = ranks[i]
        return topsis_data
