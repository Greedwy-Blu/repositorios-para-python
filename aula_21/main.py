# **kwargs


def hello(**kwargs):
  print("hello",end="")
  for key,value in kwargs.items():
    print(value, end="")


hello(title="Mr.", first="Gabriel", middle="alves", last="oliveira" )