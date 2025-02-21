import core
import curses
import config as c
import time as t



def main(screen):
    screen.timeout(0)

    e = core.Egg((0, 0))
    f = core.Field(width=c.WIDTH, height=c.HEIGHT, char_table=c.CHAR_TABLE, egg=e)
    s = core.Snake(name="snake")
    s.set_field(field=f)

    while(True):
        ch = screen.getch()
        if ch != -1:
            s.set_direction(ch)

        s.move()
        
        f.render(screen)
        screen.refresh()
        
        t.sleep(.4)

if __name__=='__main__':
    curses.wrapper(main)