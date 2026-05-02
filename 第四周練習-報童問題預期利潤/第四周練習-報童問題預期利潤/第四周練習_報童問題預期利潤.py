c = int(input())  
r = int(input())  
N = int(input())  

p0 = float(input())
p1 = float(input())
p2 = float(input())
p3 = float(input())
p4 = float(input())
p5 = float(input())
p6 = float(input())
p7 = float(input())
p8 = float(input())

max_profit = -999999.0
best_q = 0

for q in range(N + 1):
   
    expected_sales = 0.0
    
    expected_sales += (p0 * (0 if 0 < q else q)) 
     
    s0 = 0 if 0 < q else 0 
    s1 = 1 if 1 < q else q
    s2 = 2 if 2 < q else q
    s3 = 3 if 3 < q else q
    s4 = 4 if 4 < q else q
    s5 = 5 if 5 < q else q
    s6 = 6 if 6 < q else q
    s7 = 7 if 7 < q else q
    s8 = 8 if 8 < q else q
    
    expected_sales = (p0*0 + p1*min(q,1) + p2*min(q,2) + p3*min(q,3) + 
                      p4*min(q,4) + p5*min(q,5) + p6*min(q,6) + 
                      p7*min(q,7) + p8*min(q,8))
    
   
    current_profit = r * expected_sales - c * q
    
   
    if current_profit > max_profit:
        max_profit = current_profit
        best_q = q

print(best_q, int(max_profit))
