"""
クラスのメンバ関数の説明

クラスの中で定義される関数をメンバ関数と呼びます。
メンバ変数には インスタンス名.変数名 でアクセスできるのと同じように
メンバ関数には インスタンス名.関数名() でアクセスできます。
メンバ関数の中からメンバ変数にアクセスする場合は、self.変数名 とします。
ここで、'self' というキーワードは、メンバが属するインスタンス自身を指します。
"""

class Pet:
    def __init__(self, animal_type, sound):
        self.animal_type = animal_type
        self.sound = sound
    
    #メンバ関数 'make_sound' を定義
    def make_sound(self): #メンバ関数を定義する時は、第一引数に self を指定する必要があります。
        print(self.animal_type, "が今から鳴くみたい")
        print(self.sound) #self.sound は、このインスタンスのメンバ変数 sound を指します

p1 = Pet(animal_type='イヌ', sound='ワンワン') #インスタンス p1 を生成
p1.make_sound() #インスタンス p1 のメンバ関数 make_sound を呼び出す

p2 = Pet(animal_type = 'サル', sound = 'キーキー') #インスタンス p2 を生成
p2.make_sound() #インスタンス p2 のメンバ関数 make_sound を呼び出す
