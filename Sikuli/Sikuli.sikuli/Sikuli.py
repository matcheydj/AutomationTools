buttons=findAll("1449045420217.png")
for i in buttons:
    click(i)
    k=0 
    for k in range(20):
      type(Key.DOWN)
      type(Key.ENTER)
      click(i)
      click(i.right(90))
      i.left(90)
              
      wait(5)
      k+=1 
    
