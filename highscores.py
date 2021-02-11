from tkinter import *


def update_file(score):
    f = open('scores_info.txt', 'a')
    f.write(str(score))
    f.write('\n')
    f.close()


def add_highscore():
    global arr_scores
    arr_scores = []
    data = open('scores_info.txt', 'r').read().splitlines()
    try:
        data = [int(_) for _ in data]
    except:
        arr_scores = []
    data = sorted(data, reverse=True)
    for _ in range(1, len(data) + 1):
        i = []
        i.append(_)
        i.append(data[_ - 1])
        arr_scores.append(i)
    return arr_scores


current_scores = add_highscore()  # [[1, 99999999], [2, 3345], [3, 45], [4, 0]]
counter = 0


class ScoreLine(Frame):
    def __init__(self, rank, score):
        super().__init__(hs.f_scores)
        self.rank = rank
        self.score = score
        self.l_rank = Label(self, text=rank)
        self.l_score = Label(self, text=score)
        self.l_rank.pack(side=LEFT, fill=X)
        self.l_score.pack(side=LEFT, fill=X, expand=True)
        self.pack(side=TOP, fill=X)

    def self_destruct(self):
        self.destroy()


def chk_decimal(str_to_chk):
    str_to_chk = str(str_to_chk)
    decimal = True
    for char in str_to_chk:
        if char.isnumeric():
            pass
        else:
            decimal = False
    return decimal


def init_gen():
    global rank_frames
    rank_frames = {}
    for _ in ranks.keys():
        if _ not in rank_frames:
            rank_frames[_] = ScoreLine(ranks[_][0], ranks[_][1])
        else:
            exit('rank frames append error')


class HighScoresApp(Tk):
    def __init__(self, current_scores):
        global ranks
        global counter
        ranks = {}
        for _ in range(len(current_scores)):
            if _ not in ranks:
                ranks[_] = current_scores[_]
                counter += 1
            else:
                exit('ranks count error')
        super().__init__()
        self.title('HIGHSCORES TABLE')
        # self.height = (self.winfo_screenwidth()-self.winfo_width())/2
        # self.width = (self.winfo_screenheight()-self.winfo_height())/2
        # self.geometry("500x200+%d+%d" % (self.height, self.width))
        self.geometry("500x200")

        self.f_main = Frame(self, bg='navy')
        # self.f_controls = Frame(self.f_main, bg='DarkGray')

        # background_image = PhotoImage(file="bg.gif")
        # background = Label(root, image=background_image, bd=0)
        # background.pack()

        self.f_scores = Frame(self.f_main, bg='gray')
        in_rank = StringVar()
        in_score = StringVar()
        # self.f_input = Frame(self.f_controls, bg='SkyBlue4')
        # self.l_rank = Label(self.f_input, bg='black', fg='white', text='RANK:')
        # self.l_score = Label(self.f_input, bg='black', fg='white', text='SCORE:')
        # self.e_rank = Entry(self.f_input, textvariable=in_rank)
        # self.e_score = Entry(self.f_input, textvariable=in_score)
        # self.b_new = Button(self.f_controls, text='new', command=self.new_score)
        # elf.b_del = Button(self.f_controls, text='del', command=self.del_score)

        self.f_main.pack(side=TOP, fill=BOTH, expand=True)
        # self.f_controls.pack(side=TOP, fill=X)
        # self.b_new.pack(side=LEFT)
        # self.b_del.pack(side=LEFT)
        # self.f_input.pack(side=LEFT)
        # self.l_rank.pack(side=LEFT)
        # self.e_rank.pack(side=LEFT)
        # self.l_score.pack(side=LEFT)
        # self.e_score.pack(side=LEFT)
        self.f_scores.pack(side=TOP, fill=BOTH, expand=True)

    def new_score(self):
        score = self.e_score.get()
        if score == '':
            print('empty score field error')
        elif not chk_decimal(score):
            print('wrong score data format')
        else:
            score = int(score)
            global counter
            counter += 1
            rank = counter
            global rank_frames
            if counter not in ranks and counter not in rank_frames:
                ranks[counter] = (rank, score)
                rank_frames[counter] = ScoreLine(rank, score)
            else:
                exit('new_score ranks, rank frames count error')
            self.score_update()

    def del_score(self):
        rank = self.e_rank.get()
        if rank == '':
            print('empty rank field error')
        elif not chk_decimal(rank):
            print('wrong rank data format')
        else:
            global ranks
            global rank_frames
            for _ in ranks.keys():
                if ranks[_][0] == int(rank):
                    ranks.pop(_)
                    rank_frames[_].self_destruct()
                    break
                else:
                    print('rank resolution error on del func')
            self.score_update()

    def score_update(self):
        global ranks
        global rank_frames
        tmp = [_[1] for _ in ranks.values()]
        tmp.sort(reverse=True)
        for _ in rank_frames.keys():
            rank_frames[_].self_destruct()
        rank_frames = {}
        ranks = {}
        global counter
        counter = 0
        for _ in range(len(tmp)):
            ranks[_] = (_ + 1, tmp[_])
            rank_frames[_] = ScoreLine(_ + 1, tmp[_])
            counter += 1


def make_highscores():
    global hs
    hs = HighScoresApp(current_scores)
    init_gen()
    hs.mainloop()
    return hs

# make_highscores()
# hs = HighScoresApp(current_scores)
# init_gen()
# hs.mainloop()

# update_file(4534535)
# print(add_highscore())
