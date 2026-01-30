A = float(input("Enter side A: "))
B = float(input("Enter side B: "))
C = float(input("Enter side C: "))
D = float(input("Enter side D: "))
E = float(input("Enter side E: "))

rect_area = A * B
squ_area = (D - E - B) * (A - C)
tri_area = (E * (A - C)) * 0.5

total_area = rect_area + tri_area + squ_area

print(f"Room Area: " )
print(total_area)