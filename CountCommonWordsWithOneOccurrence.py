words1 = ["bjxzvssdoq","oom","lxrrvf","aoeselhvrnw","awnornqyztqlza","bjxqkapuvaw","wibxruerngdzgjd",
          "rezrwdzvllpbjpnikhzraz","pswmnrsepudx","nlicjldpeia","glg","nllxfcjjitmsuugmr","cl","pysmpgjakkjnusfopphb",
          "zxlwcdjpn","xktsfnchwrdesnf","qptnoxxgrjmvr","exlfwjfsbsirbbkyqjtinrrwuhh","rqbnghajxygilgdjejopyuwyjqrx",
          "vrjkqsicuqoalqyaxkaaogxbf","ixnlltqbpygmpjuspom","izajsxotcbhzdnkujwgdzo","b","lighabre","i","ljqqbfddipvcooh",
          "hboedpepeeunx","bkhzhiefammwqkhvampokd","ptlozguwmyyp","loeshsjgazzwvs","kyrltbdzlymjxtvwiiq","fk",
          "mbjpgwsahkgkehlcoqbhunqchxj","nfyuvlrmiturheb","cyqwsiysmoirurj","sciqruywy","podsrhmsozan","nlyadkrxhdbup",
          "gdugldwghzt","wpjm","gjobdekmjisjgadkwwemnmco","dkjdtimdghvlhuetxyaklk","iwqylhdwqbwaqdouowoodhs","mn"]

words2 = ["eeormvovhzslwsqgzthlgntgzc","zfwownznh","suxrkdbjdjjtbkjucsbyk","u","y","lbjooktoctgwbbptiffytquha",
          "dcsxrghgpultkatbecjadbespvww","vwduylshcpaiu","rtcxwctvquaiuwkgvdx","a","szearxmdqcismljmihbtkcirztdnrc",
          "htgmuxtxdunsvfizb","hybe","nsegkgwcvopncmfpaahhhjeuqjosv","jtarnnpppxtzmopixeijqqahkd","hazcgrrnpourkyoeanodejiptne",
          "kurhokvhixihe","ljwycewmecfqdhtxiokjn","qgjzzvpyvwetlsvcsw","aunns","nwcnfrzzvxafkfjfnczummtubikji",
          "nipiygnvlfntgpxfedj","mgnt","xvjehufvaqouhztnmts","sjtbrfjwtqxakqktxjaljrbwfoxvz","dfeujeikfrtrpiafrgxvjlkpxtog",
          "u","ggbcxoasodaqaazulrxjleecexey","inedrgssajhpygfvozigohis","pevxwgfzxebybfe","cgy","fnhvlx","vxfybaebkoq",
          "xvhx","mxbqjtanctljewwjjlbpkgbtsm","mlwagamcikbcpuexhikmizp","qeiomipvsoqlsnhylulirrcwtqga","bwemqcgyusuauwlpbjjru",
          "iimcbidtndh","lpjejlkmxtlbyvnscy","dlspriicnyykdsyvswlgktavwloq","dib","qoptbduulgqwquvhdvmwdz","xrtxghrbfrhpzduxeljnctgg",
          "schmbsaupayqnpchn","kah","itotymryqufqpozrwmvsl","gurb","xsyocxcmwvqmnmxthfemmu","pkfdutm","hkbwxwjxyuld","ukdqszfjckdunnhpevw",
          "kqfwytdvnvjrchiwprcqkfntqticsc","zjmsfwjddgjiypsmagdrujb","gn","ebncbjvhpbjecbrizdpv","nbfehcktwswih","sttmqcdmobdgtgkyxydyovahknjbsn",
          "sryyufrtocf","eiicpwknxrzqylqpybhfd","pey","njimttradeoa","wcogjdfr","prva","tyxdmxgw","wluzocppg","kzm","wbyyperlkflaoxyxftzwxvmemof",
          "snzpclbulddnmmjmpdurcybo","mowxgpmzojtmympmt","uvtnojjahrovzmlukf","sykhtgejlmbzshhneoyqr","ib","haqkkizidifykwijm","csjtexnr","yvgr",
          "vzcxbtlthrynnawxnkxdptp","yvxrmscsckv"]


class Solution:
    def countWords(self, words1, words2) -> int:

        words = words1 + words2
        double_repeat = 0

        for word in words:
            if words1.count(word) == 1 and words2.count(word) == 1:
                double_repeat += 1

        return int(double_repeat / 2)