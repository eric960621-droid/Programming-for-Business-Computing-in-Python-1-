import sys

def solve():
    
    try:
        first_line = input().split()
    except EOFError:
        return
        
    if not first_line:
        return
    
  
    n = int(first_line[0])
    p = int(first_line[1])
    d = int(first_line[2])
    
   
    towns = [(0, 0, 0)] 
    
   
    for i in range(1, n + 1):
        line = input().split()
        x = int(line[0])
        y = int(line[1])
        pop = int(line[2])
        towns.append((x, y, pop))
        
   
    d_squared = d * d
    
   
    coverage = [[] for _ in range(n + 1)]
    for i in range(1, n + 1):
        xi, yi, pop_i = towns[i]
        for j in range(1, n + 1):
            xj, yj, pop_j = towns[j]
           
            dist_squared = (xi - xj)**2 + (yi - yj)**2
           
            if dist_squared <= d_squared:
                coverage[i].append(j)
                
    covered_towns = set()    
    selected_bases = []       
    total_covered_pop = 0    

    for _ in range(p):
        best_town_id = -1
        max_added_pop = -1
        
     
        for i in range(1, n + 1):
            current_added_pop = 0
            
          
            for j in coverage[i]:
              
                if j not in covered_towns:
                    current_added_pop += towns[j][2] 
            
            
            if current_added_pop > max_added_pop:
               
                max_added_pop = current_added_pop
                best_town_id = i
            elif current_added_pop == max_added_pop:
                
                if best_town_id == -1 or i < best_town_id:
                    best_town_id = i
                    
        
        selected_bases.append(best_town_id)
       
        total_covered_pop += max_added_pop
        
        
        for j in coverage[best_town_id]:
            covered_towns.add(j)

  
    result = selected_bases + [total_covered_pop]
    print(" ".join(map(str, result)))

if __name__ == '__main__':
    solve()