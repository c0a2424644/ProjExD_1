import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("fig/pg_bg.jpg")
    bg2_img = pg.transform.flip(bg_img, True, False)#練習８
    tori_img = pg.image.load("fig/3.png") #練習１
    tori_img = pg.transform.flip(tori_img, True, False)#練習２
    tori_rct = tori_img.get_rect() #練習１０－１rect抽出
    tori_rct.center = 300, 200 #練習１０ー２
    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return
        key_lst = pg.key.get_pressed() #練習１０－３
        #print(key_lst)
        if key_lst[pg.K_UP]:#練習１０－４
            tori_rct.move_ip((0,-1))
        if key_lst[pg.K_DOWN]:
            tori_rct.move_ip((0,1))
        if key_lst[pg.K_RIGHT]:
            tori_rct.move_ip((1,0))
        if key_lst[pg.K_LEFT]:
            tori_rct.move_ip((-1,0))

        x = tmr % 3200 #練習６
        screen.blit(bg_img, [-x, 0])#練習３
        screen.blit(bg2_img, [-x+1600,0])#練習７
        screen.blit(bg_img, [-x+3200,0])#練習９
        screen.blit(tori_img, tori_rct) #練習４練習１０ー５
        pg.display.update()
        tmr += 1        
        clock.tick(200)#練習５


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()