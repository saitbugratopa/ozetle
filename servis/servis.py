def ozetle(metin,esik):
    kelimelersay = {}
    cumlelersay = {}
    tekrar =[]
    ozet =""

    # kelimeleri " ", cümleleri . lardan böldüm
    # kelimeleri " ", cümleleri . lardan böldüm 
    # kelimeleri " ", cümleleri . lardan böldüm
    # kelimeleri " ", cümleleri . lardan böldüm 
    # kelimeleri " ", cümleleri . lardan böldüm 
    # kelimeleri " ", cümleleri . lardan böldüm
    kelimeler = metin.split(" ")
    cumleler = metin.split(".")


    # kelimelerin toplamda kaç tane geçtiğini sayıyor. Her kelimeye tekrarına göre puan veriyor.
    for kelime in kelimeler:
        if kelimelersay.get(kelime) is not None:
            kelimelersay[kelime] +=1
        else:
            kelimelersay[kelime] =1


    # 2 den fazla geçen kelimeleri alıyor. Testlerde 2 en doğru sonucu verdi değişebilir.
    for kelime in kelimelersay:
        if kelimelersay.get(kelime) > 2:
            tekrar.append(kelime)

    # kelimelerin puanları ile cümleleri puanlandırıyor. Cümlelerin puanlarını elde ediyor.
    for cumle in cumleler:
        for kelime in tekrar:
            if cumle.find(kelime) > -1:
                if cumlelersay.get(cumleler.index(cumle)) is not None:
                    cumlelersay[cumleler.index(cumle)] += 1
                else:
                    cumlelersay[cumleler.index(cumle)] = 1

    # puanı belirli sayıdan fazla olan cümleleri yazıyor.
    for a in cumlelersay:
        if cumlelersay[a] > int(esik): # Bu kısım yani Özetleme Düzeyi Metin Boyutu ve İçeriğine göre değiştirilecek.
            ozet += cumleler[int(a)]
    return ozet