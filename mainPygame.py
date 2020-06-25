from pygame import*
window = display.set_mode((700, 500))
display.set_caption("Way to your heart")


background = transform.scale(image.load('galaxy_1.jpg'), (700,500))
img1 = transform.scale(image.load('ufo_3.png'), (100, 100))
x = 50
y = 5
window.blit(background, (0,0))
window.blit(img1, (x,y))

display.update()
run = True 
while run:
    z = 100
    p = 100
    time.delay(50)  
    draw.rect(window, (255,0,0), (z, p, 40, 60))   
    display.update()   
    for e in event.get():
        if e.type == QUIT:
            run = False
        elif e == K_LEFT:
            z += 10      
print("Hello")   
print("hghg")  




    
