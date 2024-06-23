"""
無数の円を出現させ、すべてランダムに動かしましょう
ミッションの解答
"""
import pyxel
import random

class Circle:
    def __init__(self, x, y, r, color):
        self.x = x
        self.y = y
        self.r = r
        self.color = color

    def random_move(self):
        self.x += random.randint(-1, 1) # -1, 0, 1 のいずれかの値をランダムに取得し、自分を移動させます。
        self.y += random.randint(-1, 1)

    # 円(自分自身)を描画するメソッドです。
    def draw(self):
        pyxel.circ(self.x, self.y, self.r, self.color)


# - 円をたくさん作成する
# - 円はランダムに動かす
# という風に実装を変更しています。
class Game:
    def __init__(self):

        self.circle_list = [] #たくさんの円を管理するためのリストです。
        for i in range(30): #たくさんの円のインスタンスを作成し、リストに追加します。
            x = random.randint(0, 160)
            y = random.randint(0, 120)
            r = random.randint(1, 5)
            color = random.randint(0, 15)
            circle = Circle(x, y, r, color) #Circleクラスのインスタンスをランダムなパラメータから作成します。
            self.circle_list.append(circle)

        pyxel.init(160, 120, title="Hello Pyxel") #ウィンドウを初期化します。

        # pyxelの更新処理と描画処理をこのクラスのメソッドとして定義します。
        pyxel.run(self.update, self.draw)

    # ゲームの状態を更新するメソッドです。
    def update(self):
        for circle in self.circle_list: #リストに入っているすべての円を一つづつ呼び出し、ランダムに動かすメンバ関数を呼び出します。
            circle.random_move()

    # ゲームの描画を行うメソッドです。
    def draw(self):
        pyxel.cls(0) # 画面を黒でクリアします。
        for circle in self.circle_list:
            circle.draw()

# Gameクラスのインスタンスを作成してゲームを開始します。
Game()
