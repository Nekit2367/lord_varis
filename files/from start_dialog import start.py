from start_dialog import start
from all_play import run
from last_moment import end

def playing():
    start() 
    win=run()
    print(win)
    end(win)
    while True:
        st=(input("хотите сыграть еще раз : "))
        if st=="да" or st=="yes":
            win=run()
            end(win)
        else:
            break
# Убейте как можно больше врагов за две минуты
playing()