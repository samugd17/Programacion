# **********************
# ORDENANDO CON BURBUJAS
# **********************


def bubble(items):
#    if items == []:
#     return []
    sorted_items=[]
    prev_item= items[0]
    for i in range (len(items)):
        if prev_item < items[i]:
            items[i] = prev_item
            sorted_items.append(items[i])                                                   
        elif prev_item < items[i]:
            
            sorted_items.insert(1, prev_item)
        else:
            sorted_items.insert(1, prev_item)
    print(sorted_items)
        
        
        

    
        




items= [3, 3, 3, 2, 2, 1]  
bubble(items)

