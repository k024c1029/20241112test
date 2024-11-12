from flask import Flask, jsonify
import numpy as np

app = Flask(__name__)

@app.route('/turn_rare', methods=['GET'])
def turn_rare():
    """レアガチャを回す"""
    result = []
    weight = [0.33, 0.25, 0.20, 0.15, 0.05, 0.02]
    result.append(pickup_rare(weight))
    return jsonify(result)

@app.route('/turn_11rare', methods=['GET'])
def turn_11rare():
    """11連レアガチャを回す"""
    result = []
    weight = [0.57, 0.3, 0.1, 0.03]
    for _ in range(10):
        result.append(pickup_rare2(weight))
    result.append("SR")
    return jsonify(result)

def pickup_rare(weight):
    rarities = ["N", "N+", "R", "R+", "SR", "SR+"]
    picked_rarity = np.random.choice(rarities, p=weight)
    if picked_rarity == "SR+":
        picked_rarity = "".join((picked_rarity, "(", pickup_srplus(), ")"))
    return picked_rarity

def pickup_srplus():
    """SR+ の景品を等確率で排出する"""
    SR_plus = ["SR+1", "SR+2", "SR+3", "SR+4", "SR+5", "SR+6", "SR+7", "SR+8", "SR+9", "SR+10"]
    return np.random.choice(SR_plus)

def pickup_rare2(weight):
    rarities = ["R", "R+", "SR", "SR+"]
    picked_rarity = np.random.choice(rarities, p=weight)
    return picked_rarity

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)

# VO クラスのインスタンス作成
vo = VO()

class VO:
    def __init__(self):
        self._count = 0  # 回数
        self._price = 0  # 課金額

    @property
    def count(self):
        return self._count

    @count.setter
    def count(self, value):
        if value >= 0:  # 回数は非負であるべき
            self._count = value
        else:
            raise ValueError("Count cannot be negative")

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value >= 0:  # 課金額は非負であるべき
            self._price = value
        else:
            raise ValueError("Price cannot be negative")
