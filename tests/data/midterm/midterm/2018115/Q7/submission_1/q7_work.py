# MID-TERM EXAM: QUESTION 7

def decompose(pence):
    if pence > 200:
        x200 = pence % 200
        
        if x200 > 100:
            
            x100 = x200 % 100
            
            if x100 > 50:
                
                x50 = x100 % 50 
                
                if x50 > 20:
                  
                    x20 = pence % 20 
        
                    if x20 > 10:
            
                        x10 = x20 % 10
                
                        if x10 > 5:
                        
                            x5 = x10 % 5
                            
                            if x5 > 2:
                                
                                x2 = x5% 2
                                
                                if x2 > 1
                                
                                    x1 = 1
                                    
                                      if pence > 200:
       
        
        elif pence < 200 and pence > 100:
            
            x100 = pence % 100
            
            if x100 > 50:
                
                x50 = x100 % 50 
                
                if x50 > 20:
                  
                    x20 = pence % 20 
        
                    if x20 > 10:
            
                        x10 = x20 % 10
                
                        if x10 > 5:
                        
                            x5 = x10 % 5
                            
                            if x5 > 2:
                                
                                x2 = x5% 2
                                
                                if x2 > 1
                                
                                    x1 = 1
                                    
                                      
            
            
            
            elif pence < 100 and pence > 50:
                
                x50 = pence 50 
                
                if x50 > 20:
                  
                    x20 = pence % 20 
        
                    if x20 > 10:
            
                        x10 = x20 % 10
                
                        if x10 > 5:
                        
                            x5 = x10 % 5
                            
                            if x5 > 2:
                                
                                x2 = x5% 2
                                
                                if x2 > 1
                                
                                    x1 = 1
                                    
                
                elif pence < 50 and pence > 20:
                
                  
                    x20 = pence % 20 
        
                    if x20 > 10:
            
                        x10 = x20 % 10
                
                        if x10 > 5:
                        
                            x5 = x10 % 5
                            
                            if x5 > 2:
                                
                                x2 = x5% 2
                                
                                if x2 > 1
                                
                                    x1 = 1
                                    
                                   
                     
        
                    elif pence < 20 and pence > 10:
            
                        x10 = pence % 10
                
                        if x10 > 5:
                        
                            x5 = x10 % 5
                            
                            if x5 > 2:
                                
                                x2 = x5% 2
                                
                                if x2 > 1
                                
                                    x1 = 1
                                    
            
                       
                
                        elif pence < 10 and pence > 5:
                        
                            x5 = x10 % 5
                            
                            if x5 > 2:
                                
                                x2 = x5% 2
                                
                                if x2 > 1
                                
                                    x1 = 1
                                    
                        elif pence < 5 and pence > 2:
                        
                         
                            x2 = x5% 2
                                
                            if x2 > 1
                                
                            x1 = 1