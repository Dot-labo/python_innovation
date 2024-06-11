"""
クラスのメンバ関数の説明

クラスの中で定義される関数をメンバ関数と呼びます。
メンバ変数には インスタンス名.変数名 でアクセスできるのと同じように
メンバ関数には インスタンス名.関数名() でアクセスできます。
メンバ関数の中からメンバ変数にアクセスする場合は、self.変数名 とします。
ここで、'self' というキーワードは、メンバが属するインスタンス自身を指します。
"""

class Wizard:
    #特別なメンバ関数である__init__関数を定義
    def __init__(self, name, hp, mp, magic_list):
        self.name = name
        self.hp = hp
        self.mp = mp
        self.magic_list = magic_list
    
    #メンバ関数 'talk' を定義
    def talk(self):
        print("私は", self.name) #self.name は、このインスタンスのメンバ変数 name を指します
        print("HPは", self.hp)
        print("MPは", self.mp)
        print("覚えている魔法は", self.magic_list)
    
wizard_1 = Wizard(name='マーリン', hp=14, mp=27, magic_list=['Fireball', 'Ice Storm', 'Lightning Bolt']) #インスタンス wizard_1 を生成
wizard_1.talk() #インスタンス wizard_1 のメンバ関数 talk を呼び出す