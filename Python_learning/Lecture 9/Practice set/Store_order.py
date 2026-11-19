class order:
    def __init__(self,item,price):
        self.item=item
        self.price=price

    def __gt__(self,ord2):
        return self.price > ord2.price

ord=order("coffee",15)
ord2=order("tea",10)

print(ord > ord2)