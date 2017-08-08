class Widget(object):
    def __init__(self,r,l):

        # 通常のメンバ変数
        self.rval = r
        self.lval = l

        # プライベート変数
        self.__secret = 5
    # publicクラスメンバ変数
    classVal = 30

    # プライベートクラス変数
    __SecretClassVal = 10

    # 通常メソッド
    def Clac(self):
        # メンバ変数を定義
        self.top = 10
        return self.rval * self.lval * self.top

    def __MyCalc(self):
        print("thii is private method")

#
    @classmethod
    def SelfName(cls):
        cls.number = 1

    # プライベートメソッド
    @classmethod
    def __PrivateSelfName(cls):
        print("this is private class method")

if __name__ == '__main__':
    main()
