order_list=[]

while True:
    product=input("Product: ")
    if product == "exit":
        break
    order_list.append(product)

print (order_list)

#for product in set(order_list):
   #print(product,order_list.count(product)* "*")

print("\n".join(map(lambda product: product + "  " + (order_list.count(product)* "*"), set(order_list))))