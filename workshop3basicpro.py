total_cash=0
n=int(input("ระบุจำนวนร้านที่ต้องไปเก็บ: "))
for i in range(n):
    money= float(input(f"ร้านที่{i+1} : "))
    total_cash+=money
print(f"จำนวนร้านที่เก็บ: {n}")
print(f"จำนวนเงินทั้งหมดที่เก็บได้: {total_cash}")