import sys
import math

def solve():
    try:
        
        c = int(input().strip())  
        r = int(input().strip()) 
        N = int(input().strip()) 
        s = int(input().strip()) 
        
       
        p = []
        for _ in range(N + 1):
            p.append(float(input().strip()))
    except EOFError:
        return  
        
    best_q = 0
    max_expected_profit = -float('inf')
    raw_max_profit = -float('inf')
    

    for q in range(N + 1):
        expected_profit = 0.0
        
       
        for D in range(N + 1):
            sales = min(q, D)           
            leftover = max(q - D, 0)    
           
          
            profit = (r * sales) - (c * q) + (s * leftover)
            
           
            expected_profit += p[D] * profit
            
       
        rounded_expected_profit = round(expected_profit, 4)
        
       
        if rounded_expected_profit > max_expected_profit:
            max_expected_profit = rounded_expected_profit
            best_q = q
            raw_max_profit = expected_profit  
            
 
    final_profit = math.floor(raw_max_profit)
    
   
    print(f"{best_q} {int(final_profit)}")

if __name__ == '__main__':
    solve()