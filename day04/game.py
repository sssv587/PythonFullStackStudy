'''
掷骰子

1.欢迎进入xxxx游戏
2.输入用户名，默认用户是没有币
3.提示用户充值买币 (100块钱30币，充值必须是100的倍数，充值不成功可以再次充值)
4.玩一局游戏扣除2个币，猜大小(系统用随机模拟骰子数产生)
5.只要你猜对了奖励1个币，可以继续玩(想不想继续玩，也可以没有金币，自动退出)

'''
import random as randint

print('*'*30)
print('欢迎进入澳门赌场')
print('*'*30)

username = input('请输入顾客的大名:')
money = 0

anwser = input('确定进入游戏吗?')

while True:
	if anwser == 'y':
		# 判断游戏币是否充足
		# 做到反复充值
		while money < 2:
			n = int(input('金币不足，请充值(100块钱30币，充值必须是100的倍数):'))
			# 充值金额
			if n % 100 == 0 and n > 0:
				money=(n//100)*30
			print('当前剩余游戏币是:{},玩一局游戏扣除2个币'.format(money))

			print('进入游戏----------')

		    # 模拟骰子 产生骰子的值
		    t1 = rd.randint(1,6)
		    t2 = rd.randint(1,6)
		    # 两个骰子的值大于6，否则就是小

		    money -= 2 # 扣除金币
		 
		    print('系统清洗完毕，请猜大小:')
		    guess = int(input('输入大或者输入小:'))

		    # 判断
		    if ((t1+t2)> 6 and guess == '大') or (( t1+t2)<= 6 and guess == '小'):
		    	print('恭喜{}！本局游戏获奖励1个游戏币！'.format(username))
		    	money += 1
		    else:
		    	print('很遗憾！本局游戏输啦。')


		    input('是否再来一局游戏，要扣除2枚游戏币?(y/n)')
		    if anwser != 'y' or money < 2:
		    	print('退出游戏啦！！！！')
		    	break
