class Wizard:
    def __init__(self, name, hp, mp, magic_list):
        self.name = name
        self.hp = hp
        self.mp = mp
        self.magic_list = magic_list
    
    def talk(self):
        print("私は", self.name)
        print("HPは", self.hp)
        print("MPは", self.mp)
        print("覚えている魔法は", self.magic_list)
    
# "Wizard"クラスのインスタンス「wizard」を生成
# インスタンスを生成した瞬間に、そのクラス(Wizard)の持つ__init__メソッドが呼び出される
# その際に、引数として指定した値が、self.name, self.hp, self.mp, self.magic_listに代入される
# このように、インスタンスを生成する際に、初期化処理を行うことができる
wizard = Wizard(name='マーリン', hp=14, mp=27, magic_list=['Fireball', 'Ice Storm', 'Lightning Bolt'])
wizard.talk()