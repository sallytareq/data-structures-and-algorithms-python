from data_structures_and_algorithms.challenges.hashtable.hashtable import Hashtable

# hm1 contains synonyms & hm2 contains antonyms 
def left_join(hm1,hm2):
    try:
        output = Hashtable(hm1.size)

        for key in hm1.map:
            # print(key)
            if key:
                index = hm1.hash(key.head.value[0])
                # print(index)
                output.add(key.head.value[0],key.head.value[1])
                # print(hm2.map[index].head.value[0])
                # print(key.head.value[0])
                if hm2.map[index]:
                    if hm2.map[index].head.value[0] == key.head.value[0]:
                        output.map[index].head.value.append(hm2.map[index].head.value[1])
                    else:
                        output[index].head.value.append(None)

        return output
    except:
        return 'Invalid Input'

if __name__ == "__main__":
    hm1 = Hashtable(1024)
    hm1.add('fond','enamored')
    hm1.add('wrath','anger')
    hm1.add('diligent','employed')
    hm1.add('seize','grab')
    hm1.add('guide','usher')
    hm2 = Hashtable(1024)
    hm2.add('fond','averse')
    hm2.add('wrath','delight')
    hm2.add('diligent','idle')
    hm2.add('guide','follow')
    hm2.add('flow','jam')

    x = left_join(hm1,hm2)
    for n in x.map:
        if n:
            print(n.head.value)