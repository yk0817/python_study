class MainClass:
    class InnerClass:
        def __init__(self):
            self.prop = "inner class"

    def __init__(self):
        self.prop = "main class"
        self.inner = MainClass.InnerClass()

obj = MainClass()
print(obj.prop)
print(obj.inner.prop)
