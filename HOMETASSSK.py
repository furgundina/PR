a = float(input("Оцените силу вашей душевной боли по шкале от 0 до 10: "))
if a < 0.5:
    print("Кажется, вы испытываете легкое огорчение. Как человек, которому, после долгих поисков, все же предстоит спросить цену за 1 кг нектарин (っ´ω`)ﾉ(╥ω╥) Не сдавайтесь, что бы ни было на месте нектарин, оно стоит того, чтобы спросить! ")
elif 0.5 <= a <= 4.5:
    print("Вы встревожены - почти как человек, которому придется принять вызов с незнакомого номера, и это в эпоху мессенджеров! (╬ Ò﹏Ó) Советуем подключить функцию опознавания номеров, подробный гайд можете найти на данном сайте https://habr.com/ru/articles/432444/")
elif 4.5 <= a <= 6.5:
    print( "Ваш уровень тревожности сравним с ситуацией, когда вам принесли совсем не то, что вы заказывали.(μ_μ)Вам вот-вот придеться позвать официанта и попросить его поменять блюдо..")
elif 6.5 <= a <= 8.5:
    print( "Ваш уровень тревожности соответсвует уровню волнения пятиклассника, которому вот-вот предстоит рассказывать невыученный стих на глазах У ВСЕХ (×﹏×)...Позвольте предложить вам парочку способов, дабы облегчить вашу ношу: -вспомните, что вы - не пятиклассник!, -выучите стих, возможно это поможет закрыть гештальт ")
elif 8.5 <= a <= 10:
    print("＼(〇_ｏ)／Думаем, с таким уровнем тревожности, о вашем состоянии должны говорить не мы вам.. А вы нам! Опишите ваше состояние в нашем чате, а мы придумаем, как вам помочь: https://t.me/EmSup_bot ")