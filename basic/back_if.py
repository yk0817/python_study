# test→ trueの際の条件
test = "true" if True else "false"
print(test)

# Falseになった際、elseの式
test2 = "false" if False else "false"
print(test2)

# rubyみたいにかけない。 elseはつけないといけない
test3 = "true" if True
print(test3)
