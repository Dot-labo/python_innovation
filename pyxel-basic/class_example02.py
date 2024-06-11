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

# "Game" という名前のclassを定義しています。
# これは、ゲーム全体を管理するためのクラスです。
# ゲーム全体の設計図を用意しているイメージです。
class Game:
    def __init__(self):
        self.my_circle = Circle(80, 60, 10, 7) #Circleクラスのインスタンス(実体)を, 'my_circle' という名前で作成します。
        pyxel.init(160, 120, title="Hello Pyxel") #ウィンドウを初期化します。
        # pyxelの更新処理と描画処理をこのクラスのメソッドとして定義します。
        pyxel.run(self.update, self.draw)

    # ゲームの状態を更新するメソッドです。
    #ここでは、Circleクラスが持つmoveメソッドを呼ぶことで、円を動かしています。
    def update(self):
        if pyxel.btn(pyxel.KEY_UP):
            self.my_circle.move(0, -2)
        if pyxel.btn(pyxel.KEY_DOWN):
            self.my_circle.move(0, 2)
        if pyxel.btn(pyxel.KEY_LEFT):
            self.my_circle.move(-2, 0)
        if pyxel.btn(pyxel.KEY_RIGHT):
            self.my_circle.move(2, 0)

    # ゲームの描画を行うメソッドです。
    def draw(self):
        pyxel.cls(0) # 画面を黒でクリアします。
        # my_circleを実際に描画します。
        self.my_circle.draw()

# Gameクラスのインスタンスを作成してゲームを開始します。
Game()