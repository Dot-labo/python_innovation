"""
classを使ったpyxelの基本を学ぶためのサンプルコード2

Gameクラスはゲームの情報を管理するためのクラスで、Circleクラスは円の情報を管理するためのクラスです。
このようにゲームのロジックを管理するクラスト、ゲームに登場するモノのクラスで分けることで、
ゲームの内容を変更しやすくなります。
様々な色や形の円を表示して、ランダムに動かしてみましょう。
"""
import pyxel
import random

# Circleクラスの実装は前の例(class_example02.py)と全く変更していません。
class Circle:
    def __init__(self, x, y, r, color):
        # 位置(x, y)、半径r、色color を決めれば、円が持つ情報を表現できます。
        self.x = x
        self.y = y
        self.r = r
        self.color = color

    # 円を移動させるメソッドです。
    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    # 円(自分自身)を描画するメソッドです。
    def draw(self):
        pyxel.circ(self.x, self.y, self.r, self.color)


# - 円をたくさん作成する
# - 円はランダムに動かす
# という風に実装を変更しています。
class Game:
    def __init__(self):

        self.circle_list = [] #たくさんの円を管理するためのリストです。
        for i in range(30):
            x = random.randint(0, 160)
            y = random.randint(0, 120)
            r = random.randint(1, 5)
            color = random.randint(0, 15)

            circle = Circle(x, y, r, color)
            self.circle_list.append(circle)

        pyxel.init(160, 120, title="Hello Pyxel") #ウィンドウを初期化します。
        # pyxelの更新処理と描画処理をこのクラスのメソッドとして定義します。
        pyxel.run(self.update, self.draw)

    # ゲームの状態を更新するメソッドです。
    def update(self):
        for circle in self.circle_list:
            random_x = random.randint(-1, 1)
            random_y = random.randint(-1, 1)
            circle.move(random_x, random_y)

    # ゲームの描画を行うメソッドです。
    def draw(self):
        pyxel.cls(0) # 画面を黒でクリアします。
        for circle in self.circle_list:
            circle.draw()

# Gameクラスのインスタンスを作成してゲームを開始します。
Game()
