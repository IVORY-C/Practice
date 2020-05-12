# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
class Test:
    MAX = 10
    def __init__(self):
        self.max = 100

t1 = Test()
t2 = Test()


# %%
t1.max = 101
t2.max = 102

t1.MAX = 103
t2.MAX = 104

Test.MAX = 105
t3 = Test()

print(Test.MAX)


# %%
class test():
    def __init__(self,data=1):
        self.data = data

    def __iter__(self):
        return self
    def __next__(self):
        if self.data > 5:
            raise StopIteration
        else:
            self.data+=1
            return self.data

for item in test(3):
    print(item)


