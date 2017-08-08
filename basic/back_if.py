# testはtrueの際の出力 if True なら test = "true"
test = "true" if True else "false"
print(test) #true

# Falseになった際、elseの式
test2 = "false" if False else "false"
print(test2) #false

# rubyみたいにかけない。 elseはつけないといけない
test3 = "true" if True
print(test3) #false
