monitor = 5000 * 4
cpu = 2500 * 3
mouse = 540.50 * 2
keyboard = 850.75 * 4

total = monitor + cpu + mouse + keyboard

print("Total Price =", total)

if total > 50000:
    discount = total * 0.10
else:
    discount = total * 0.05

    final_amount = total - discount

    print("Discount =", discount)
    print("Final Amount =", final_amount)