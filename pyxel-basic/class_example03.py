"""
classを使ったpyxelの基本を学ぶためのサンプルコード2

CircleとGameに実装が分かれています。
Circleクラスのインスタンスを3つ作成し、それぞれ動かせるようにします。
"""
import pyxel

# "Circle" クラスの定義です。円の持つ情報や処理は前のプログラムと同じなので、ここの実装は変わりません。
class Circle:
    def __init__(self, x, y, r, color, speed):
        # 位置(x, y)、半径(r)、色(color),スピード(speed) を決めれば、円が持つ情報を表現できます。
        self.x = x
        self.y = y
        self.r = r
        self.color = color
        self.speed = speed

    # 円を移動させるメソッドです。
    # キー入力を取得して自分自身を移動(self.x, self.yを更新)しています。
    def get_key_and_move(self):
        if pyxel.btn(pyxel.KEY_RIGHT):
            self.x += self.speed
        if pyxel.btn(pyxel.KEY_LEFT):
            self.x -= self.speed
        if pyxel.btn(pyxel.KEY_UP):
            self.y -= self.speed
        if pyxel.btn(pyxel.KEY_DOWN):
            self.y += self.speed
    
    # 円(自分自身)を描画するメソッドです。
    def draw(self):
        pyxel.circ(self.x, self.y, self.r, self.color)

# 3つの円のインスタンスを作り、メンバ関数を呼び出しています。
class Game:
    def __init__(self):
        self.circle_1 = Circle(x=80, y=60, r=10, color=7, speed=2)
        self.circle_2 = Circle(x=100, y=80, r=7, color=4, speed=3)
        self.circle_3 = Circle(x=60, y=40, r=4, color=10, speed=4)
        pyxel.init(160, 120, title="Hello Pyxel") #ウィンドウを初期化します。
        pyxel.run(self.update, self.draw) #ゲームを実行します。

    def update(self):
        self.circle_1.get_key_and_move() #circle_1のget_key_and_moveメソッドを呼び出しています。
        self.circle_2.get_key_and_move()
        self.circle_3.get_key_and_move()

    # ゲームの描画を行うメソッドです。
    def draw(self):
        pyxel.cls(0) #画面を黒く塗りつぶします。
        self.circle_1.draw() #circle_1を実際に描画します。
        self.circle_2.draw()
        self.circle_3.draw()

# Gameクラスのインスタンスを作成してゲームを開始します。
Game()