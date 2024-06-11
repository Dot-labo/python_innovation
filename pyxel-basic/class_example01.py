"""
classを使ったpyxelの基本を学ぶためのサンプルコード1

矢印キーで円を動かすだけの簡単なプログラムですが、pyxelの基本的な使い方がわかります。
simple_example01.py と同じロジックですが、classを用いた書き方に変更しています。
"""
import pyxel

# "Game" という名前のclassを定義しています。
# classとは、関数(処理)とデータ(プロパティ)を一つにまとめて管理しやすくしたものです。
class Game:
    # __init__() は、インスタンス(クラスの実体)が作成されるときに自動で呼び出される特別なメソッドです。
    def __init__(self):
        # 画面の設定を初期化します。画面サイズは160x120、タイトルは"Hello Pyxel"です。
        pyxel.init(160, 120, title="Hello Pyxel")

        # 円の初期位置を画面の中心に設定します。
        self.x = 80
        self.y = 60
        
        # pyxelの更新処理と描画処理をこのクラスのメソッドとして定義します。
        pyxel.run(self.update, self.draw) #なぜselfが必要なのかというと、クラス内で定義されたメソッドを呼び出す際には、selfをつける必要があるからです。

    # ゲームの状態を更新するメソッドです。
    def update(self):
        # 矢印キーに応じて円の座標を更新します。
        if pyxel.btn(pyxel.KEY_UP):
            self.y -= 2 # 上矢印キーで上に移動します。
        if pyxel.btn(pyxel.KEY_DOWN):
            self.y += 2 # 下矢印キーで下に移動します。
        if pyxel.btn(pyxel.KEY_LEFT):
            self.x -= 2 # 左矢印キーで左に移動します。
        if pyxel.btn(pyxel.KEY_RIGHT):
            self.x += 2 # 右矢印キーで右に移動します。

    # ゲームの描画を行うメソッドです。
    def draw(self):
        pyxel.cls(0) # 画面を黒でクリアします。
        pyxel.circ(self.x, self.y, 10, 7) # (x, y)座標に半径10, 色7（赤色）の円を描画

# Gameクラスのインスタンスを作成してゲームを開始します。
Game()