"""
classを使ったpyxelの基本を学ぶためのサンプルコード2

class_example01.py と同じロジックですが、Gameクラスの他にCircleクラスを定義しています。
Gameクラスはゲームの情報を管理するためのクラスで、Circleクラスは円の情報を管理するためのクラスです。
このように、表現したいものごとにクラスを分けて設計することで、
「ゲームのロジック」と「ゲーム内の要素」を分けて管理することができます。
そのため、大規模で複雑なプログラムではクラスがよく利用されているのです。
"""
import pyxel

# "Circle" という名前のclassを定義しています。
# これは、１つの円が持つ情報や動きを表現するためのclassです。
# ここでは、円の設計図を用意しているイメージです。
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

# 円を表現するクラスがゲームのクラスとは別に定義されています。
# そのためゲームのロジックだけがこのクラスに残っています。
# ゲームのロジックの中で、Circle クラスのインスタンスを作成して利用しています。
class Game:
    def __init__(self):
        self.my_circle = Circle(x=80, y=60, r=10, color=7, speed=2) #Circleクラスのインスタンス(実体)を, 'my_circle' という名前で作成します。
        pyxel.init(160, 120, title="Hello Pyxel") #ウィンドウを初期化します。
        pyxel.run(self.update, self.draw) #ゲームを実行します。

    def update(self):
        self.my_circle.get_key_and_move() #self.my_circleが持つメンバ関数`get_key_and_move`を実行しています。

    # ゲームの描画を行うメソッドです。
    def draw(self):
        pyxel.cls(0) #画面を黒く塗りつぶします。
        self.my_circle.draw() #my_circleを実際に描画します。

# Gameクラスのインスタンスを作成してゲームを開始します。
Game()