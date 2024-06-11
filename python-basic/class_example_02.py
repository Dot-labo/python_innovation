"""
__init__関数の説明

__init__関数は、クラスの初期化処理を行う関数です。
クラスを定義する際に、__init__関数を定義しておくと、そのクラスのインスタンスを生成する際に、 * 自動的に * __init__関数が呼び出されます。
__init__関数は、インスタンスを生成する際に、そのインスタンスが持つべきメンバ変数を初期化するために使用します。
"""
class Wizard:
    #特別なメソッドである__init__関数を定義
    def __init__(self, name, hp, mp, magic_list): #selfは、インスタンス自身を指します
        self.name = name
        self.hp = hp
        self.mp = mp
        self.magic_list = magic_list

# "Wizard"クラスのインスタンス「wizard_1」を生成 
# インスタンスを生成した瞬間に、そのインスタンス(wizard_1)の持つ__init__関数が呼び出される
# その際に、引数として指定した値が、self.name, self.hp, self.mp, self.magic_listに代入される
# このように、インスタンスを生成する際に、初期化処理を行うことができる
wizard_1 = Wizard(name='マーリン', hp=14, mp=27, magic_list=['Fireball', 'Ice Storm', 'Lightning Bolt'])
# wizard_1 = Wizard() という形式になっていることに注目

print("私は", wizard_1.name)
print("HPは", wizard_1.hp)
print("MPは", wizard_1.mp)
print("覚えている魔法は", wizard_1.magic_list)