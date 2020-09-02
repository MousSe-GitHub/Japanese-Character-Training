# coding: utf-8
from pypresence import Presence
from tkinter import *
import random
import time
import os


startTime = int(time.time())
client_id = 714537755425898596
RPC = Presence(client_id)
RPC.connect()
RPC.update(large_image="ico", large_text='JP char training', details='Training his japanese skill', state="Score : 0/0 (100%)", start = startTime)


#Window set up
window = Tk()
window.resizable(False, False)
window.geometry('600x400')
window.title("Japanese Characters Training")


#Var set up

#Character to list
hiragana = ['あ','い','う','え','お','か','き','く','け','こ','さ','し','す','せ','そ','た','ち','つ','て','と','な','に','ぬ','ね','の','は','ひ','ふ','へ','ほ','ま','み','む','め','も','や','ゆ','よ','ら','り','る','れ','ろ','わ','を','ん', 'が', 'ぎ', 'ぐ', 'げ', 'ご', 'ざ', 'じ', 'ず', 'ぜ', 'ぞ', 'だ', 'ぢ', 'づ', 'で', 'ど', 'ば', 'び', 'ぶ', 'べ', 'ぼ', 'ぱ', 'ぴ', 'ぷ', 'ぺ', 'ぽ', 'きゃ', 'きゅ', 'きょ', 'しゃ', 'しゅ', 'しょ', 'ちゃ', 'ちゅ', 'ちょ', 'にゃ', 'にゅ', 'にょ', 'ひゃ', 'ひゅ', 'ひょ', 'みゃ', 'みゅ', 'みょ', 'りゃ', 'りゅ', 'りょ', 'ぎゃ', 'ぎゅ', 'ぎょ', 'じゃ', 'じゅ', 'じょ', 'びゃ', 'びゅ', 'びょ', 'ぴゃ', 'ぴゅ', 'ぴょ']

katakana = ['ア','イ','ウ','エ','オ','カ','キ','ク','ケ','コ','サ','シ','ス','セ','ソ','タ','チ','ツ','テ','ト','ナ','ニ','ヌ','ネ','ノ','ハ','ヒ','フ','ヘ','ホ','マ','ミ','ム','メ','モ','ヤ','ユ','ヨ','ラ','リ','ル','レ','ロ','ワ','ヲ','ン', 'ガ', 'ギ', 'グ', 'ゲ', 'ゴ', 'ザ', 'ジ', 'ズ', 'ゼ', 'ゾ', 'ダ', 'ヂ', 'ヅ', 'デ', 'ド', 'バ', 'ビ', 'ブ', 'ベ', 'ボ', 'パ', 'ピ', 'プ', 'ペ', 'ポ', 'キャ', 'キュ', 'ｷｮ', 'シャ', 'シュ', 'ショ', 'チャ', 'チュ', 'チョ', 'ニャ', 'ニュ', 'ニョ', 'ヒャ', 'ヒュ', 'ヒョ', 'ミャ', 'ミュ', 'ミョ', 'リャ', 'リュ', 'リョ', 'ギャ', 'ギュ', 'ギョ', 'ジャ', 'ジュ', 'ジョ', 'ビャ', 'ビュ', 'ビョ', 'ピャ', 'ピュ', 'ピョ']

letter = ['A','I','U','E','O','KA','KI','KU','KE','KO','SA','SHI','SU','SE','SO','TA','CHI','TSU','TE','TO','NA','NI','NU','NE','NO','HA','HI','FU','HE','HO','MA','MI','MU','ME','MO','YA','YU','YO','RA','RI','RU','RE','RO','WA','WO','N', 'GA', 'GI', 'GU', 'GE', 'GO', 'ZA', 'JI', 'ZU', 'ZE', 'ZO', 'DA', 'JI', 'DU', 'DE', 'DO', 'BA', 'BI', 'BU', 'BE', 'BO', 'PA', 'PI', 'PU', 'PE', 'PO', 'KYA', 'KYU', 'KYO', 'SHA', 'SHU', 'SHO', 'CHA', 'CHU', 'CHO', 'NYA', 'NYU', 'NYO', 'HYA', 'HYU', 'HYO', 'MYA', 'MYU', 'MYO', 'RYA', 'RYU', 'RYO', 'GYA', 'GYU', 'GYO', 'JA', 'JU', 'JO', 'BYA', 'BYU', 'BYO', 'PYA', 'PYU', 'PYO']


#General var
showHiragana = True
showKatakana = True
showHandakuten = True
showCombinaison = True

randomChar = random.randint(0, 45)

score = 0
count = 0




#Switch buttons
def switchHiragana():
	global showHiragana

	try:
		if showHiragana == True:
			btnHiragana.configure(fg='#ad3d3d', bg='#cfcfcf')
			showHiragana = False
		else:
			btnHiragana.configure(fg='#69c989', bg='#dedede')
			showHiragana = True
	except:
		pass

	return showHiragana


def switchKatakana():
	global showKatakana

	try:
		if showKatakana == True:
			btnKatakana.configure(fg='#ad3d3d', bg='#cfcfcf')
			showKatakana = False
		else:
			btnKatakana.configure(fg='#69c989', bg='#dedede')
			showKatakana = True
	except:
		pass

	return showKatakana


def switchHandakuten():
	global showHandakuten

	try:
		if showHandakuten == True:
			btnHandakuten.configure(fg='#ad3d3d', bg='#cfcfcf')
			showHandakuten = False
		else:
			btnHandakuten.configure(fg='#69c989', bg='#dedede')
			showHandakuten = True
	except:
		pass

	return showHandakuten


def switchCombinaison():
	global showCombinaison

	try:
		if showCombinaison == True:
			btnCombinaison.configure(fg='#ad3d3d', bg='#cfcfcf')
			showCombinaison = False
		else:
			btnCombinaison.configure(fg='#69c989', bg='#dedede')
			showCombinaison = True
	except:
		pass

	return showCombinaison



#Response check + Change character
def sendText(event):
	global showKatakana
	global showHiragana
	global showHandakuten
	global showCombinaison
	global randomChar
	global score
	global count


	try:

		if str(textEntry.get()) == letter[randomChar].lower():
			score += 1
			nope.configure(text='')
			caw.configure(text='')
			answer.configure(text='')
			plusOne.configure(text='+1')
			goodOne.configure(text='GOOD !')
		else:
			plusOne.configure(text='')
			goodOne.configure(text='')
			nope.configure(text='nope', fg= '#a83232')
			caw.configure(text='CORRECT ANSWER WAS:')
			answer.configure(text=letter[randomChar])



		if showCombinaison == True and showHandakuten == True:
			randomChar = random.randint(0, 103)

		elif showCombinaison == False and showHandakuten == True:
			randomChar = random.randint(0, 70)

		elif showCombinaison == True and showHandakuten == False:
			randomChar = random.choice([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91])

		elif showCombinaison == False and showHandakuten == False:
			randomChar = random.randint(0, 45)

		if showHiragana == True and showKatakana == True:
			choose = random.randint(1, 2)
			if choose==1:
				char.configure(text=hiragana[randomChar])
			else:
				char.configure(text=katakana[randomChar])

		elif showHiragana==False:
			char.configure(text=katakana[randomChar])

		elif showKatakana==False:
			char.configure(text=hiragana[randomChar])

		count += 1
		showScore.configure(text=str(str(score) + '/' + str(count) + ' (' + str(int(score*100/count)) + '%)'))

	except:
		pass



	textEntry.delete(0, END)





#Character
choose = 1
char = Label(window, text=hiragana[randomChar], font=('arial', 70), fg = '#5C6BC2')
char.place(x=250, y=135)

textEntry = Entry(window, width=26)
textEntry.place(x=220, y=265)

nope = Label(window, font=('Arial', 17), fg= '#303030')
nope.place(x=270, y=40)

caw = Label(window, font=('Arial', 8), fg= '#353535')
caw.place(x=234, y=72)

answer = Label(window, font=('Arial', 12), fg= '#151515')
answer.place(x=282, y=90)

plusOne = Label(window, font=('Arial', 18), fg= '#5C6BC2')
plusOne.place(x=280, y=86)

goodOne = Label(window, font=('Arial', 18), fg= '#151515')
goodOne.place(x=256, y=60)

yourScore = Label(window, text='YOUR SCORE :', font=('Arial', 12), fg='#151515')
yourScore.place(x=0, y=348)

showScore = Label(window, text='0/0 (100%)', font=('Arial', 18), fg='#5C6BC2')
showScore.place(x=0, y=369)



#Buttons
btnHiragana = Button(window, text = 'Hiragana', fg='#69c989', bg='#dedede', command=switchHiragana)
btnKatakana = Button(window, text = 'Katakana', fg='#69c989', bg='#dedede', command=switchKatakana)
btnHiragana.place(x=5, y=5)
btnKatakana.place(x=70, y=5)

btnHandakuten = Button(window, text = 'Handakuten', fg='#69c989', bg='#dedede', command=switchHandakuten)
btnHandakuten.place(x=135, y=5)

btnCombinaison = Button(window, text = 'Combinaison', fg='#69c989', bg='#dedede', command=switchCombinaison)
btnCombinaison.place(x=217, y=5)


def update():
	try:
		RPC.update(large_image="ico", large_text='JP char training', details='Training his japanese skill', state=str('Score : ' + str(score) + '/' + str(count) + ' (' + str(int(score*100/count)) + '%)'), start = startTime)
	except:
		pass

	window.after(15000, update)



#stuff
window.bind('<Return>', sendText)
textEntry.focus()
window.after(15000, update)
window.mainloop()